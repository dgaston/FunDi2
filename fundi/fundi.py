"""
.. module:: FunDi
   :platform: Unix, OSX
   :synopsis: A module containing all appropriate methods for FunDI2 function
   into additional formats.

.. moduleauthor:: Daniel Gaston <daniel.gaston@dal.ca>


"""

import sys
import subprocess as sub

from Bio import AlignIO
from Bio import MultipleSeqAlignment
from subgroup import Subgroup


def run_and_log_command(command, logfile):
    """This function uses the python subprocess method to run the specified command and writes all error to the
    specified logfile
    :param command: The command-line command to execute.
    :type command: str.
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
        err.write(output)
        code = p.returncode
        if code:
            raise RuntimeError("An error occurred when executing the commandline: {}. "
                               "Please check the logfile {} for details\n".format(command, logfile))


def parse_subgroups(tree, config, alignment, subtrees, subgroups):
    """This function takes the subtree taxa definitions and returns subtrees as trees. Note
    that this method features a recursive function call strategy to deal with correct partitioning of
    unrooted trees where one subgroup may be nested within another and parsing must occur in order
    :param tree: The command-line command to execute.
    :type tree: ETE Tree Object.
    :param config: The run-time configuration object.
    :type config: dict.
    """

    unpruned = list()
    # Get subtree definitions
    for taxon_list in subgroups:
        if tree.check_monophyly(values=taxon_list, target_attr="name"):
            # Remove the defined subtree from the full tree
            ancestor = tree.get_common_ancestor(taxon_list)

            # Check that only the desired taxa are in the subtree
            ok = True
            leaf_names = ancestor.get_leaf_names()
            for name in leaf_names:
                if name not in taxon_list:
                    sys.stderr.write("WARNING: Leaf Node {} found in subtree when attempting parsing. "
                                     "Skipping...\n".format(name))
                    ok = False

            if ok:
                subtree = ancestor.detach()
                subalignment = get_subalignment(alignment, leaf_names)
                subgroup_id = Subgroup.create(subtree, subalignment)

                with open("{}_subgroup_{}.tre".format(config['run_id'], subgroup_id)) as subtree:
                    subtree.write(ancestor.write())
                with open("{}_subgroup_{}.phy".format(config['run_id'], subgroup_id), 'w') as out_alignfh:
                    AlignIO.write(alignment, out_alignfh, 'phylip')
            else:
                unpruned.append(taxon_list)

    # Recursive function calling
    if len(unpruned) > 1:
        subtrees = parse_subgroups(tree, config, subtrees, unpruned)
    else:
        # Probably need a clean up step here to collapse any internal nodes with their only descendant(s) being
        # internal nodes
        subtrees.append(tree)

    return subtrees


def get_subalignment(alignment, names):
    """This function takes an AlignIO object and retrieves just the sequences of interest
    :param alignment: The input alignment.
    :type alignment: AlignIO object.
    :param names: The list of names that comprise the subgroup of interest.
    :type names: list.
    """
    records = list()
    for record in alignment:
        if record.id in names:
            records.append(record)

    subalign = MultipleSeqAlignment(records, annotations={"tool": "demo"})

    return subalign


def process_alignment(align_file, config):
    """This function processes the provided alignment file. Simply opens if the file format is phylip,
    otherwise the file format is converted to phylip format and returned
    :param align_file: The input alignment file name.
    :type align_file: str.
    :param config: The run-time configuration object.
    :type config: dict.
    """

    # This may not work. May need to nest the with opens and keep the input file open as it doesn't read it all in?
    # Discovered this wen writing fixFAsta.py file in ddb-tools repo.
    if config['align_format'] != 'phylip':
        with open(align_file, 'r') as alignfh:
            alignment = AlignIO.parse(alignfh, config['align_format'])
        with open("{}.converted.phy".format(align_file), 'w') as out_alignfh:
            AlignIO.write(alignment, out_alignfh, 'phylip')
        align_file = "{}.converted.phy".format(align_file)

    with open(align_file, 'r') as alignfh:
        alignment = AlignIO.read(alignfh, config['align_format'])

    return alignment
