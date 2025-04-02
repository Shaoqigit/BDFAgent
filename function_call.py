import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

functions = [{
    "name": "get_node_count",
    "description": "Get total number of nodes in the model",
    "parameters": {
        "type": "object",
        "properties": {}
    }
}, {
    "name": "get_elements_by_type",
    "description": "Get elements of specified type",
    "parameters": {
        "type": "object",
        "properties": {
            "element_type": {
                "type": "string",
                "enum": ["CQUAD4", "CTRIA3", "CHEXA", "CBAR", "CBEAM"],
                "description": "Element type to filter"
            }
        },
        "required": ["element_type"]
    }
}, {
    "name": "get_material_properties",
    "description": "Get material properties by ID",
    "parameters": {
        "type": "object",
        "properties": {
            "material_id": {
                "type": "integer",
                "description": "Material ID"
            }
        },
        "required": ["material_id"]
    }
}]
