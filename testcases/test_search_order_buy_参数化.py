import time

import pytest

from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.OrderPage import OrderPage
from page.LoginPage import LoginPage

tab_list = ['全部', '待付款', '待发货', '运输中', '待确认', '待评价']

# 使用 参数化， 以上，如果点击待付款失败，还会执行下一个 待发货。。。， 相当于解耦，比原代码方便执行维护
class TestOrderBuy:
    @pytest.mark.parametrize('tab', tab_list)
    def test_order_buy(self, driver, tab):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        time.sleep(2)
        # 点击我的订单，已卖出的宝贝
        LeftMenuPage().click_level_one_menu(driver, '我的订单')
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, '已买到的宝贝')
        time.sleep(2)
        # # 点击
        # tab_list = ['全部', '待付款', '待发货', '运输中', '待确认', '待评价']
        # for i in tab_list:
        #     OrderPage().click_order_tab(driver, i)
        #     time.sleep(2)

        OrderPage().click_order_tab(driver, tab)

        driver.quit()
