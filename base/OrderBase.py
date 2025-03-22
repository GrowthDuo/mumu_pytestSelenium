
class OrderBase:
    def order_tab(self, tab_name):
        '''
        订单tab按钮
        :param tab_name: 全部，待付款，待发货，运输中，待确认，待评价
        :return:
        '''
        return "//div[@class='el-tabs__nav-scroll']//div[contains(text(),'"+tab_name+"')]"

if __name__ == '__main__':
    print(OrderBase().order_tab('全部'))