import datetime
import os
import time
from typing import Optional

# 获取时间戳
def get_now_time():
    return datetime.datetime.now()

# 获取项目目录
def get_project_path():
    # 项目名称
    pro_name = "mumu_pytestSelenium"
    abspath = os.path.dirname(__file__)
    # print(abspath)
    # 打印获取项目名称的下标
    # print(abspath.index(pro_name))
    #  获取项目名称的下标
    pro_index = abspath.index(pro_name)
    # print(abspath[ :pro_index + len(pro_name)] )
    return abspath[ :pro_index + len(pro_name)]

# 拼接文件路径
def file_sep(path, add_sep_before =False, end_add_sep_before = False):
    '''
    拼接文件路径/获取项目目录
    :param path: 要拼接的路径使用列表的方式
    :param add_sep_before: 当为True时，路径前加/
    :param end_add_sep_before:当为True时，路径后加/
    :return:
    '''
    all_path = os.sep.join(path)
    # print(all_path)
    if add_sep_before == True:
        all_path = os.sep+all_path
    if end_add_sep_before:
        all_path = all_path+os.sep
    # print(all_path)
    return all_path

def get_img_path(img_name):
    '''
    获取商品图片的路径
    :param img_name:
    :return:
    '''
    img_dir_path = get_project_path() + file_sep(['img', img_name], add_sep_before = True)
    return img_dir_path

# 自定义截图
# 自定义截图
def driver_get_screenshot(driver, image_name=None, suffix=False, time_sleep=False, return_path=False) -> Optional[str]:
    '''
    自定义截图
    :param driver: 浏览器驱动实例
    :param image_name: 截图名
    :param suffix: 后缀，True 为 .PNG，False 为 .jpg
    :param time_sleep: 是否等待 2 秒后截图
    :param return_path: 是否返回截图保存路径
    :return: 截图保存路径（如果 return_path 为 True），否则返回 None
    '''
    # 保存目录
    file_path = get_project_path() + file_sep(['img', 'screenshot_img'], add_sep_before=True, end_add_sep_before=True)
    # 确保保存目录存在
    os.makedirs(file_path, exist_ok=True)

    # 获取当前时间
    time_t = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

    # 生成文件名
    if image_name is not None:
        if suffix:
            tu_f = time_t + '.PNG'
            fileName = file_sep([image_name, tu_f], add_sep_before=True)
        else:
            fileName = image_name + time_t + '.jpg'
    else:
        if suffix:
            fileName = time_t + '.PNG'
        else:
            fileName = time_t + '.jpg'

    # 拼接路径与图片
    path = os.path.join(file_path, fileName)

    try:
        if time_sleep:
            time.sleep(2)
        # 开始截屏，保存到指定目录
        driver.get_screenshot_as_file(path)
        print(f"截图已保存至: {path}")
        if return_path:
            return path
        return None
    except Exception as e:
        print(f"截图保存失败: {e}")
        return None

'''
优化点说明：
添加 return_path 参数：通过该参数控制是否返回截图保存的路径，默认不返回。
路径拼接优化：使用 os.path.join 来拼接文件路径，避免不同操作系统下路径分隔符的问题。
目录创建：使用 os.makedirs 确保保存截图的目录存在，如果目录不存在会自动创建。
错误处理：添加了 try-except 块来捕获截图保存过程中可能出现的异常，并打印错误信息。
类型提示：为函数的参数和返回值添加了类型提示，提高代码的可读性和可维护性。
代码简化：将 if suffix == True 简化为 if suffix，符合 Python 的简洁风格。
'''

# def driver_get_screenshot(driver, image_name=None, suffix=False, time_sleep=False):
#     '''
#     自定义截图
#     :param driver:
#     :param file_path: 文件目录
#     :param image_name: 截图名
#     :param suffix: 后缀
#     :return:
#     '''
#     # 保存目录
#     # if file_path == None:
#     file_path = get_project_path() + file_sep(['img', 'screenshot_img'], add_sep_before=True, end_add_sep_before= True)
#     # print(file_path)
#     # else:
#     #     file_path = get_project_path() + file_sep([file_path], add_sep_before=True)
#
#
#     # 获取当前时间
#     time_t = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
#     if image_name is not None:
#         if suffix == True:
#             tu_f = time_t + '.PNG'
#             fileName = file_sep([image_name, tu_f], add_sep_before=True)
#         else:
#             fileName = image_name + time_t + '.jpg'
#     else:
#         if suffix == True:
#             fileName = time_t + '.PNG'
#         else:
#             fileName = time_t + '.jpg'
#     # 拼接路径与图片
#     path = file_path + file_sep([fileName])
#     print(path)
#     # return path
#     if time_sleep == True:
#         time.sleep(2)
#         driver.get_screenshot_as_file(path)
#
#     # # 开始截屏，保存当前目录下
#     driver.get_screenshot_as_file(path)
#     return path


if __name__ == '__main__':
    print(get_now_time())
    print(get_project_path())
    file_sep(["config", "enviroment.yaml"], add_sepbefore=True, end_add_sep_before=True)
    print(file_sep(['ccc'], add_sep_before=True, end_add_sep_before=True))
    print(get_img_path('po.png'))
    print(get_img_path('po2.jpg'))
    print('---------')
    # print(driver_get_screenshot(image_name='hhh', suffix=True))
    # print(driver_get_screenshot())