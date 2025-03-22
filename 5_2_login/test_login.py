import time

from selenium.webdriver.common.by import By

from config.driver_config import test_driver_config

web_driver = test_driver_config()
web_driver.get('https://doc.pescms.com/?g=Doc&m=Login&a=index')
element = web_driver.find_element(By.XPATH, '//input[@placeholder="登录账号"]')
element.clear()
time.sleep(1)
element.send_keys('guanli')
find_element = web_driver.find_element(By.XPATH, '//input[@placeholder="登录密码"]')
find_element.clear()
time.sleep(1)
find_element.send_keys('123456')
time.sleep(3)
web_driver.find_element(By.XPATH, '//button[contains(text(),"登录")]').click()
time.sleep(3)
web_driver.quit()