from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        
    # Go to some page -----------------------------------------------------------------------------------------------
    def go_to(self, url):
        self.driver.get(url)


    # Find element by attribute (id, name, class, xpath) ------------------------------------------------------------
    def find_element_by_id(self, id):
        return self.driver.find_element(By.ID, id)
    

    def find_element_by_name(self, name):
        return self.driver.find_element(By.NAME, name)
    

    def find_element_by_class(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)
    

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)
    

    # Find list of elements_by_xpath --------------------------------------------------------------------------------
    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)


    # Scroll element into view --------------------------------------------------------------------------------------
    def scroll_into_view(self, element):
        js_code = "arguments[0].scrollIntoView(true)"
        self.driver.execute_script(js_code, element)


    # Close driver --------------------------------------------------------------------------------------------------
    def close(self):
        self.driver.close()