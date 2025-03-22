from time import sleep

from page.LoginPage import LoginPage
class TestLoginImgAssert:
    def test_login_img_assert(self, driver):
        '''
        登录后断言图片
        :param driver:
        :return:
        '''
        LoginPage().login(driver, 'jay')
        sleep(3)
        print(LoginPage().login_assert(driver, 'po3.jpg'))
        assert LoginPage().login_assert(driver, 'po3.jpg')>0.7


