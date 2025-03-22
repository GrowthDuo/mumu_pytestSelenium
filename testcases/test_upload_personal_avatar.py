from time import sleep

from page.LoginPage import LoginPage
from page.AccountPage import AccountPage
from page.LeftMenuPage import LeftMenuPage
from config.driver_config import DriverConfig

class TestUploadPersonalAvatar:
    def test_upload_personal_avatar(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, '账户设置')
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, '个人资料')
        sleep(2)
        AccountPage().upload_avatar(driver, 'search.jpg')
        sleep(2)
        AccountPage().click_save(driver)
        sleep(30)
        driver.quit()

