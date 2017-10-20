#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Thomas Meeus
# Copyright (c) 2017 Thomas Meeus <thomas@sector7g.be>
#
# License: MIT
#

"""This module exports the Yamllint plugin class."""

from SublimeLinter.lint import PythonLinter, util


class Yamllint(PythonLinter):
    """Provides an interface to yamllint."""

    syntax = ('yml', 'yaml')
    cmd = ('yamllint@python3', '-f', 'parsable', '*')
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.9'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): \[((?P<warning>warning)|(?P<error>error))\] (?P<message>.+)'
    )
    tempfile_suffix = '-'
    error_stream = util.STREAM_STDOUT
    word_re = r'^(".*?"|[-\w]+)'
    module = 'yamllint'
