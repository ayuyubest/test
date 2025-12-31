import pytest
import pandas as pd
from utils.data_handler import DataHandler

@pytest.fixture(scope="module")
def tax_declare_test_data():
    """税务申报相关测试数据"""
    df = DataHandler.load_test_cases("data/test_cases.csv")
    return df[df['tags'].str.contains('tax_declare')].to_dict("records")

@pytest.fixture(scope="module")
def expense_config_test_data():
    """费用项配置相关测试数据"""
    df = DataHandler.load_test_cases("data/test_cases.csv")
    return df[df['tags'].str.contains('expense_config')].to_dict("records")

@pytest.fixture(scope="module")
def predict_config_test_data():
    """预测配置相关测试数据"""
    df = DataHandler.load_test_cases("data/test_cases.csv")
    return df[df['tags'].str.contains('predict_config')].to_dict("records")