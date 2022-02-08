"""genft

usage: genft [-hv] (-d MIXDB) [-i MIXID] [-o OUTPUT]

options:
    -h, --help
    -v, --verbose                   Be verbose.
    -d MIXDB, --mixdb MIXDB         Mixture database JSON file.
    -i MIXID, --mixid MIXID         Mixture IDs JSON file.
    -o OUTPUT, --output OUTPUT      Output HDF5 file.

Generate a SonusAI feature/truth file from a SonusAI mixture database.

Inputs:
    MIXDB       A SonusAI mixture database JSON file.
    MIXID       A JSON file containing a list of mixture IDs. The list should be named 'mixid'.
                If no file is provided, then all mixtures in the database will be generated.

Outputs:
    OUTPUT.h5   A SonusAI feature HDF5 file (containing 'feature' and 'truth_f' datasets).
    genft.log

"""

import json
from copy import deepcopy
from itertools import zip_longest
from os.path import exists
from os.path import splitext
from typing import List
from typing import Union

import h5py
import numpy as np
from docopt import docopt
from pyaaware import FeatureGenerator
from pyaaware import ForwardTransform
from tqdm import tqdm

import sonusai
from sonusai import create_file_handler
from sonusai import initial_log_messages
from sonusai import logger
from sonusai import update_console_handler
from sonusai.mixture import apply_augmentation
from sonusai.mixture import build_noise_audio_db
from sonusai.mixture import build_target_audio_db
from sonusai.mixture import generate_truth
from sonusai.mixture import get_mixtures_from_mixid
from sonusai.mixture import get_total_class_count
from sonusai.mixture import process_mixture_audio
from sonusai.mixture import truth_reduction
from sonusai.utils import human_readable_size
from sonusai.utils import int16_to_float
from sonusai.utils import seconds_to_hms
from sonusai.utils import trim_docstring


def genft(mixdb: dict,
          mixid: Union[str, List[int]],
          start_offset: int = 0,
          logging: bool = True,
          show_progress: bool = False) -> (np.ndarray, np.ndarray, dict):
    mixdb_out = deepcopy(mixdb)
    mixdb_out['mixtures'] = get_mixtures_from_mixid(mixdb_out['mixtures'], mixid)

    if not mixdb_out['mixtures']:
        logger.error('Error processing mixid: {}; resulted in empty list of mixtures'.format(mixid))
        exit()

    total_samples = sum([sub['samples'] for sub in mixdb_out['mixtures']])

    fft = ForwardTransform(N=mixdb_out['frame_size'] * 4, R=mixdb_out['frame_size'])
    fg = FeatureGenerator(frame_size=mixdb_out['frame_size'],
                          feature_mode=mixdb_out['feature'],
                          num_classes=mixdb_out['num_classes'],
                          truth_mutex=mixdb_out['truth_mutex'])

    transform_frames = total_samples // mixdb_out['frame_size']
    feature_frames = total_samples // mixdb_out['feature_step_samples'] - start_offset

    feature = np.empty((feature_frames, fg.stride, fg.num_bands), dtype=np.single)
    truth_f = np.empty((feature_frames, fg.num_classes), dtype=np.single)

    if logging:
        logger.info('')
        logger.info('Found {} mixtures to process'.format(len(mixdb_out['mixtures'])))
        logger.info('{} samples, {} transform frames, {} feature frames'.format(total_samples, transform_frames,
                                                                                feature_frames))

    noise_audios = build_noise_audio_db(mixdb_out)
    target_audios = build_target_audio_db(mixdb_out)

    i_sample_offset = 0
    i_frame_offset = 0
    o_frame_offset = 0
    feature_frame = 0
    for mixture_record in tqdm(mixdb_out['mixtures'], desc='genft', disable=not show_progress):
        noise_audio, target_audio = process_mixture_audio(i_frame_offset=i_frame_offset,
                                                          i_sample_offset=i_sample_offset,
                                                          o_frame_offset=o_frame_offset,
                                                          mixdb=mixdb_out,
                                                          mixture_record=mixture_record,
                                                          target_audios=target_audios,
                                                          noise_audios=noise_audios)

        mixture_audio = np.array(target_audio + noise_audio, dtype=np.int16)

        truth = generate_truth(mixdb=mixdb_out, mixture_record=mixture_record, target_audio=target_audio)

        for offset in range(0, mixture_record['samples'], mixdb_out['frame_size']):
            mixture_fd = fft.execute(int16_to_float(mixture_audio[offset:offset + mixdb_out['frame_size']]))
            fg.execute(mixture_fd,
                       truth_reduction(truth[:, offset:offset + mixdb_out['frame_size']],
                                       mixdb_out['truth_reduction_function']))
            if fg.eof():
                # start_offset is used when generating one batch at a time and makes it
                # possible to preserve the mixture data sequence across batch boundaries
                if start_offset != 0:
                    start_offset -= 1
                else:
                    feature[feature_frame] = np.reshape(fg.feature(), (fg.stride, fg.num_bands))
                    truth_f[feature_frame] = fg.truth()
                    feature_frame += 1

        fft.reset()
        fg.reset()

        i_sample_offset += mixture_record['samples']
        i_frame_offset += mixture_record['samples'] // mixdb_out['frame_size']
        o_frame_offset += mixture_record['samples'] // mixdb_out['feature_step_samples']

    mixdb_out['class_count'] = get_total_class_count(mixdb_out)

    duration = total_samples / sonusai.mixture.sample_rate
    if logging:
        logger.info('')
        logger.info('Duration: {}'.format(seconds_to_hms(seconds=duration)))
        logger.info('feature:  {}'.format(human_readable_size(feature.nbytes, 1)))
        logger.info('truth_f:  {}'.format(human_readable_size(truth_f.nbytes, 1)))

    return feature, truth_f, mixdb_out


