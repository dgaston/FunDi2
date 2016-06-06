class Subgroup:
    subgroups = {}

    @classmethod
    def create(cls, name):
        subgroup = Subgroup(name)
        cls.subgroups[name] = subgroup

        return subgroup

    def __init__(self, name):
        self.name = name