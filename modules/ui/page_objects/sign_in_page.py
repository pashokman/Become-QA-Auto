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
        self.paste_value_into_field(login_elem, username)       
            # Find password field
        password_elem = self.find_element_by_id("password")        
            # Enter wrong password
        self.paste_value_into_field(password_elem, password)       
            # Find button 'Login'
        btn_login = self.find_element_by_name('commit')        
            # Click on btn
        btn_login.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
    def title_testing(self, username, password, expected_title):
        self.go_to()
        self.try_login(username, password)
        self.check_title(expected_title)
        self.close()