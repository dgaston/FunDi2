#!/usr/bin/env python

import sys
import argparse
from ete3 import Tree
from collections import defaultdict

from fundi import fundi
from fundi import configuration


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--configuration', help="Configuration file for various settings")
    parser.add_argument('-t', '--tree', help='Input tree file')
    parser.add_argument('-a', '--alignment', help='Input alignment file')
    args = parser.parse_args()
    args.logLevel = "INFO"

    sys.stdout.write("Parsing the provided input configuration file {}\n".format(args.configuration))
    config = configuration.configure_runtime(args.configuration)

    sys.stdout.write("Reading the provided tree file {}\n".format(args.tree))
    with open(args.tree, 'r') as treefile:
        tree_string = treefile.read().replace('\n', '')
    input_tree = Tree(tree_string)

    sys.stdout.write("Reading the provided alignment file {}\n".format(args.alignment))
    # Return the alignment as a BioPython Bio AlignIO object
    alignment = fundi.process_alignment(args.alignment, config)

    sys.stdout.write("Parsing subtrees based on definitions from configuration file")
    # Parse the provided tree file into defined subtrees and return as a list of ETE Tree objects
    subtrees = defaultdict(dict)
    subtrees = fundi.parse_subgroups(input_tree, config, alignment, subtrees, config['subgroups'])

