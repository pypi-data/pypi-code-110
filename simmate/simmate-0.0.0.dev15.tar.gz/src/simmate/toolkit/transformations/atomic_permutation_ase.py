# -*- coding: utf-8 -*-

from simmate.toolkit.transformations.base import Transformation


class AtomicPermutationASE(Transformation):

    # known as PermutationMutation in ase.ga
    # https://gitlab.com/ase/ase/-/blob/master/ase/ga/standardmutations.py

    io_scale = "one_to_one"
    ninput = 1
    use_multiprocessing = False

    def __init__(
        self,
        composition,
        ratio_of_covalent_radii=0.1,
    ):

        # we can assume the user has ASE installed because it is a dependency of PyMatgen
        #!!! it looks like the ase.ga module is actively changing so version may introduce errors
        from ase.ga.utilities import closest_distances_generator

        # the closest_distances_generator is exactly the same as an element-dependent distance matrix
        # expect ASE puts this in dictionary form
        # the function requires a list of element integers
        element_ints = [element.number for element in composition]
        # the default of the ratio of covalent radii (0.1) is based on the ASE tutorial of this function
        self.element_distance_matrix = closest_distances_generator(
            element_ints, ratio_of_covalent_radii
        )

        # we also need to convert pymatgen Structures to ase Atoms below
        #!!! is it faster and more memory efficient to import below?
        from pymatgen.io.ase import AseAtomsAdaptor

        self.adaptor = AseAtomsAdaptor

    def apply_transformation(self, structure):

        ### CHECK FOR BUGS

        # This mutation is not possible for structures that have only one element
        if len(structure.composition.elements) == 1:
            print(
                "You cannot perform an atomic permutation on structure that only has one element type!!"
            )
            return False

        ### RUN

        # first I need to convert the structures to an ASE atoms object
        structure_ase = self.adaptor.get_atoms(structure)

        # now we can make the generator
        from ase.ga.standardmutations import PermutationMutation

        perm = PermutationMutation(
            n_top=int(
                structure.composition.num_atoms
            ),  # number of atoms to optimize. I set this to all
            probability=0.33,  # probability an atom is permutated
            # test_dist_to_slab=True,
            # use_tags=False,
            blmin=self.element_distance_matrix,  # distance cutoff matrix
            # rng=np.random,
            # verbose=False
        )

        #!!! Their code suggests the use of .get_new_individual() but I think .mutate() is what we'd like
        new_structure_ase = perm.mutate(structure_ase)

        # if the mutation fails, None is return
        if not new_structure_ase:
            return False

        # if it was successful, we have a new Atoms object
        # now convert back to a pymatgen object
        new_structure = self.adaptor.get_structure(new_structure_ase)

        return new_structure
