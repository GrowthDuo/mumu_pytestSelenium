class AccountBase:
    def basic_avatar_input(self):
        '''
        基本信息-个人头像
        :return:
        '''
        return "//div[@class='avatar-uploader']//div[@class='el-upload el-upload--text']"

    def basic_info_save_button(self):
        '''
        基本信息-保存按钮
        :return:
        '''
        return "//span[contains(text(), '保存')]/parent::button"