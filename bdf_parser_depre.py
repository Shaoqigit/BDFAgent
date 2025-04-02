from pyNastran.bdf.bdf import BDF


class BDFParser:

    def __init__(self, filepath):
        self.model = BDF()
        self.model.read_bdf(filepath)

    def get_node_count(self):
        return len(self.model.nodes)

    def get_node_ids(self):
        return list(self.model.nodes.keys())

    def get_element_count(self):
        return len(self.model.elements)

    def get_elements_by_type(self, element_type):
        return [
            e for e in self.model.elements.values()
            if e.type == element_type.upper()
        ]

    def get_material_properties(self, material_id):
        return self.model.materials[material_id]

    def get_loads(self):
        return self.model.loads
