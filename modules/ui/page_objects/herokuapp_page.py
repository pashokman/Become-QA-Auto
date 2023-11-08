from modules.ui.page_objects.base_page import BasePage
from utils.logger import Loger
from selenium.webdriver.common.action_chains import ActionChains

class HerokuAppPage(BasePage):
    log = Loger.custom_logger()

    MAIN_URL = "https://the-internet.herokuapp.com/"

    def __init__(self):
        super().__init__()

    def start(self):
        text = "TESTING PERSONAL_UI_2"
        self.log.critical(f"{text:.^75}")

    def end(self):
        text = "SUCCESSFUL END OF TESTING - PERSONAL_UI_2"
        self.log.critical(f"{text:.^75}")

        # Steps to reproduce
    def go_to_add_remove_elem_page(self):
        self.go_to(HerokuAppPage.MAIN_URL)
        self.log.debug("Open herokuapp page.")
        addRemElemLink = self.find_element_by_xpath("//a[normalize-space()='Add/Remove Elements']")
        addRemElemLink.click()
        self.log.debug("Click on 'Add/remove element' link.")


    def click_add_elem(self, numb_click):
        while numb_click > 0:
            self.find_element_by_xpath("//button[normalize-space()='Add Element']").click()
            numb_click -= 1
            self.log.debug("Click on 'Add Element' button.")


    def click_del_elem(self, numb_click):
        elem_list = self.find_elements_by_xpath("//button[@class='added-manually']")
        while numb_click > 0:
            elem_list[0].click()
            numb_click -= 1
            self.log.debug("Click on 'Delete' button.")


    def go_to_drag_and_drop_page(self):
        self.go_to(HerokuAppPage.MAIN_URL)
        self.log.debug("Open drag and drop page.")
        dragAndDropLink = self.find_element_by_xpath("//a[normalize-space()='Drag and Drop']")
        dragAndDropLink.click()
        self.log.debug("Click on 'Add Element' button.")


    def drag_elem_and_drop(self):
        drag_from = self.find_element_by_id('column-a')
        drag_to = self.find_element_by_id('column-b')

        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_from, drag_to).perform()
        self.log.debug("Drag and drop elements.")


        # Assertions
        # Check if element exist
    def elements_count_assertion(self, xpath, count):
        assert len(self.find_elements_by_xpath(xpath)) == count
        self.log.info(f"! Successful ! Elements count is - {count}.")

    def drag_and_drop_assertion(self):
        elem_list = self.find_elements_by_xpath("//div[@class='column']")
        assert ((elem_list[0].text == "B") and (elem_list[1].text == "A")) == True
        self.log.info(f"! Successful ! Drag and drop completed.")