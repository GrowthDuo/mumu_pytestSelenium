'''
定位上一级
 1、 parent::div  2、 使用/..
//span[contains(text(),'欢迎您回来')]/parent::div
//span[contains(text(),'欢迎您回来')]/..

使用class属性，  使用文字定位  contains：包含
    //div[@class="logo"]  和 //div[contains(text(),'二手')]

 # following-sibling ：定位同级别元素的下一位
        return "//div[contains(text(),'我的日历')]/following-sibling::div"

定位同一级别 preceding-sibling
//span[contains(text(),'欢迎您回来')]/parent::div/preceding-sibling::div

# ancestor ：寻找（单）多级的父级元素定位
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"
'''
class HomeBase:
    def wallet_switch(self):
        '''
        首页钱包开关
        :return:
        '''
        return '//span[@class="el-switch__core"]'

    def log(self):
        '''
        进入首页后，首页左上角的log
        :return:
        '''
        # 两种方法定位，class和文本  contains：包含
        # //div[@class="logo"]  和 //div[contains(text(),'二手')]
        return "//div[@class='logo']"

    def welcome(self):
        '''
        首页的 欢迎您回来
        :return:
        '''
        return "//span[contains(text(),'欢迎您回来')]"

    def show_date(self):
        '''
        首页显示日期
        :return:
        '''
        # following-sibling ：定位同级别元素的下一位
        return "//div[contains(text(),'我的日历')]/following-sibling::div"

    def home_user_avator(self):
        '''
        首页用户头像图片
        :return:
        '''
        return "//span[contains(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img"

    def home_user_avatar_2(self):
        """
        首页用户头像大图2
        :return:
        """
        # ancestor ：寻找多级的父级元素定位
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"