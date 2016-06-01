"""
.. module:: iqtree
   :platform: Unix, OSX
   :synopsis: A module for calling and interacting with output from IQ-TREE
   into additional formats.

.. moduleauthor:: Daniel Gaston <daniel.gaston@dal.ca>


"""

from fundi import fundi


def iqtree(config):
    """Generate RAxML command-line call
    :param config: The configuration dictionary.
    :type config: dict
    """

    logfile = "{}.iqtree.log".format(config['run_name'])

    command = ("{}".format(config['iqtree']['bin'])
               )

    fundi.run_and_log_command(" ".join(command), logfile)

    return logfile
