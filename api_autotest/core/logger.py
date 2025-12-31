import logging
import os
from config.config import Config

def setup_logger():
    config = Config()
    log_config = config._config_data['logging']
    
    # 创建logs目录
    log_dir = os.path.dirname(log_config['file'])
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 配置日志
    logging.basicConfig(
        level=getattr(logging, log_config['level']),
        format=log_config['format'],
        handlers=[
            logging.FileHandler(log_config['file'], encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

logger = setup_logger()