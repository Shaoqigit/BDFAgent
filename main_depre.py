from agent_depre import BDFAgent

if __name__ == "__main__":
    agent = BDFAgent("your_model.bdf")

    print(agent.query("How many nodes are there?"))
    # Output: Total nodes: 2450

    print(agent.query("Show me all CQUAD4 elements"))
    # Output: Found 120 CQUAD4 elements

    print(agent.query("What are the properties of material 1?"))
    # Output: Material 1: E=210000.0, nu=0.3
