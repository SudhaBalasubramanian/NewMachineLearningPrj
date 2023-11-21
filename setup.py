from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'housing_predictor'
VERSION = "0.0.5"
DESCRIPTION = "My first machine learning project"
AUTHOR = "Sudha B"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name = PROJECT_NAME,
    version = VERSION,
    description = DESCRIPTION,
    author = AUTHOR,
    packages = PACKAGES,
    install_requires = get_requirements_list()
)
