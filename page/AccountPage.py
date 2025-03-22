from selenium.webdriver.common.by import By

from base.AccountBase import AccountBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path
class AccountPage(ObjectMap, AccountBase):
    def upload_avatar(self, driver, img_name):
        '''
        头像更换
        :param driver:
        :param img_name:
        :return:
        '''
        # 选择图片路径
        img_xpath = get_img_path(img_name)
        avatar_xpath = self.basic_avatar_input()
        # 点击头像
        ObjectMap().element_click(driver, By.XPATH, avatar_xpath)
        # 上传头像
        return self.upload(driver, By.XPATH, avatar_xpath, img_xpath)

    def click_save(self, driver):
        '''
        个人头像-点击保存
        :param driver:
        :return:
        '''
        save_button_xpath = self.basic_info_save_button()
        # 点击保存
        return self.element_click(driver, By.XPATH, save_button_xpath)

    