def grouper(iterable, n):
    args = [iter(iterable)] * n
    result = zip_longest(*args, fillvalue=None)
    return [list(filter(None.__ne__, x)) for x in result]


def main():
    try:
        args = docopt(trim_docstring(__doc__), version=sonusai.version(), options_first=True)

        verbose = args['--verbose']
        mixdb_name = args['--mixdb']
        mixid_name = args['--mixid']
        output_name = args['--output']

        if not output_name:
            output_name = splitext(mixdb_name)[0] + '.h5'

        log_name = 'genft.log'
        create_file_handler(log_name)
        update_console_handler(verbose)
        initial_log_messages('genft')

        if not exists(mixdb_name):
            logger.error('{} does not exist'.format(mixdb_name))
            exit()

        with open(mixdb_name, encoding='utf-8') as f:
            mixdb = json.load(f)

        if not mixid_name:
            mixid = list(range(len(mixdb['mixtures'])))
        else:
            if not exists(mixid_name):
                logger.error('{} does not exist'.format(mixid_name))
                exit()

            with open(mixid_name, encoding='utf-8') as f:
                mixid = json.load(f)
                if not isinstance(mixid, dict) or 'mixid' not in mixid.keys():
                    logger.error('Could not find ''mixid'' in {}'.format(mixid_name))
                    exit()
                mixid = mixid['mixid']

        mixtures = get_mixtures_from_mixid(mixdb['mixtures'], mixid)

        mixid = grouper(mixid, 100)
        frame_offset = 0
        feature_elems = 0
        truth_elems = 0
        with h5py.File(output_name, 'w') as f:
            for idx, val in enumerate(mixid):
                logger.info('Processing chunk {} of {}'.format(idx + 1, len(mixid)))
                feature, truth_f, _ = genft(mixdb=mixdb,
                                            mixid=val,
                                            logging=False,
                                            show_progress=True)

                if frame_offset == 0:
                    feature_dataset = f.create_dataset(name='feature',
                                                       data=feature,
                                                       maxshape=(None, feature.shape[1], feature.shape[2]))
                    truth_dataset = f.create_dataset(name='truth_f',
                                                     data=truth_f,
                                                     maxshape=(None, truth_f.shape[1]))
                    feature_elems = feature.shape[1] * feature.shape[2]
                    truth_elems = truth_f.shape[1]
                else:
                    feature_dataset.resize(frame_offset + feature.shape[0], axis=0)
                    feature_dataset[frame_offset:] = feature
                    truth_dataset.resize(frame_offset + feature.shape[0], axis=0)
                    truth_dataset[frame_offset:] = truth_f
                frame_offset += feature.shape[0]

        logger.info('Wrote {}'.format(output_name))
        total_samples = sum([sub['samples'] for sub in mixtures])
        duration = total_samples / sonusai.mixture.sample_rate
        logger.info('')
        logger.info('Duration: {}'.format(seconds_to_hms(seconds=duration)))
        logger.info('feature:  {}'.format(human_readable_size(frame_offset * feature_elems * 4, 1)))
        logger.info('truth_f:  {}'.format(human_readable_size(frame_offset * truth_elems * 4, 1)))

    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        exit()


if __name__ == '__main__':
    main()
