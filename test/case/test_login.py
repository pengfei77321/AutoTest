# -*-coding:utf-8-*-
import pytest
from test.pages.loginPage import LoginPage

class TestLogin:
    """登陆测试"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.login = LoginPage()
        yield
        self.login.quit_driver()

    def test_login01(self):
        """登录成功"""
        self.login.login()

if __name__ == '__main__':
    pytest.main(["-s", "-v", __file__])