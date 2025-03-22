from time import sleep

import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


# 使用fixture实战- 新增二手商品
# pytest的精髓二：conftest的使用

# 新建一个conftest.py文件，测试文件会自动调用conftest.py的代码。就近原则
class TestAddGoods:

    def test_add_goods_001(self, driver):
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, '产品')
        sleep(2)
        LeftMenuPage().click_level_two_menu(driver, '新增二手商品')
        sleep(2)
        GoodsPage().add_new_goods(
            driver,
            '新增商品测试',
            '新增商品测试详情',
            1,
            ['po.png'],
            123,
            '上架',
            '提交'
        )
        sleep(3)
        # driver.quit()
