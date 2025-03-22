from time import sleep

import pytest

from config.driver_config import DriverConfig

class TestPyTestM:
    @pytest.mark.baidu
    def test_open_baidu(self):
        driver = DriverConfig().driver_config()
        driver.get('https://www.baidu.com')
        sleep(3)
        driver.quit()
    # 标记执行的测试用例
    # 一个用例有多个标记时使用and连接
    @pytest.mark.bing
    @pytest.mark.open_bing
    def test_open_bing(self):
        driver = DriverConfig().driver_config()
        driver.get('https://cn.bing.com')
        sleep(3)
        driver.quit()

    @pytest.mark.open_bing
    def test_open_bing(self):
        driver = DriverConfig().driver_config()
        driver.get('https://cn.bing.com')
        sleep(3)
        driver.quit()


    @pytest.mark.taobao
    def test_open_bing(self):
        driver = DriverConfig().driver_config()
        driver.get('https://www.taobao.com/')
        # 提示信息，如果需要输出显示，执行时需要带上 -s
        print("打印的是淘宝")
        sleep(3)
        driver.quit()
'''
终端执行
          
          【使用 :: 拼接】 :  pytest testcases/test_pytest_m.py::TestPyTestM::test_open_bing
          【使用m标记】 pytest -m bing 
                          执行两个使用or连接:  pytest -m "baidu or bing"  
                          一个用例有多个标记时使用and连接:  pytest -m "bing and open_bing"  
                          不执行baidu标记的用例：  pytest -m "not baidu"  
                          执行baidu,不执行taobao,忽略bing: pytest .\ test_pytest_m.py -m "baidu and not taobao"  
               
'''
