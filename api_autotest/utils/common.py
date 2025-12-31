import json
from typing import Any, Dict, Union

def safe_json_loads(data: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
    """安全地解析JSON数据"""
    if isinstance(data, str):
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return {}
    elif isinstance(data, dict):
        return data
    else:
        return {}

def format_test_name(test_case_name: str) -> str:
    """格式化测试用例名称"""
    return test_case_name.replace(" ", "_").replace("-", "_")