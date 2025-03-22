from time import sleep

import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage

goods_info_list = [
    {
        "goods_title": "新增商品测试1",
        "goods_details": "新增商品测试详情1",
        "goods_num": 1,
        "goods_pic_list": ["po.png"],
        "goods_price": 100,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    },
    {
        "goods_title": "新增商品测试2",
        "goods_details": "新增商品测试详情2",
        "goods_num": 2,
        "goods_pic_list": ["po2.jpg"],
        "goods_price": 200,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    }
]


class TestAddGoods:
    @pytest.mark.parametrize('goods_info_list_date', goods_info_list)
    def test_add_goods_001(self, driver, goods_info_list_date):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, '产品')
        sleep(2)
        LeftMenuPage().click_level_two_menu(driver, '新增二手商品')
        sleep(2)

        GoodsPage().add_new_goods(driver=driver,
                                  goods_title=goods_info_list_date['goods_title'],
                                  goods_details=goods_info_list_date['goods_details'],
                                  goods_num=goods_info_list_date['goods_num'],
                                  goods_pic_list=goods_info_list_date['goods_pic_list'],
                                  goods_price=goods_info_list_date['goods_price'],
                                  goods_status=goods_info_list_date['goods_status'],
                                  bottom_button_name=goods_info_list_date['bottom_button_name']
                                  )
        sleep(3)
