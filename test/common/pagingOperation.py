# -*-coding:utf-8-*-

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class PagingOperation(object):
    """Tab操作"""
    def __init__(self, driver):
        self.driver = driver

        # 分页中每个操作元素进行定位
        # 分页
        self.paging = self.driver.find_element(By.CLASS_NAME, 'pagination')
        # 首页
        self.first = self.paging.find_element(By.CLASS_NAME, 'first')
        # 上一页
        self.previous = self.paging.find_element(By.CLASS_NAME, 'previous')
        # 下一页
        self.next = self.paging.find_element(By.CLASS_NAME, 'next')
        # 未页
        self.last = self.paging.find_element(By.CLASS_NAME, 'last')
        # 输入页数
        self.input = self.paging.find_element(By.CSS_SELECTOR, 'input')

    def paging_operation(self, text):
        """分页操作"""
        sleep(1)
        if text == "首页" or text == "第一页":
            return self.first.click()
        elif text == "上一页":
            return self.previous.click()
        elif text == "下一页":
            return self.next.click()
        elif text == "未页" or text == "最后一页":
            return self.last.click()
        elif type(text) == int:
            self.input.click()
            self.input.send_keys(text)
            self.input.send_keys(Keys.ENTER)
        else:
            error = "只接受首页、第一页、上一页、下一页、未页、最后一页和整型数字"
            print(error)
            return


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('file:///G:/Study/%E4%B9%A6%E7%B1%8D/python%E8%87%AA%E5%8A%A8%E5%8C%96/Python%20Web%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%85%A5%E9%97%A8%E4%B8%8E%E5%AE%9E%E6%88%98%20(%E6%9D%A8%E5%AE%9A%E4%BD%B3)/AutoTestExample-master/projectHtml/chapter9/period4-5/index.html')
    sleep(3)
    paging = PagingOperation(driver)
    paging.paging_operation(5)
    paging.paging_operation("上一页")
    paging.paging_operation("下一页")
    paging.paging_operation("首页")
    paging.paging_operation("未页")
    #driver.quit()
