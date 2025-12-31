import os
import yaml
from typing import Dict, Any

class Config:
    _instance = None
    _config_data: Dict[str, Any] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._config_data:
            self.load_config()

    def load_config(self):
        config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        with open(config_path, 'r', encoding='utf-8') as f:
            self._config_data = yaml.safe_load(f)

    @property
    def base_url(self) -> str:
        env = os.getenv('TEST_ENV', 'test')
        return self._config_data['env'][env]['base_url']

    @property
    def headers(self) -> Dict[str, str]:
        return self._config_data['headers']

    @property
    def timeout(self) -> int:
        env = os.getenv('TEST_ENV', 'test')
        return self._config_data['env'][env]['timeout']