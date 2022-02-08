from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = 'SEING is a C/C++ package for fingerprint calculations suitable for machine learning studies of molecular systems.'
LONG_DESCRIPTION = 'SEING was developed in the Clancy Group (https://clancygroup.wse.jhu.edu/). Fingerprints (in this context) are numerical representations of chemical environments designed to be invariant under property-perseving operations such as permutation of atoms of the same nature, geometric rotation, etc. For more information on fingerprints in general and the ones currently implemented in SEING, please see the official documentation and user-guide.'

# Setting up
setup(
    name="pyseing",
    version=VERSION,
    author="Mardochee Reveil",
    author_email="<mr937@cornell.edu>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[]
)
