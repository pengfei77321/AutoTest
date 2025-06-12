# -*-utf-8-*-
from time import sleep
from selenium.webdriver.common.by import By
from test.common.elementIsExist import ElementIsExist

class TabOperation(object):
    """Tab操作"""
    def __init__(self, driver):
        self.driver = driver

    def get_all_tab(self):
        """获取所有的tab"""
        sleep(1)

        # 获取所有的tab父元素
        # 元素定位, 我们默认取CSS定位
        fathers_tabs = [('.tabs1', 'a2'),
                        ('.tabs', 'a'),
                        ]
        # 获取页面显示父节点下的所有tab
        for father_tab in fathers_tabs:
            # 使用is_exist()方法判断父节点是否存在,如果父节点不存在,则查找的tab不匹配
            father_exist = ElementIsExist(self.driver).is_exist(father_tab[0])

            # 父节点存在,则进行操作
            if father_exist:
                father = self.driver.find_element(By.CSS_SELECTOR, father_tab[0])
                tabs = father.find_elements(By.CSS_SELECTOR, father_tab[1])
                return tabs

    def switch_tab(self, tab_text):
        """
        切换tab
        :param tab_text: 需要切换到的tab内容
        :return:
        """
        tabs = self.get_all_tab()
        for tab in tabs:
            print(tab.text)
            if tab.text == tab_text:
                tab.click()
                return

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('file:///G:/Study/%E4%B9%A6%E7%B1%8D/python%E8%87%AA%E5%8A%A8%E5%8C%96/Python%20Web%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%85%A5%E9%97%A8%E4%B8%8E%E5%AE%9E%E6%88%98%20(%E6%9D%A8%E5%AE%9A%E4%BD%B3)/AutoTestExample-master/projectHtml/chapter9/period4-1/index.html')
    sleep(1)
    tab = TabOperation(driver)
    tab.switch_tab('Tab3')

    sleep(10)
    driver.quit()