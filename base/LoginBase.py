
class LoginBase:
    def login_input(self, input_placeholder):
        '''
        登录用户名，密码输入框
        :param input_placeholder:
        :return:
        '''
        return "//input[@placeholder='"+input_placeholder+"']"

    def login_button(self, button_name):
        '''
        登录按钮
        :param button_name:
        :return:
        '''
        # //button[contains(text(),"登录")   '//button[contains(text(),"登录")]'
        # //span[contains(text(),'登录')]
        return "//span[contains(text(),'"+button_name+"')]"
if __name__ == '__main__':
    print(LoginBase().login_input("登录账号"))
    print(LoginBase().login_button("登录"))