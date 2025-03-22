from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from common.tools import get_project_path, file_sep

# def test_driver_config():
#     web_driver = webdriver.Chrome()
#     web_driver.maximize_window()
#     # web_driver.get('https://doc.pescms.com/?g=Doc&m=Login&a=index')
#     # 隐形等待时间
#     web_driver.implicitly_wait(5)
#     # 删除所有的cookis
#     web_driver.delete_all_cookies()
#     return web_driver

class DriverConfig:
    def driver_config(self):
        """
        浏览器驱动
        :return:
        """
        driver_path = get_project_path() + file_sep(["driver_files", "chromedriver.exe"], add_sep_before=True)
        options = webdriver.ChromeOptions()
        # 设置窗口大小，设置为1920*1080
        options.add_argument("window-size=1920,1080")
        # 去除chrome正受到自动测试软件的控制的提示
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 去除chrome正受到自动测试软件的控制的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        # 解决selenium没法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式，一般使用无痕跑
        # options.add_argument("--incognito")
        # 设置为无头模式
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        # 原代码

        # 使用原始字符串表示路径
        # driver = webdriver.Chrome(
        #     executable_path=driver_path, options= options)

        # 修改后的代码
        # 这样修改后，就不会再出现executable_path已被弃用的警告了。
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        # 删除所有cookies
        driver.delete_all_cookies()

        return driver

        # driver.get("https://www.baidu.com")
        # time.sleep(3)
        # driver.quit()







