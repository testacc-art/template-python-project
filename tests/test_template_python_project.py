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
# along with template-python-project. If not, see <https://www.gnu.org/licenses/>.

from io import StringIO

import template_python_project
import unittest
import unittest.mock


class TestTemplatePythonProject(unittest.TestCase):
    def test_main_default_output(self):
        with unittest.mock.patch("sys.stdout", new=StringIO()) as stdout:
            template_python_project.main()
            self.assertEqual(stdout.getvalue(), "Hello, World!\n")

    def test_main_with_different_name(self):
        with unittest.mock.patch("sys.stdout", new=StringIO()) as stdout:
            template_python_project.main(name="Test")
            self.assertEqual(stdout.getvalue(), "Hello, Test!\n")


if __name__ == "__main__":
    unittest.main()
