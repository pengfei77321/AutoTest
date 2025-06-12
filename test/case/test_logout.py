# -*-coding:utf-8-*-

import pytest
from test.pages.loginPage import LoginPage

class TestLogout:
    """测试退出登录功能"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.login = LoginPage()
        self.login.login()
        yield
        self.login.quit_driver()

    def test_logout01(self):
        """测试退出登录"""
        self.login.log_out()

if __name__ == '__main__':
    pytest.main(["-s", "-v", __file__])
