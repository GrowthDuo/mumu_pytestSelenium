import time

import allure

from page.ExternalLinkPage import ExternalLinkPage
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from common.report_add_img import add_img_2_report
class TestWindowHandle(ExternalLinkPage):

    @allure.description('窗口句柄')
    @allure.epic('窗口句柄epic')
    @allure.feature('窗口句柄feature')
    @allure.story('窗口句柄story')
    @allure.tag('窗口句柄tag')
    def test_switch_window_handle(self, driver):
        # 浏览器驱动
        # driver = DriverConfig().driver_config()

        with allure.step('登录'):
            # 登录
            LoginPage().login(driver, 'jay')
            time.sleep(2)
            # 截图
            add_img_2_report(driver, '登录')

        with allure.step('点击外链'):
            # 点击外链
            LeftMenuPage().click_level_one_menu(driver, '外链')
            time.sleep(1)
            # 截图
            add_img_2_report(driver, '外链')


        with allure.step('断言title'):
            # 窗口切换 -》切换后可以操作页面的元素
            title = ExternalLinkPage().goto_imooc(driver)
            # 看一下标题
            print(title)
            time.sleep(1)
            assert title == '慕课网-程序员的梦工厂'
