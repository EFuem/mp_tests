from setuptools import setup, find_packages

setup(
    name = "mp_tests",
    version = "0.0.1",
    author = "Eric Fuemmeler",
    description = ("A suite of property tests for Materials Project data using KIM models or arbitrary ASE Calculators"),
    license = "BSD",
    packages=find_packages(),
    package_data={"": ['*.pkl', '*.edn']},
    include_package_data=True,
    install_requires = [
        'numpy==1.26.4',
        'tqdm',
        'tinydb',
        'kim-tools @  git+https://github.com/openkim/kim-tools.git',
        'pymatgen',
        'numdifftools',
        'kimvv @ git+https://github.com/openkim/kimvv.git',
    ],
)
