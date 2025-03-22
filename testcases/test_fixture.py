from time import sleep

import pytest

from config.driver_config import DriverConfig

class TestFixtrue:
    @pytest.fixture(scope='class')
    def test_class(self):
        print('我是class级别的，只执行一次')

    @pytest.fixture(scope='function')
    def driver(self):
        driver = DriverConfig().driver_config()
        return driver


    def test(self, driver, test_class):
        driver.implicitly_wait(5)
        driver.get('http:www.baidu.com')
        sleep(3)

    @pytest.mark.open_bing
    def test_open_bing(self, driver, test_class):
        # driver = DriverConfig().driver_config()
        driver.get('https://cn.bing.com')
        sleep(3)
        driver.quit()

