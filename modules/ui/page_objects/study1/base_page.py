from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, browser = 'chrome'):
        
        if browser.lower() == 'chrome':
            self.options = Options()
            # eager - need to work vs page content as soon as possible, before all page loaded
            self.options.page_load_strategy = 'eager'
            self.driver = webdriver.Chrome(options=self.options)
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

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


    # Wait for all list elements
    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        
        return list_of_elements

    # Close driver --------------------------------------------------------------------------------------------------
    def close(self):
        self.driver.close()