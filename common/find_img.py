import aircv as ac

from common.tools import get_img_path
class FindImg:
    def img_imread(self, img_path):
        '''
        读取图片
        :param img_path:
        :return:
        '''
        return ac.imread(img_path)

    def get_confidence(self, source_path, search_path):
        """
        查找图片
        :param source_path: 原图路径
        :param search_path: 需要查找的图片的路径
        :return:
        """
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        result = ac.find_template(img_src, img_sch)
        print(result)
        # print(result["confidence"])
        return result["confidence"]


if __name__ == '__main__':
    # source_path = get_img_path('source.png')
    source_path = 'D:\\Software\\python\\test\\mumu_pytestSelenium\\img\\source_img\\po3.png'
    # search_path = get_img_path('search.jpg')
    search_path = 'D:\\Software\\python\\test\\mumu_pytestSelenium\\img\\assert_img\\po3.jpg'

    # print(source_path)
    FindImg().get_confidence(source_path, search_path)
