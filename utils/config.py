# utils/config_driver.py

import yaml
from pathlib import Path


class ConfigUtil:

    def __init__(self, filename='config.yaml'):
        self.config_path = Path(__file__).parent.parent / filename
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)

    def get_config(self):
        return self.config


# 用于在当前utils目录下测试ConfigUtil类是否正确读取配置
if __name__ == "__main__":
    config_util = ConfigUtil()
    print(config_util.get_config())
