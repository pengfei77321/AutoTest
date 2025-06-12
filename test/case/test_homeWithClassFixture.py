# -*-coding:utf-8-*-
import pytest
from test.pages.homePage import HomePage

class TestHome:
    """测试主页功能"""

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        request.cls.home = HomePage()
        request.cls.home.login()
        yield
        request.cls.home.quit_driver()

    def test_home01_add_data_cancel(self):
        """测试添加数据时取消"""
        self.home.add_data(code='302010', name="测试数据", sex="女", grader="六年级一班", button="取消")

    def test_home02_add_data_confirm(self):
        """测试添加数据成功"""
        self.home.add_data(code='302010', name="测试数据", sex="女", grader="六年级一班", button="确定")

    def test_home03_edit_data_cancel(self):
        """测试编辑数据时取消"""
        self.home.edit_data(header_text="姓 名", row_text="测试数据", code='302011', sex="男", button="取消")

    def test_home04_edit_data_confirm(self):
        """测试编辑数据成功"""
        self.home.edit_data(header_text="姓 名", row_text="测试数据", code='302011', sex="男", button="确定")

    def test_home05_search(self):
        """测试搜索功能"""
        self.home.search("测试数据")

    def test_home06_delete_data_cancel(self):
        """测试删除数据取消"""
        self.home.delete_data(header_text="姓 名", row_text="测试数据", button="取消")

    def test_home07_delete_data_confirm(self):
        """测试删除数据成功"""
        self.home.delete_data(header_text="姓 名", row_text="测试数据", button="确定")

if __name__ == '__main__':
    pytest.main(["-s", "-v", __file__])