###step1
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options=opt)
#
# driver.get('https://demowebshop.tricentis.com/')
# login_btn=driver.find_element('xpath',"//a[.='Log in']")
# login_btn.click()
# email_btn=driver.find_element('id','Email')
# email_btn.send_keys('athulmr249@gmail.com')
# password_btn=driver.find_element('id','Password')
# password_btn.send_keys('Athul@mr2')
# login_btn=driver.find_element('xpath','//input[@value="Log in"]')
# login_btn.click()

#######################################
#step2
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
#
# driver.get('https://demowebshop.tricentis.com/')
# class LoginPage:
#     def click_login_link(self):
#         login_btn=driver.find_element('xpath',"//a[.='Log in']")
#         login_btn.click()
#     def enter_email(self):
#         email_btn=driver.find_element('id','Email')
#         email_btn.send_keys('athulmr249@gmail.com')
#     def enter_password(self):
#         password_btn=driver.find_element('id','Password')
#         password_btn.send_keys('Athul@mr2')
#     def click_login_btn(self):
#         login_btn=driver.find_element('xpath','//input[@value="Log in"]')
#         login_btn.click()
#
#
# login_page=LoginPage()
# login_page.click_login_link()
# login_page.enter_email()
# login_page.enter_password()
# login_page.click_login_btn()

######################################
# step3
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# driver.get('https://demowebshop.tricentis.com/')
# class LoginPage:
#     def click_login_link(self):
#         login_btn=driver.find_element('xpath',"//a[.='Log in']")
#         login_btn.click()
#     def enter_email(self):
#         email_btn=driver.find_element('id','Email')
#         email_btn.send_keys('athulmr249@gmail.com')
#     def enter_password(self):
#         password_btn=driver.find_element('id','Password')
#         password_btn.send_keys('Athul@mr2')
#     def click_login_btn(self):
#         login_btn=driver.find_element('xpath','//input[@value="Log in"]')
#         login_btn.click()

##############################################
#step4:moving the driver setup to the test file
# class LoginPage:
#     def click_login_link(self):
#         login_btn=driver.find_element('xpath',"//a[.='Log in']")
#         login_btn.click()
#     def enter_email(self):
#         email_btn=driver.find_element('id','Email')
#         email_btn.send_keys('athulmr249@gmail.com')
#     def enter_password(self):
#         password_btn=driver.find_element('id','Password')
#         password_btn.send_keys('Athul@mr2')
#     def click_login_btn(self):
#         login_btn=driver.find_element('xpath','//input[@value="Log in"]')
#         login_btn.click()
# # error as the driver is not present

#############################################################
# step5
# class LoginPage:
#     def __init__(self,driver):
#         self.driver=driver
#     def click_login_link(self):
#         login_btn=self.driver.find_element('xpath',"//a[.='Log in']")
#         login_btn.click()
#     def enter_email(self):
#         email_btn=self.driver.find_element('id','Email')
#         email_btn.clear()
#         email_btn.send_keys('athulmr249@gmail.com')
#     def enter_password(self):
#         password_btn=self.driver.find_element('id','Password')
#         password_btn.clear()
#         password_btn.send_keys('Athul@mr2')
#     def click_login_btn(self):
#         login_btn=self.driver.find_element('xpath','//input[@value="Log in"]')
#         login_btn.click()
#############################################################
from pages.base_page import BasePage
#
# class LoginPage(BasePage):
#     def __init__(self,driver):
#         super().__init__(driver)
#
#     def login(self):
#         self.click(('xpath',"//a[.='Log in']"))
#         self.send_keys(('id','Email'),'athulmr249@gmail.com')
#         self.send_keys(('id','Password'),'Athul@mr2')
#         self.click(('xpath','//input[@value="Log in"]'))
#
##############################################################
class LoginPage(BasePage):
    log_in=('xpath',"//a[.='Log in']")
    email_cred=('id','Email')
    password_cred=('id','Password')
    log_in_btn=('xpath','//input[@value="Log in"]')

    def __init__(self,driver):
        super().__init__(driver)

    def login(self):
        self.click(self.log_in)
        self.send_keys(self.email_cred,'athulmr249@gmail.com')
        self.send_keys(self.password_cred,'Athul@mr2')
        self.click(self.log_in_btn)

        
        print('hei hello')
        print('this is from kannathal')