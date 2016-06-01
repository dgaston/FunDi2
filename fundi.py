#!/usr/bin/env python

import sys
import argparse
from ete3 import Tree

from fundi import fundi
from fundi import configuration


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--configuration', help="Configuration file for various settings")
    parser.add_argument('-t', '--tree', help='Input tree file')
    parser.add_argument('-a', '--alignment', help='Input alignment file')
    args = parser.parse_args()
    args.logLevel = "INFO"

    config = configuration.configure_runtime(args.configuration)

    with open(args.tree, 'r') as treefile:
        tree_string = treefile.read().replace('\n', '')
    input_tree = Tree(tree_string)

    subtree_taxa = fundi.get_subtrees()
    tree.get_common_ancestor([node1, node2, node3])
