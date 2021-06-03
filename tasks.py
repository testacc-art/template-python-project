# This file is part of template-python-project.
#
# template-python-project is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# template-python-project is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with template-python-project. If not, see <https://www.gnu.org/licenses/>.

from collections import defaultdict
from invoke import task
from pathlib import Path
from setuptools import find_packages
from setuptools.config import read_configuration
from typing import Any


# #####################################################################################################################
# GLOBALS
# #####################################################################################################################

BUILD_DIR = Path("./build")
DIST_DIR = Path("./dist")
TEST_DIR = Path("./tests")
COVERAGE_REPORT_DIR = BUILD_DIR / Path("coverage")
DOCS_BUILD_DIR = BUILD_DIR / Path("docs")
IGNORE_PACKAGES = ["tests"]


# #####################################################################################################################
# SUPPORTING CLASSES AND FUNCTIONS
# #####################################################################################################################


class Project:
    """A singleton class providing basic properties related to the project"""

    _config: defaultdict[Any, dict]
    _instance: Any = None

    def __init__(self) -> None:
        self._config = read_configuration("setup.cfg")

    def __new__(klass, *args, **kwargs) -> Any:
        if not isinstance(klass._instance, klass):
            klass._instance = object.__new__(klass, *args, **kwargs)

        return klass._instance

    @property
    def config(self) -> defaultdict[Any, dict]:
        return self._config

    @property
    def name(self) -> str:
        return self.config["metadata"]["name"]

    @property
    def modules(self) -> list[str]:
        return [module for module in find_packages() if module not in IGNORE_PACKAGES]


# #####################################################################################################################
# TASKS
# #####################################################################################################################


@task
def build(c):
    """Build source and wheel packages"""
    c.run("python setup.py sdist bdist_wheel")


@task
def clean(c):
    """Remove build files and directories"""
    c.run("python setup.py clean")
    c.run("coverage erase")
    c.run("rm -rf *.egg-info")
    c.run(f"rm -rf {COVERAGE_REPORT_DIR}")
    c.run(f"rm -rf {DOCS_BUILD_DIR}")
    c.run(f"rm -rf {BUILD_DIR}/bdist.*")
    c.run(f"rm -rf {BUILD_DIR}/lib")
    c.run(f"rm -rf {DIST_DIR}/*.tar.gz")
    c.run(f"rm -rf {DIST_DIR}/*.whl")


@task
def docs(c):
    """Build documentation"""
    project = Project()

    for module in project.modules:
        c.run(f"sphinx-apidoc -o docs {module}")

    c.run("sphinx-build -M html docs build/docs")


@task
def install(c):
    """Install the project inside the virtual environment"""
    c.run("pip install -e .")


@task
def lint(c):
    """Check the code for syntax issues and style"""
    c.run("black .")

    project = Project()

    for module in project.modules:
        c.run(f"mypy {module}")


@task(help={"pypi_test": "Release the package to PyPi Test service"})
def release(c, pypi_test=False):
    """Release the package to PyPi"""
    c.run(f"twine upload {'-r testpypi' if pypi_test else ''} dist/*")


@task(clean)
def reset(c):
    """Removes build files, directories and test environment"""
    c.run("rm -rf .tox")


@task
def scan(c):
    """Scan the project for security vulnerabilities"""
    c.run("snyk test --fail-on=upgradable")


@task
def test(c):
    """Test the project"""
    c.run("tox -o --pre -p auto")


@task
def test37(c):
    """Test the project using only Python 3.7"""
    c.run("tox -e py37 -o --pre -p auto")


@task
def test38(c):
    """Test the project using only Python 3.8"""
    c.run("tox -e py38 -o --pre -p auto")


@task
def test39(c):
    """Test the project using only Python 3.9"""
    c.run("tox -e py39 -o --pre -p auto")
