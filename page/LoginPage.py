from selenium.webdriver.common.by import By

from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf
class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        '''
        登录页输入值
        :param driver: 驱动
        :param input_placeholder:
        :param input_value:
        :return:
        '''
        # 用户名密码输入框的定位
        input_xpath = self.login_input(input_placeholder)
        # driver.find_element(By.XPATH, input_xpath).clear()
        # return driver.find_element(By.XPATH, input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def login_click_button(self, driver, button_name):

        # 登录按钮得定位
        button_xpath = self.login_button(button_name)
        # return driver.find_element(By.XPATH, button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user):
        '''
        登录
        :param driver:
        :param url:
        :return:
        '''
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_user_pass(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.login_click_button(driver, '登录')

    def login_assert(self, driver, img_name):
        '''
        登录后判断头像
        :param driver:
        :param img_name:
        :return:
        '''
        return self.find_img_in_source(driver, img_name)