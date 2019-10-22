#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Bruno JJE
# Copyright (c) 2015 Bruno JJE
#
# Modified for 
# SublimeLinter defaults/selector usage
# (c) 2019 David Goncalves
#
# License: MIT
#

"""This module exports the Ghdl plugin class."""

from SublimeLinter.lint import Linter


class Ghdl(Linter):

    """Provides an interface to ghdl."""
    cmd = 'ghdl -a @'
    version_re = r'GHDL (?P<version>\d+\.\d+)'
    version_requirement = '>= 0.31'
    tempfile_suffix = 'vhd'
    defaults = {
    'selector': 'source.vhdl',
    }

    # Here is a sample ghdl error output:
    # ----8<------------
    # filtre8.vhd:35:3: object class keyword such as 'variable' is expected
    # ----8<------------

    regex = (
        r"^(?P<path>.*)(?P<error>:)(?P<line>[0-9]+):(?P<col>[0-9]+)"
        r": (?P<message>.*)"
    )

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method to prefix the error message with the
        linter name.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if match:
            message = '[ghdl] ' + message

        return match, line, col, error, warning, message, near
