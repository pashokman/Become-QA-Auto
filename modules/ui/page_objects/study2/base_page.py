from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from allure_commons.types import AttachmentType


class BasePage():

    def __init__(self, browser = 'chrome'):
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        self.driver.maximize_window()


    # Go to some page ------------------------------------------------------------------------------------------------
    def go_to(self, url):
        self.driver.get(url)


    # Handle dynamic scroll ------------------------------------------------------------------------------------------
    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;"
        )
        match = False
        while match == False:
            lastCount = pageLength
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;"
            )
            if lastCount == pageLength:
                match = True


    def scroll_into_view(self, element):
        js_code = "arguments[0].scrollIntoView(true)"   
        self.driver.execute_script(js_code, element)


    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        
        return list_of_elements


    def wait_until_element_is_clicable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        
        return element


    def wait_until_text_to_be_present_in_element_value(self, locator_type, locator, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.text_to_be_present_in_element_value((locator_type, locator), text))
        
        return element


    def wait_until_presence_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        
        return element


    def wait_until_next_page_open(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.number_of_windows_to_be(2))


    def make_screenshot(self, filename):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{filename}", attachment_type=AttachmentType.PNG)


    def switch_to_frame(self, iframe):
        self.driver.switch_to.frame(iframe)


    # Close driver --------------------------------------------------------------------------------------------------
    def close(self):
        self.driver.close()
        