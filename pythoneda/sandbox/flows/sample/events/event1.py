# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/flows/sample/events/event1.py

This file declares the Event1 class.

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
from pythoneda.shared import Event


class Event1(Event):
    """
    A meaningless event.

    Class name: Event1

    Responsibilities:
        - Be used in tests.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new Event1 instance.
        """
        super().__init__()
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
