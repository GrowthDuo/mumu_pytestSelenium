# 左侧菜单栏的封装

class LeftMenuBase:
    def level_one_menu(self, menu_name):
        '''
        一级菜单栏定位
        :param menu_name:
        :return:
        '''
        # //aside[@class='el-aside']//span[text()='首页']/ancestor::li
        # return "//aside[@class='el-aside']//span[text()='"+menu_name+"']/.."
        return "//aside[@class='el-aside']//span[text()='"+menu_name+"']/ancestor::li"

    def level_two_menu(self, menu_name):
        '''
        二级菜单定位
        :param menu_name:
        :return:
        '''
#       //aside[@class='el-aside']//span[text()='新增二手商品']/..
        return "//aside[@class='el-aside']//span[text()='"+menu_name+"']/parent::li"


if __name__ == '__main__':
    print(LeftMenuBase().level_one_menu("首页"))
    print(LeftMenuBase().level_one_menu("交易市场"))