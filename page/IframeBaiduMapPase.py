from selenium.webdriver.common.by import By

from base.IframeBaiduMapBase import IframeBaiduMapBase
from base.ObjectMap import ObjectMap

class IframeBaiduMapPase(IframeBaiduMapBase,ObjectMap):
    def get_baidu_search_button(self, driver):
        '''
        百度地图搜索按钮
        :param driver:
        :return:
        '''
        search_button_id = self.search_button()
        return self.element_click(driver, By.XPATH, search_button_id)

    def switch_2_baidu_map_iframe(self, driver):
        """
        切换到百度地图iframe
        :param driver:
        :return:
        """
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        """
        从百度地图iframe切回校园二手系统
        :param driver:
        :return:
        """
        return self.switch_from_iframe_to_content(driver)

    def send_baidu_search(self, driver, search_value):
        '''
        搜索内容
        :param driver:
        :param search_value:
        :return:
        '''
        input_baidu_id = self.input_baidu()
        return self.element_fill_value(driver, By.XPATH, input_baidu_id, search_value)