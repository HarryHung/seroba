import glob
from setuptools import setup, find_packages

setup(
    name='seroba',
    version='2.0.4',
    description='SEROBA: Serotyping for illumina reads',
    packages = find_packages(),
    author='Lennard Epping',
    author_email='path-help@sanger.ac.uk',
    url='https://github.com/sanger-pathogens/seroba',
    scripts=glob.glob('scripts/*'),
    test_suite='nose.collector',
    tests_require=['nose >= 1.3'],
    install_requires=[
        'ariba >= 2.9.1',
        'pymummer==0.10.3',
        'PyYAML>=3.12',
        'biopython>=1.68',
        'pyfastaq>=3.15.0'
    ],
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
