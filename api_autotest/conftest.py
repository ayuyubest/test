import pytest
import pandas as pd
from typing import Dict, Any
from core.api_client import ApiClient

@pytest.fixture(scope="session")
def api_client():
    return ApiClient()

@pytest.fixture(scope="session")
def test_data() -> pd.DataFrame:
    return pd.read_csv("data/test_cases_fixed.csv")

@pytest.fixture
def auth_cookies(api_client):
    """获取认证Cookie的fixture"""
    # 使用提供的Cookie信息
    cookies = {
        "_ati": "6809640610819",
        "_xhcsid": "hjytest41", 
        "_xhcud": "1573",
        "X-HC-TOKEN": "_ati=6809640610819; _xhcsid=hjytest41; _xhcud=1573; X-HC-TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJzcyI6InBvVURjbk9qSTBMdSIsImlzcyI6ImxvZ2luIiwidW4iOiJhZG1pbiIsImV4cCI6MTc2NzA5MjUzMiwiaWF0IjoxNzY3MDg1MzMyLCJzaWQiOiJoanl0ZXN0NDEiLCJ1ZCI6MTU3M30.AajSobEDQ3CgC25rnVFHiEvYcIXmBtcWJanE99YAI1r9K9lcRjoJHZJy5fe9SNmrss9s4qFeEL2K0mXLS_qTxBG8APuj4Mr0lhBdUzWilDnpIgs8IFQkLyWC4H0z8d9q9zeaUzgtO8Wv1Q51t9vTip_nohyWZedFe1Vcgf_Kup3Psyb-",
        "version": "v1"
    }
    return cookies

@pytest.fixture  
def auth_token(auth_cookies):
    """为了兼容现有代码，保留auth_token fixture"""
    # 返回X-HC-TOKEN的值，用于需要token的地方
    return auth_cookies.get("X-HC-TOKEN")