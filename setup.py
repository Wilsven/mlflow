from setuptools import find_packages, setup

from template import PROJECT_NAME

HYPEN_E_DOT = "-e ."


def get_requirements() -> list[str]:
    """Returns a list of requirements.

    Reads all requirements in the `requirements.txt` file and
    returns a list of requirements.

    Returns:
        list[str]: List of requirements
    """
    with open("requirements.txt", "r") as f:
        requirements = [req.strip() for req in f.readlines()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


PROJECT_NAME = PROJECT_NAME
__version__ = "0.0.1"
AUTHOR = "Wilsven"
AUTHOR_EMAIL = "wilsven_leong96@hotmail.co.uk"

setup(
    name=PROJECT_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=f"https://github.com/{AUTHOR}/{PROJECT_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR}/{PROJECT_NAME}/issues"},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements(),
)
