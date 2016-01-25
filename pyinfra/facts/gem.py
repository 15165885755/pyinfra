# pyinfra
# File: pyinfra/facts/gem.py
# Desc: facts for the RubyGems package manager

import re

from pyinfra.api import FactBase


class GemPackages(FactBase):
    '''
    Returns a dict of installed gem packages:

    .. code:: python

        'package_name': 'version',
        ...
    '''

    command = 'gem list --local'
    _regex = r'^([a-zA-Z0-9\-\+\_]+)\s\(([0-9\.]+)\)$'

    def process(self, output):
        packages = {}

        for line in output:
            matches = re.match(self._regex, line)
            if matches:
                packages[matches.group(1)] = matches.group(2)

        return packages
