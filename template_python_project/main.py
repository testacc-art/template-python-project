# This file is part of template-python-project.
#
# ProjectPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ProjectPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ProjectPy. If not, see <https://www.gnu.org/licenses/>.

import fire


def main(name: str = "World") -> None:
    """Main function.

    Executes the main function block of the program.

    Args:
        name (str): Name to say hello to

    Returns:
        None.
    """
    print(f"Hello, {name}!")


def run() -> None:  # pragma: no cover
    """Run function.

    Runs the problem providing parsing of the command line arguments.

    Args:
        None.

    Returns:
        None.
    """
    fire.Fire(main)


if __name__ == "__main__":  # pragma: no cover
    run()
