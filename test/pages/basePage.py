# -*-coding:utf-8-*-
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class BasePage(object):
    """基础页面"""

    def __init__(self, driver=None, base_url=None):
        """
        基础参数, webdriver,默认访问的URL
        :param driver: 浏览器驱动
        :param base_url: 默认打开的url, 一般都是登陆页面
        """

        if driver is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            driver_path = current_path + "/../../drivers/chromedriver.exe"
            # driver_path = os.path.abspath(os.path.join(current_path + "/../../drivers/chromedriver.exe"))
            print(driver_path)

            # 检查文件是否存在
            if not os.path.exists(driver_path):
                raise FileNotFoundError(f"ChromeDriver 未找到: {driver_path}")

            service = Service(executable_path=driver_path)
            self.driver = webdriver.Chrome(service=service)
        else:
            self.driver = driver

        if base_url is None:
            self.base_url = 'http://192.168.31.18:39053/#/'
        else:
            self.base_url = base_url

        # 设置默认打开页面
        self.open_page()

    def open_page(self):
        """打开默认页面"""
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        sleep(1)

    def close_page(self):
        """关闭页面"""
        return self.driver.close()

    def quit_driver(self):
        """关闭页面且退出程序"""
        return self.driver.quit()

    def find_element(self, by, element):
        """返回单个定位元素"""
        sleep(1)
        return self.driver.find_element(by, element)

    def find_elements(self, by, element):
        """返回一组定位元素"""
        sleep(1)
        return self.driver.find_elements(by, element)

    def switch_alert(self):
        """返回弹窗页面"""
        sleep(1)
        return self.driver.switch_to_alert

    def select_menu(self, menu_text):
        """菜单选择"""
        sleep(1)
        menus_element = self.driver.find_elements(By.CSS_SELECTOR, '#menu>div>h4')
        print(menus_element)
        for menu in menus_element:
            # replace(" ", "")去掉字符串中的空格
            print(menu)
            print(menu.text)
            if menu.text.replace(' ', '') == menu_text.replace(' ', ''):
                print(menu.text.replace(' ', ''))
                print(menu_text.replace(' ', ''))
                return menu.click()
        print(menu_text + "未找到")
        return

    def log_out(self):
        """退出登录"""
        return self.select_menu("退出登录")
