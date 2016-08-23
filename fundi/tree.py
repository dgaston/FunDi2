"""
.. module:: tree
   :platform: Unix, OSX
   :synopsis: A module containing methods for working with phylogenetic trees
   into additional formats.

.. moduleauthor:: Daniel Gaston <daniel.gaston@dal.ca>


"""

from ete3 import Tree


def read_tree(filename):
    tree = Tree(filename)

    return tree


def write_tree(tree, filename):
    tree.write(outfile=filename)


def is_monophyletic(tree, values, attr):

    return tree.check_monophyly(values=values, target_attr=attr, ignore_missing=True)


def parse_subtree(tree, node_list):
    node = tree.get_common_ancestor(node_list)

    subtree = node.detach()

    return subtree
