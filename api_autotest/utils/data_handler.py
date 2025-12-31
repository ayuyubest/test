import pandas as pd
from typing import List, Dict, Any

class DataHandler:
    @staticmethod
    def load_test_cases(csv_path: str) -> pd.DataFrame:
        """加载测试用例数据"""
        return pd.read_csv(csv_path)

    @staticmethod
    def group_by_module(test_cases: pd.DataFrame) -> Dict[str, List[Dict[str, Any]]]:
        """按模块分组测试用例"""
        # 根据tags字段的第一个标签进行分组
        test_cases['module'] = test_cases['tags'].str.split(',').str[0]
        return {
            name: group.to_dict("records")
            for name, group in test_cases.groupby("module")
        }