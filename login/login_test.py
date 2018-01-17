from selenium import webdriver
from time import sleep

class Login_Test():
    def __init__(self,username='',password='',re_password='',email=''):
        self.username = username
        self.password = password
        self.re_password = re_password
        self.email = email

    def login_test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(r'http://118.31.19.120:3000/signup')
        sleep(3)
        username = driver.find_element_by_id('loginname')
        username.clear()
        username.send_keys(self.username)
        password = driver.find_element_by_id('pass')
        username.clear()
        password.send_keys(self.password)
        re_pass = driver.find_element_by_id('re_pass')
        username.clear()
        re_pass.send_keys(self.re_password)
        email = driver.find_element_by_id('email')
        username.clear()
        email.send_keys(self.email)
        sleep(3)
        login = driver.find_element_by_class_name('span-primary')
        login.click()
        sleep(3)
        driver.quit()


if __name__ == '__main__':
    login = Login_Test('18956376183','123456','123456','123')
    login.login_test()
