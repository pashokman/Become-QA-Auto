from modules.ui.page_objects.base_page import BasePage
from utils.logger import Loger
from selenium.webdriver.common.action_chains import ActionChains


class HerokuAppPage(BasePage):
    
    log = Loger.custom_logger()

    MAIN_URL = "https://the-internet.herokuapp.com/"

    def __init__(self):
        super().__init__()


    # Methods that add additional info string in logs about start/end of testing this module. ------------------------
    def start(self):
        text = "TESTING HEROKUAPP_UI"
        self.log.critical(f"{text:.^75}")


    def end(self):
        text = "SUCCESSFUL END OF TESTING - HEROKUAPP_UI"
        self.log.critical(f"{text:.^75}")


    # Steps to reproduce methods -------------------------------------------------------------------------------------
    def go_to_add_remove_elem_page(self):
        self.go_to(HerokuAppPage.MAIN_URL)
        self.log.debug("Open herokuapp page.")
        addRemElemLink = self.find_element_by_xpath("//a[normalize-space()='Add/Remove Elements']")
        addRemElemLink.click()
        self.log.debug("Click on 'Add/remove element' link.")


    def click_add_elem_times(self, numb_click):
        while numb_click > 0:
            self.find_element_by_xpath("//button[normalize-space()='Add Element']").click()
            numb_click -= 1
            self.log.debug("Click on 'Add Element' button.")

    
    def get_added_elements_count(self):
        return len(self.find_elements_by_xpath("//button[@class='added-manually']"))


    def click_del_elem_times(self, numb_click):
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


    def drag_and_drop_elem(self):
        drag_from = self.find_element_by_id('column-a')
        drag_to = self.find_element_by_id('column-b')

        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_from, drag_to).perform()
        self.log.debug("Drag and drop elements.")


    def get_drag_and_drop_elem_list(self):
        return self.find_elements_by_xpath("//div[@class='column']")
