import openai

from bdf_parser import BDFParser
from function_call import functions


class BDFAgent:

    def __init__(self, bdf_file):
        self.parser = BDFParser(bdf_file)
        self.functions = {
            "get_node_count": self.handle_node_count,
            "get_elements_by_type": self.handle_elements_by_type,
            "get_material_properties": self.handle_material_properties
        }

    def handle_node_count(self, _):
        return f"Total nodes: {self.parser.get_node_count()}"

    def handle_elements_by_type(self, params):
        element_type = params["element_type"]
        elements = self.parser.get_elements_by_type(element_type)
        return f"Found {len(elements)} {element_type} elements"

    def handle_material_properties(self, params):
        mat_id = params["material_id"]
        try:
            mat = self.parser.get_material_properties(mat_id)
            return f"Material {mat_id}: E={mat.E}, nu={mat.nu}"
        except KeyError:
            return f"Material {mat_id} not found"

    def query(self, question):
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613",
                                                messages=[{
                                                    "role": "user",
                                                    "content": question
                                                }],
                                                functions=functions,
                                                function_call="auto")

        if not (func_call := response.choices[0].message.get("function_call")):
            return "Unable to process this query"

        func_name = func_call["name"]
        params = eval(func_call["arguments"])

        if handler := self.functions.get(func_name):
            return handler(params)
        return "Function not implemented"
