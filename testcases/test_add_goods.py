from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


class TestAddGoods:
    # def test_add_goods_001(self):
    #     driver = DriverConfig().driver_config()
    #     LoginPage().login(driver, 'jay')
    #     LeftMenuPage().click_level_one_menu(driver, '产品')
    #     sleep(2)
    #     LeftMenuPage().click_level_two_menu(driver, '新增二手商品')
    #     sleep(2)
    #     GoodsPage().add_new_goods(driver, '新增商品测试', '新增商品测试详情', 1, ['po.png'], 123, '上架', '提交')
    #     sleep(3)
    # driver.quit()

    def test_add_goods_001(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, '产品')
        sleep(2)
        LeftMenuPage().click_level_two_menu(driver, '新增二手商品')
        sleep(2)

        GoodsPage().add_new_goods(driver=driver,
                                  goods_title='新增商品测试',
                                  goods_details='新增商品测试详情',
                                  goods_num=1,
                                  goods_pic_list=['po.png'],
                                  goods_price=123,
                                  goods_status='上架',
                                  bottom_button_name='提交'
                                  )
        sleep(3)
