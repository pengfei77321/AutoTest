# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By

class ElementIsExist(object):
    def __init__(self, driver):
        self.driver = driver

    def is_exist(self, element):
        flag = True
        try:
            self.driver.find_element(By.CSS_SELECTOR, element)
            return flag
        
        except:
            flag = False
            return flag