import time

import pytest

from common.tools import driver_get_screenshot
class TestBaiDu:
    pytest.fixture()
    def test_baidu(self, driver):
        driver.get('https://www.baidu.com')
        time.sleep(1)
        driver_get_screenshot(driver=driver, image_name='百度-')
        # print(screenshot)
        time.sleep(3)