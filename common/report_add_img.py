import time
import allure

def add_img_2_report(driver, step_name, need_sleep=True):
    '''
    截图并插入 allure 报告
    :param driver:
    :param step_name: 图片名
    :param need_sleep: 休息
    :return:
    '''
    try:
        if need_sleep:
            time.sleep(2)
        allure.attach(
            # 截图
            driver.get_screenshot_as_png(),
            step_name + '.png',  # 修正文件名
            allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"截图添加到报告失败: {e}")
