import requests
from typing import Dict, Any, Optional
from core.logger import logger
from config.config import Config

class ApiClient:
    def __init__(self):
        self.config = Config()
        self.session = requests.Session()
        self.session.headers.update(self.config.headers)

    def request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> requests.Response:
        """发送HTTP请求"""
        full_url = f"{self.config.base_url}{url}"
        merged_headers = {**self.session.headers, **(headers or {})}

        logger.info(f"Sending {method} request to {full_url}")
        logger.debug(f"Headers: {merged_headers}")
        logger.debug(f"Data: {data}")
        if cookies:
            logger.debug(f"Cookies: {cookies}")

        response = self.session.request(
            method=method,
            url=full_url,
            headers=merged_headers,
            json=data,
            cookies=cookies,
            timeout=self.config.timeout,
            **kwargs
        )

        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")

        return response