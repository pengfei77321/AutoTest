# -*-coding:utf-8-*-
import os
import subprocess
import time
import pytest

class Main:
    # 删除 get_all_case() 方法调用
    # 使用pytest的自动发现机制（不需要手动指定测试文件）
    # def get_all_case(self):
    #     """获取所有测试用例"""
    #     current_path = os.path.abspath(os.path.dirname(__file__))
    #     case_path = os.path.join(current_path, '../case')
    #     return [os.path.join(case_path, f) for f in os.listdir(case_path)
    #             if f.startswith('test') and f.endswith('.py')]

    def generate_allure_report(self, results_dir, report_dir):
        """生成Allure报告"""
        os.makedirs(results_dir, exist_ok=True)
        os.makedirs(report_dir, exist_ok=True)

        # 使用绝对路径
        results_dir = os.path.abspath(results_dir)
        report_dir = os.path.abspath(report_dir)

        result = subprocess.run(
            "where allure",
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        print(f"result: {result.stdout} ------")
        allure_path = result.stdout.strip().split('\n')[0]
        print(f"allure_path: {allure_path}")
        cmd = f"{allure_path} generate {results_dir} -o {report_dir} --clean"
        print("生成报告命令:", cmd)
        os.system(cmd)
        print(f"Allure报告已生成至: {report_dir}")

        # 自动打开报告
        os.system(f"{allure_path} open {report_dir}")

    def run_case(self):
        """执行测试并生成报告"""
        current_path = os.path.abspath(os.path.dirname(__file__))
        project_root = os.path.abspath(os.path.join(current_path, '../..'))

        # 报告目录设置
        base_report_path = os.path.join(project_root, 'report')
        results_dir = os.path.join(base_report_path, 'allure_results')
        report_dir = os.path.join(base_report_path, 'allure_report')

        # 确保使用绝对路径
        results_dir = os.path.abspath(results_dir)
        report_dir = os.path.abspath(report_dir)
        os.makedirs(results_dir, exist_ok=True)
        os.makedirs(report_dir, exist_ok=True)

        # test_cases = self.get_all_case()

        print("="*50)
        print(f"项目根目录: {project_root}")
        print(f"Allure结果目录: {results_dir}")
        print(f"Allure报告目录: {report_dir}")
        print("="*50)

        # 切换到项目根目录(确保pytest.ini被识别)
        os.chdir(project_root)

        # 构建命令字符串
        cmd_args = [
            '-c', 'pytest.ini', # 显示指定配置文件
            '-v',
            f'--alluredir={results_dir}',
            # *test_cases
        ]
        # cmd_str = "pytest " + " ".join(f'"{arg}"' for arg in cmd_args)
        print("执行命令:", "pytest " + " ".join(cmd_args))

        # 执行测试（使用pytest的自动测试发现机制）
        exit_code = pytest.main(cmd_args)

        if exit_code == 0:
            print("√√√√ 所有测试执行成功!")
        else:
            print(f"×××× 测试失败，退出码: {exit_code}")

        # 生成报告
        self.generate_allure_report(results_dir, report_dir)

if __name__ == '__main__':
    Main().run_case()