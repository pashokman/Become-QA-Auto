"""
Here I create my first SignInPage class based on BasePage class with it's own methods.
"""

from modules.ui.page_objects.base_page import BasePage


class SignInPage(BasePage):

    URL = "https://github.com/login"

    def __init__(self):
        super().__init__()


    def go_to(self):
        self.driver.get(SignInPage.URL)


    def try_login(self, username, password):
        # Find login field
        login_elem = self.find_element_by_id("login_field")        
        
        # Enter nonexisting username/email
        login_elem.send_keys(f'{username}')     
        
        # Find password field
        password_elem = self.find_element_by_id("password")        
        
        # Enter wrong password
        password_elem.send_keys(f'{password}')      
        
        # Find button 'Login'
        btn_login = self.find_element_by_name('commit')        
        
        # Click on btn
        btn_login.click()


    def get_err_message(self):
        err_message = self.find_element_by_class("js-flash-alert")
        
        return err_message
        

    def get_title(self):
        return self.driver.title
    