from common.base import Base
from common.config import host
import allure
import time

login_url = host
class LoginPage(Base):
    loc_1 = ("xpath", '//*[@id="kw"]')            # 输入框
    loc_3 = ("xpath", '//*[@id="su"]')   # 登录按钮

    # 判断元素
    loc_4 = ("xpath", '//*[@id="content_left"]/div[1]/div/span/i')


    @allure.step("步骤：1.登陆web    2.输入正确的账号和密码")
    def login(self, username="songxuelong"):
        '''登录'''

        self.driver.get(login_url)
        self.send(self.loc_1, username)
        self.click(self.loc_3)

    @allure.step("步骤：判断登录是否成功")
    def is_login_success(self):
        '''判断登录是否成功'''
        result = self.is_element_exist(self.loc_4)
        return result

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    web.login()

    result = web.is_login_success()
    print(result)
    time.sleep(3)
    driver.quit()