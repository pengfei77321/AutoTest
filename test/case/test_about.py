# -*-coding:utf-8-*-
import allure
import pytest
from test.pages.aboutPage import AboutPage

class TestAbout:
    """测试关于我们页面"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.about = AboutPage()
        self.about.login()
        yield
        self.about.quit_driver()

    @allure.story("关于我们")
    @allure.title("测试关于我们页面加载")
    def test_about01(self):
        """进入关于我们页面测试"""
        self.about.select_menu("关于我们")
        about = self.about.about_element()
        assert "关于我们" == about.text

if __name__ == '__main__':
    pytest.main(["-s", "-v", __file__])