"""
pythoneda/sandbox/flows/sample/sample.py

This file declares the Sample class.

Copyright (C) 2024-today rydnr's pythoneda-sandbox/flow-sample

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda import Flow


class Sample(Flow):
    """
    A sample flow.

    Class name: Sample

    Responsibilities:
        - Show a simple flow.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new Sample instance.
        """
        super().__init__()