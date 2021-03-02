from common.base import Base
from common.config import host
import allure
import time


class ArticlclassifyPage(Base):
    子集_客户管理 = ("xpath", '//*[@id="result_logo"]/img[1]')
    点击_详情 = ("xpath", '//*[@id="kw"]')

    # 判断元素
    table = ("xpath", '//*[@id="result_logo"]/img[1]')

    @allure.step("步骤：点击详情按钮")
    def edit_classify(self, name="小皮球"):
        '''点击详情按钮'''
        self.click(self.子集_客户管理)
        self.send(self.点击_详情, name)

    @allure.step("步骤：判断是否跳转详情页面成功，返回布尔值")
    def is_edit_classify_success(self):
        '''判断是否添加成功，返回布尔值'''
        result = self.is_element_exist(self.table)
        return result
