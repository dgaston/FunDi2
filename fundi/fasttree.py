"""
.. module:: fasttree
   :platform: Unix, OSX
   :synopsis: A module for calling and interacting with output from FastTree
   into additional formats.

.. moduleauthor:: Daniel Gaston <daniel.gaston@dal.ca>


"""

from fundi import fundi


def fasttree(config):
    """Generate RAxML command-line call
    :param config: The configuration dictionary.
    :type config: dict
    """

    logfile = "{}.fasttree.log".format(config['run_name'])

    command = ["{}".format(config['fasttree']['bin'])
               ]

    fundi.run_and_log_command(" ".join(command), logfile)

    return logfile
