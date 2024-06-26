from setuptools import setup, find_packages

setup(
    name = "mp_tests",
    version = "0.0.1",
    author = "Eric Fuemmeler",
    description = ("A suite of property tests for Materials Project data using KIM models or arbitrary ASE Calculators"),
    license = "BSD",
    packages=find_packages(),
    package_data={"": ['*.pkl']},
    include_package_data=True,
    install_requires = [
        'tqdm',
        'tinydb',
        'numdifftools',
        'pymatgen',
        'kim_property',
        'kim-test-utils @  git+https://github.com/EFuem/kim-test-utils.git'
    ],
)
