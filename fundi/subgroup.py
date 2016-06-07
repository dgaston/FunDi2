class Subgroup:
    subgroups = {}

    @classmethod
    def create(cls, name, alignment, tree):
        subgroup = Subgroup(name, alignment, tree)
        cls.subgroups[name] = subgroup

        return subgroup

    def __init__(self, name, alignment, tree):
        self.name = name
        self.alignment = alignment
        self.tree = tree
