
class IframeBaiduMapBase:
    def input_baidu(self):
        return "//input[@id='sole-input']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"

    def search_button(self):
      '''
      搜索按钮
      :return:
      '''
      # // input[ @ id = 'sole-input']
      return "//button[@id ='search-button']"