"""
.. module:: FunDi
   :platform: Unix, OSX
   :synopsis: A module containing all appropriate methods for FunDI2 function
   into additional formats.

.. moduleauthor:: Daniel Gaston <daniel.gaston@dal.ca>


"""

import sys
import subprocess as sub


def run_and_log_command(command, logfile):
    """This function uses the python subprocess method to run the specified command and writes all error to the
    specified logfile

    :param command: The command-line command to execute.
    :type name: str.
    :param logfile: The logfile to output error messages to.
    :type logfile: str.
    :returns:  Nothing
    :raises: RuntimeError

    """

    with open(logfile, "wb") as err:
        sys.stdout.write("Executing {} and writing to logfile {}\n".format(command, logfile))
        err.write("Command: {}\n".format(command))
        p = sub.Popen(command, stdout=sub.PIPE, stderr=err, shell=True)
        output = p.communicate()
        code = p.returncode
        if code:
            raise RuntimeError("An error occurred when executing the commandline: {}. "
                               "Please check the logfile {} for details\n".format(command, logfile))
