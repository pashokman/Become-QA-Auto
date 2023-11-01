from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find login field
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Enter nonexisting username/email
        login_elem.send_keys(username)

        # Find password field
        password_elem = self.driver.find_element(By.ID, "password")

        # Enter wrong password
        password_elem.send_keys(password)

        # Find button 'Login'
        btn_login = self.driver.find_element(By.NAME, 'commit')

        # Click on btn
        btn_login.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
    def title_testing(self, username, password, expected_title):
        self.go_to()
        self.try_login(username, password)
        self.check_title(expected_title)
        self.close()