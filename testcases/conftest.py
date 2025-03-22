import pytest

from config.driver_config import DriverConfig


@pytest.fixture
def driver():
    driver = DriverConfig().driver_config()
    # 使用 yield 生成器
    yield driver
    driver.quit()