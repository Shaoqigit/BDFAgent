from agent_Lc import agent_executor

test_cases = [{
    "query": "找出所有厚度超过3mm的四边形单元",
    "expected_tool": "FiniteElement_Query",
    "expected_params": {
        "element_type": "CQUAD4",
        "list_properties": True
    }
}, {
    "query": "统计模型中使用的材料种类数量",
    "expected_tool": "Material_Summary",
    "expected_params": {}
}]


def validate_tool_selection():
    for case in test_cases:
        response = agent_executor.invoke(case["query"])
        assert response.tool == case["expected_tool"]
        assert response.params == case["expected_params"]
