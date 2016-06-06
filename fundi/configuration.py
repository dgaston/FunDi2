"""
.. module:: config
   :platform: Unix, OSX
   :synopsis: A module for dealing with run-time configuration data
   into additional formats.

.. moduleauthor:: Daniel Gaston <daniel.gaston@dal.ca>


"""

import sys
import ConfigParser
from collections import defaultdict


def configure_runtime(infile):
    """Parse the configuration settings from a file
    :param infile: input filename
    :type infile: string.
    :returns:  dict -- A configuration dictionary.
    """

    configuration = defaultdict()
    config = ConfigParser.SafeConfigParser()
    config.read(infile)

    try:
        config.options('settings')
    except ConfigParser.NoSectionError:
        sys.stderr.write("No section: settings in file\n")
        sys.exit()

    try:
        config.options('subgroups')
    except ConfigParser.NoSectionError:
        sys.stderr.write("No section: subgroups in file\n")
        sys.exit()

    # Set all options specified in file
    for option in config.options('settings'):
        configuration[option] = config.get('settings', option)

    for subgroup in config.options('subgroups'):
        taxon_string = config.get('subgroups', subgroup)
        configuration[subgroup] = taxon_string.split()

    # Configure individual tools
    for section in config.sections():
        if section != 'settings' and section != 'subgroups':
            tool = section
            options = config.options(tool)
            tool_dict = dict()

            # Set all specified options
            for option in options:
                tool_dict[option] = config.get(tool, option)

            configuration[tool] = tool_dict

    return configuration
