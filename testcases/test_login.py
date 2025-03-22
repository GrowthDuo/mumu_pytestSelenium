from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage

class TestLogin:
    def test_login(self, driver):
        # 如果取消这行注释，需要将上面的参数driver【conftest】删除 driver = DriverConfig().driver_config()

        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        sleep(3)
        # driver.get('http://120.78.226.139/login')
        # sleep(3)
        # LoginPage().login_input_value(driver, "用户名", "william")
        # sleep(2)
        # LoginPage().login_input_value(driver, "密码", "123456")
        # sleep(2)
        # LoginPage().login_click_button(driver, "登录")
        # sleep(2)
        driver.quit()