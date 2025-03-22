import time

from selenium.webdriver.common.by import By

from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.IframeBaiduMapPase import IframeBaiduMapPase


class TestIframeBaiduMap:
    # def test_iframe_baidu_map(self):
    #     driver = DriverConfig().driver_config()
    #     LoginPage().login(driver, 'jay')
    #     time.sleep(2)
    #     # 点击iframe测试
    #     LeftMenuPage().click_level_one_menu(driver, 'iframe测试')
    #     time.sleep(2)
    #     # 切换到百度地图
    #     IframeBaiduMapPase().switch_2_baidu_map_iframe(driver)
    #
    #     # 点击搜索按钮
    #     IframeBaiduMapPase().get_baidu_search_button(driver)
    #     time.sleep(3)
    #     IframeBaiduMapPase().send_baidu_search(driver, '天津')
    #     time.sleep(5)
    #     # 切回首页
    #     IframeBaiduMapPase().iframe_out(driver)
    #     LeftMenuPage().click_level_one_menu(driver, '首页')
    #     time.sleep(3)
    #     driver.quit()

    def test_iframe_baidu_map(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        time.sleep(2)
        # 点击iframe测试
        LeftMenuPage().click_level_one_menu(driver, 'iframe测试')
        time.sleep(2)
        # 切换到百度地图
        IframeBaiduMapPase().switch_2_baidu_map_iframe(driver)

        # 点击搜索按钮
        IframeBaiduMapPase().get_baidu_search_button(driver)
        time.sleep(3)
        IframeBaiduMapPase().send_baidu_search(driver, '天津')
        time.sleep(5)
        # 切回首页
        IframeBaiduMapPase().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver, '首页')
        time.sleep(3)
        driver.quit()
