"""
.. module:: qmmraxml
   :platform: Unix, OSX
   :synopsis: A module for calling and interacting with output from QmmRAxML
   into additional formats.

.. moduleauthor:: Daniel Gaston <daniel.gaston@dal.ca>


"""

from fundi import fundi


def qmmraxml(config):
    """Generate QmmRAxML command-line call
    :param config: The configuration dictionary.
    :type config: dict
    """

    logfile = "{}.qmmraxml.log".format(config['run_name'])

    command = ("{}".format(config['qmmraxml']['bin'])
               )

    fundi.run_and_log_command(" ".join(command), logfile)

    return logfile
