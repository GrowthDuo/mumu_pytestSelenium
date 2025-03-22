import time
# ElementNotVisibleException 是 Selenium 库中定义的异常类，用于在元素定位失败时抛出特定的异常信息。
# WebDriverException 是一个通用的 WebDriver 异常类，用于处理与浏览器驱动相关的各种异常
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from common.yaml_config import GetConf
from common.tools import file_sep, get_project_path
from common.find_img import FindImg
from config.driver_config import DriverConfig


# class ObjectMap:
#     # 获取基本地址
#     URL = GetConf().get_url()
#
#     # 以下方法 ：提供一个灵活的元素查找机制，允许设置超时时间和元素是否必须可见的条件，
#     # 确保在元素加载缓慢或需要特定可见状态时，能够正确定位到目标元素。
#
#     # 获取元素的封装：如何使用selenium获取元素
#     def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
#         # todo 查找元素
#         '''
#         单个元素获取
#         :param driver:浏览器驱动
#         :param locate_type: 定位方式类型
#         :param locator_expression: 定位表达式
#         :param timeout: 默认寻找超时时间是10秒
#         :param must_be_visible: 元素是否必须可见，True是必须可见，False是默认值
#         :return: 返回的元素
#         '''
#         # start_time：记录开始查找元素的时间，单位为毫秒。
#         start_time = time.time() * 1000
#         # print(start_time)
#         # stop_time：计算出查找元素的截止时间，同样以毫秒为单位。
#         stop_time = start_time + (timeout * 1000)
#         # print(stop_time)
#
#         # 循环查找元素
#         # 循环查找元素，循环次数为超时时间乘以 10，因为每次循环间隔 0.1 秒
#         for x in range(int(timeout*10)):
#             try:
#                 # 使用指定的定位方式和定位表达式查找元素
#                 element = driver.find_element(by=locate_type, value=locator_expression)
#                 # 如果元素不是必须可见的，就直接返回元素
#                 '''
#                 如果 must_be_visible 为 True，
#                 则需要进一步判断元素是否可见（通过 element.is_displayed() 方法），
#                 如果可见则返回元素，否则抛出异常。
#                 '''
#                 # if true :
#                 if not must_be_visible:
#                     # 如果元素不是必须可见的，直接返回找到的元素
#                     return element
#                 # 如果元素是必须可见的，则需要先判断元素是否可见
#                 else:
#                     # 如果元素必须可见，判断元素是否显示在页面上
#                     if element.is_displayed():
#                         # 若元素可见，返回该元素
#                         return element
#                     else:
#                         # 若元素不可见，抛出异常以继续尝试查找
#                         raise Exception()
#             except Exception:
#                 # 获取当前时间，将其转换为毫秒
#                 now_ms = time.time() * 1000
#                 # 检查当前时间是否超过了截止时间
#                 if now_ms >= stop_time:
#                     break
#                 # 若未超过截止时间，忽略本次异常，继续下一次查找尝试
#                 pass
#             # 每次查找尝试后暂停 0.1 秒，避免过于频繁查找
#             time.sleep(0.1)
#         # 如果在超时时间内未找到符合条件的元素，抛出元素不可见异常，并给出详细错误信息
#         raise ElementNotVisibleException("元素定位失败，定位方式："+ locate_type + "定位元素：" + locator_expression)
#
#
#     # 等待页面完全加载完成的封装：页面什么时候才算加载完成？
#     def wait_for_ready_state_complete(self, driver, timeout =30):
#         '''
#         等待页面完全加载完成
#         :param driver: 浏览器驱动
#         :param timeout: 超时时间
#         :return:
#         '''
#         # 记录开始等待页面加载的时间，将当前时间（以秒为单位）转换为毫秒
#         start_time = time.time()*1000
#         stop_time = start_time + (timeout * 1000)
#
#         # 进行循环检查页面加载状态，循环次数为 timeout * 10，因为每次循环间隔 0.1 秒
#         for x in range(int(timeout*10)):
#
#             # 尝试获取页面的加载状态
#             try:
#                 # 通过执行 JavaScript 代码获取页面的 readyState 属性
#                 # document.readyState 有三种可能的值："loading"（页面正在加载）、"interactive"（页面已经解析完成，但资源仍在加载）、"complete"（页面和所有资源都已加载完成）
#
#                 ready_state = driver.execute_script("return document.readyState")
#             except WebDriverException:
#                 # 如果在执行 JavaScript 代码时出现 WebDriver 相关的异常，例如驱动与浏览器通信问题等
#                 # 则等待 0.03 秒后直接返回 True，认为页面加载完成（这里逻辑可能需要根据实际情况调整）
#
#                 # 如果有driver的错误，执行js失败，就直接跳过
#                 time.sleep(0.03)
#                 return True
#
#             # 判断页面的加载状态是否为 "complete"，即页面和所有资源都已加载完成
#             if ready_state == "complete":
#                 # 如果页面加载完成，再等待 0.01 秒，可能是为了确保页面完全稳定
#                 time.sleep(0.01)
#                 # 返回 True 表示页面加载完成
#                 return True
#             else:
#                 # 如果页面还未加载完成，获取当前时间并转换为毫秒
#                 now_ms = time.time()*1000
#                 # 检查当前时间是否超过了设定的截止时间
#                 if now_ms >=stop_time:
#                     # 如果超过截止时间，跳出循环
#                     break
#                 # 如果未超过截止时间，等待 0.1 秒后再次进行检查
#                 time.sleep(0.1)
#         # 如果在超时时间内页面仍未加载完成，抛出异常并提示具体的超时时间
#         raise Exception("打开网页时页面元素在%s秒后仍然未加载完成"%timeout)
#
#     def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
#         '''
#         等待页面元素消失
#         :param driver:浏览器驱动
#         :param locate_type:定位类型
#         :param locator_expression: 定位表达式
#         :param timeout:超时时间
#         :return:
#         '''
#         # 如果有定位
#         if locate_type:
#             start_time = time.time() * 1000
#             stop_time = start_time + (1000 * timeout)
#
#             for x in range(int(timeout*10)):
#                 try:
#                     element = driver.find_element(By=locate_type, value=locator_expression)
#                     # 如果元素必须可见，判断元素是否显示在页面上
#                     if element.is_displayed():
#                         now_ms = time.time() * 1000
#                         if now_ms >= stop_time:
#                             break
#                         time.sleep(0.1)
#                 except Exception:
#                     return True
#             raise Exception("元素没有消失，定位方式："+locate_type + "\n定位表达式："+locator_expression)
#         else:
#             pass
#
#     def element_appear(self,  driver, locate_type, locator_expression, timeout=30):
#         '''
#         等待元素可见
#         :param driver:  浏览器驱动
#         :param locate_type: 定位类型
#         :param locator_expression: 定位表达式
#         :param timeout: 超时时间
#         :return:
#         '''
#         if locate_type:
#             start_time = time.time()*1000
#             stop_time = start_time + (timeout*1000)
#
#             for x in range(int(timeout *10)):
#                 try:
#                     element = driver.find_element(By=locate_type, value=locator_expression)
#                     # 如果是可见的
#                     if element.is_displayed():
#                         return element
#                     else:
#                         raise Exception()
#                 except Exception:
#                     now_ms = time.time() * 1000
#                     if now_ms >= stop_time:
#                         break
#                     time.sleep(0.1)
#                     pass
#             # raise ElementNotVisibleException("元素没有出现，定位方式："+locate_type+"定位表达式: " +locator_expression)
#         else:
#             pass
#
#     def element_to_url(self,
#                        driver,
#                        url,
#                        locate_type_disappear=None,
#                        locator_expression_disappear=None,
#                        locate_type_appear =None,
#                        locator_expression_appear=None
#                        ):
#         '''
#         跳转地址
#         :param driver: 浏览器驱动
#         :param url: 地址
#         :param locate_type_disappear: 等待页面元素消失的定位类型
#         :param locator_expression_disappear: 等待页面元素消失的定位表达式
#         :param locate_type_appear: 等待元素可见的定位类型
#         :param locator_expression_appear: 等待元素可见的定位表达式
#         :return:
#         # 后四个参数使用场景：登录跳转首页，判断登录按钮的消失，首页的logg的可见显示
#         '''
#         try:
#             # 基本地址+参数地址 = 完整的url
#             driver.get(self.URL + url)
#             # 等待页面元素加载完成
#             self.wait_for_ready_state_complete(driver, timeout=30)
#             # 跳转页面后等待元素消失(如登录-》首页，判断登录按钮消失)
#             self.element_disappear(driver,locate_type_disappear, locator_expression_disappear)
#             # 跳转页面后等待元素显示((如登录-》首页，判断首页log出现))
#             self.element_appear(driver,locate_type_appear, locator_expression_appear)
#         except Exception as e:
#             print( "跳转地址出现异常，异常原因：%s" %e)
#             return False
#         return True
#
#
#     # 元素是否出现的封装：我想找的元素在当前页面上吗？
#     def element_is_display(self,driver, locate_type, locator_expression):
#         '''
#         元素是否显示
#         :param driver:
#         :param locate_type:
#         :param locator_expression:
#         :return:
#         '''
#         try:
#             driver.find_element(By=locate_type, value= locator_expression)
#         #     如果显示
#             return True
#         except NoSuchElementException:
#             print("页面元素未找到")
#             # 如果不显示
#             return False
#
#     # 元素填值的封装：填写输入框
#     def element_send_value(self, driver, locate_type, locator_expression, send_value, timeout = 30):
#         '''
#         元素填值
#         :param driver:
#         :param locate_type:
#         :param locator_expression:
#         :param send_value:
#         :param timeout:
#         :return:
#         '''
#         # 元素出现
#         element = self.element_appear(driver, locate_type, locator_expression, timeout)
#         # 先清除元素中原有值
#         try:
#             element.clear()
#         #  StaleElementReferenceException: 页面元素没有刷新出来，对异常进行捕获
#         except StaleElementReferenceException:
#             # 等待页面完全加载完成的封装
#             self.wait_for_ready_state_complete(driver)
#             time.sleep(0.06)
#             element = self.element_appear(driver, locate_type, locator_expression, timeout)
#             try:
#                 element.clear()
#             except:
#                 pass
#         except Exception:
#             pass
#         # 填入值转为字符串
#         if type(send_value) is int or type(send_value) is float:
#             send_value = str(send_value)
#         try:
#             #  如果结尾不是\n则直接填入值
#             if not send_value.endswith("\n"):
#                 element.send_keys(send_value)
#                 # 元素加载完成
#                 self.wait_for_ready_state_complete(driver)
#             else:
#                 send_value = send_value[:-1]
#                 element.send_keys(send_value)
#                 # 回车
#                 element.send_keys(Keys.RETURN)
#                 self.wait_for_ready_state_complete(driver)
#
#         except StaleElementReferenceException:
#             # 元素加载完成
#             self.wait_for_ready_state_complete(driver)
#             time.sleep(0.05)
#             # 判断元素是否存在
#             element = self.element_appear(driver, locate_type, locator_expression, timeout)
#             element.clear()
#             #  如果结尾不是\n则直接填入值
#             if not send_value.endswith("\n"):
#                 element.send_keys(send_value)
#                 # 元素加载完成
#                 self.wait_for_ready_state_complete(driver)
#             else:
#                 send_value = send_value[:-1]
#                 element.send_keys(send_value)
#                 # 回车
#                 element.send_keys(Keys.RETURN)
#                 # 元素加载完成
#                 self.wait_for_ready_state_complete(driver)
#         except Exception:
#             raise Exception("填值失败")
#
#     def element_click(self,
#                       driver,
#                       locate_type,
#                       locator_expression,
#                       locate_type_disappear = None,
#                       locator_expression_disappear = None,
#                       locate_type_appear = None,
#                       locator_expression_appear = None,
#                       timeout = 30
#                       ):
#         '''
#         元素点击
#         :param driver:
#         :param locate_type: 定位类型
#         :param locator_expression: 表达式
#         :param locate_type_disappear: 等待页面元素消失的定位类型
#         :param locator_expression_disappear: 等待页面元素消失的定位表达式
#         :param locate_type_appear: 等待元素可见的定位类型
#         :param locator_expression_appear: 等待元素可见的定位表达式
#         :return:
#         '''
#         # 元素可见
#         element = self.element_appear(driver, locate_type, locator_expression, timeout)
#         try:
#             element.click()
#         except StaleElementReferenceException:
#             self.wait_for_ready_state_complete(driver)
#             time.sleep(0.06)
#             element = self.element_appear(driver, locate_type, locator_expression, timeout)
#             element.click()
#         except Exception as e:
#             print("页面出现异常，元素不可点击", e)
#             return False
#         try:
#             # 点击元素后，元素出现或消失
#             self.element_appear(driver, locate_type, locator_expression)
#             self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)
#         except Exception as e:
#             print('等待元素消失或出现失败', e)
#             return False
#         return True
class ObjectMap:
    # 获取基准地址
    url = GetConf().get_url()

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        """
        单个元素获取
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :param must_be_visible:元素是否可见，True是必须可见，False是默认值
        :return: 返回的元素
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)
                # 如果元素不是必须可见的，就直接返回元素
                if not must_be_visible:
                    return element
                # 如果元素必须可见，则先判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time()
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败,定位方式：" + locate_type + "定位表达式" + locator_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等待页面完全加载完成
        :param driver:浏览器驱动
        :param timeout:超时时间
        :return:
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # 获取页面状态
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                # 如果有driver的错误，执行js会失败，直接跳过
                time.sleep(0.03)
                return True
            # 如果页面元素全部加载完成，返回True
            if ready_state == 'complete':
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("打开网页时，页面元素在%s后仍然没有加载完" % timeout)

    def element_disappear(self, driver, locate_type, locate_expression, timeout=30):
        """
        等待页面元素消失
        :param driver:浏览器驱动
        :param locate_type: 定位方式类型
        :param locate_expression: 定位表达式
        :param timeout: 超市时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locate_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式" + locate_type + "\n定位表达式" + locate_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locate_expression, timeout=30):
        """
        等待页面元素出现
        :param driver:
        :param locate_type:
        :param locate_expression:
        :param timeout:
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locate_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()

                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException("元素没有出现，定位方式" + locate_type + " 定位表达式" + locate_expression)

        else:
            pass

    def element_to_url(
            self,
            driver,
            url,
            locate_type_disappear=None,
            locate_expression_disappear=None,
            locate_type_appear=None,
            locate_expression_appear=None
    ):
        """
        跳转地址
        :param driver:浏览器驱动
        :param url: 跳转的地址
        :param locate_type_disappear: 等待页面元素消失的定位方式
        :param locate_expression_disappear:等待页面元素消失的定位表达式
        :param locate_type_appear:等待页面元素出现的定位方式
        :param locate_expression_appear:等待页面元素出现的定位表达式
        :return:
        """
        try:
            driver.get(self.url + url)
            # 等待页面元素加载完成
            self.wait_for_ready_state_complete(driver)
            # 跳转地址后等待元素消失
            self.element_disappear(driver, locate_type_disappear, locate_expression_disappear)
            # 跳转地址后等待元素出现
            self.element_appear(driver, locate_type_appear, locate_expression_appear)
        except Exception as e:
            print("跳转地址出现异常，异常原因：%s" % e)
            return False
        return True

    def element_is_display(self, driver, locate_type, locate_expression):
        """
        元素是否显示
        :param driver:
        :param locate_type:
        :param locate_expression:
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locate_expression)
            return True
        except NoSuchElementException:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False

    def element_fill_value(self, driver, locate_type, locate_expression, fill_value, timeout=30):
        """
        元素添置
        :param driver:浏览器驱动
        :param locate_type:定位方式
        :param locate_expression:定位表达式
        :param fill_value:填充值
        :param timeout:超时时间
        :return:
        """
        # 元素必须先出现
        element = self.element_appear(
            driver,
            locate_type=locate_type,
            locate_expression=locate_expression,
            timeout=timeout
        )
        try:
            element.clear()
        except StaleElementReferenceException:  # 页面元素没有刷新出来，就对元素进行捕获从而引发的异常
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver,
                                          locate_type=locate_type,
                                          locate_expression=locate_expression,
                                          timeout=timeout
                                          )
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        # 填入值转成字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            # 不是以\n结尾
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver,
                                          locate_type=locate_type,
                                          locate_expression=locate_expression,
                                          timeout=timeout)
            element.clear()
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            raise Exception("元素填值失败")
        return True

    def element_click(self,
                      driver,
                      locate_type,
                      locate_expression,
                      locate_type_disappear=None,
                      locate_expression_disappear=None,
                      locate_type_appear=None,
                      locate_expression_appear=None,
                      timeout=30):
        """
        元素点击
        :param driver: 浏览器驱动
        :param locate_type:定位方式
        :param locate_expression:定位表达式
        :param locate_type_disappear: 等待元素消失的定位方式类型
        :param locate_expression_disappear:等待元素消失的定位表达式
        :param locate_type_appear:等待元素出现的定位方式类型
        :param locate_expression_appear:等待元素出现的定位表达式
        :param timeout:超时时间
        :return:

        """
        element = self.element_appear(driver=driver,
                                      locate_type=locate_type,
                                      locate_expression=locate_expression,
                                      timeout=timeout)
        try:
            # 点击元素
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver=driver,
                                          locate_type=locate_type,
                                          locate_expression=locate_expression,
                                          timeout=timeout)
            element.click()
        except Exception as e:
            print("页面出现异常，元素不可点击", e)
            return False

        try:
            # 点击元素后的元素出现或消失
            self.element_appear(driver,
                                locate_type=locate_type_appear,
                                locate_expression=locate_expression_appear)
            self.element_disappear(driver,
                                   locate_type=locate_type_disappear,
                                   locate_expression=locate_expression_disappear)
        except Exception as e:
            print("等待元素消失或出现失败", e)
            return False
        return True

    def upload(self, driver, locate_type, locate_expression, file_path):
        """
        文件/图片等上传
        :param driver:
        :param locate_type:
        :param locate_expression:
        :param file_path:
        :return:
        """
        # element_get :自定义的元素定位方法
        element = self.element_get(driver, locate_type, locate_expression)
        return element.send_keys(file_path)

    def switch_into_iframe(self, driver, locate_iframe_type, locate_iframe_expression):
        """
        进入iframe
        :param driver: 浏览器驱动
        :param locate_iframe_type: 定位iframe方式
        :param locate_iframe_expression:定位iframe表达式
        :return:
        """
        iframe = self.element_get(driver, locate_iframe_type, locate_iframe_expression)
        driver.switch_to.frame(iframe)

    def switch_from_iframe_to_content(self, driver):
        """
        从iframe切回主文当
        :param dirver:
        :return:
        """
        driver.switch_to.parent_frame()

    def switch_window_2_latest_handle(self, driver):
        """
        句柄切换串口到最新的窗口
        :param driver:
        :return:
        """
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

    def find_img_in_source(self, driver, img_name):
        '''
        截图并在截图中查找图片
        :param driver:
        :param img_name:
        :return:
        '''
        # 截图后图片保存路径
        source_img_path = get_project_path() + file_sep(['img', 'source_img', img_name], add_sep_before=True)
        # 需要查找图片的路径
        search_img_path = get_project_path() + file_sep(['img', 'assert_img', img_name], add_sep_before=True)
        # print(source_img_path)
        # print(search_img_path)
        # 截图并保存图片
        driver.get_screenshot_as_file(source_img_path)
        time.sleep(3)
        # 在原图中查找是否有指定的图片，返回信心值
        confidence = FindImg().get_confidence(source_img_path, search_img_path)
        return confidence
if __name__ == '__main__':
    driver = DriverConfig().driver_config()
    ObjectMap().find_img_in_source(driver=driver, img_name='po3.jpg')