from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from modules.ui.page_objects.study2.base_page import BasePage

from utils.logger import Loger
from utils.additional_functions import AdditionalFunctions


LOG = Loger.custom_logger()


class GeneralPage(BasePage):

    ####### TEST BUILD ELEMENTS/CONSTANTS ----------------------------------------------------------------------------
    # Search calculator ----------------------------------------------------------------------------------------------
    CLOUD_URL = "https://cloud.google.com/"
    SEARCH_FIELD = "//input[@placeholder='Search']"

    # Open calculator result -----------------------------------------------------------------------------------------
    SEARCH_RESULT = "//div[@class='gs-title']//b[contains(text(),'Google Cloud Pricing Calculator')]"

    # Work with calculator -------------------------------------------------------------------------------------------
    CALC_URL = "https://cloud.google.com/products/calculator"
    EXTERNAL_IFRAME = 0
    INNER_IFRAME = "myFrame"
    COMPUTE_ENGINE_BTN = '//md-tab-item[@tabindex="0"]'
    INSTANCES = '//input[@id="input_101"]'
    OSSOFTWARE__DD = '//md-select-value[@id="select_value_label_93"]'
    OS_SOFTWARE_VALUES = '//div[@id="select_container_115"]//md-option'
    SERIES = '//md-select-value[@id="select_value_label_96"]'
    SERIES_VALUES = '//div[@id="select_container_127"]//md-option'
    MACHINE_TYPE = '//md-select-value[@id="select_value_label_97"]'
    MACHINE_TYPE_VALUES = '//div[@id="select_container_129"]//md-option'
    ADD_GPUS_CHECKBOX = '//md-checkbox[@aria-label="Add GPUs"]'
    GPUS_TYPE = '//md-select[@aria-label="GPU type"]'
    GPUS_TYPE_VALUES = '//div[@id="select_container_510"]//md-option'
    NUMBER_OF_GPUS = '//md-select[@id="select_511"]'
    NUMBER_OF_GPUS_VALUES = '//div[@id="select_container_512"]//md-option'
    SSD = '//md-select[@id="select_468"]'
    SSD_VALUES = '//div[@id="select_container_469"]//md-option'
    DATACENTER = '//md-select[@id="select_134"]'
    DATACENTER_VALUES = '//div[@id="select_container_135"]//md-option'
    COMMITTED_USAGE = '//md-select[@id="select_141"]'
    COMMITTED_USAGE_VALUES = '//div[@id="select_container_142"]//md-option'
    ESTIMATE_BTN = '//button[contains(text(),"Add to Estimate")]'
    EMAIL_ESTIMATE = '//button[@id="Email Estimate"]'
    EMAIL_FIELD = '//form[@name="emailForm"]//div[3]//input'
    SEND_EMAIL_BTN = '//button[contains(text(),"Send Email")]'

    # Assertions elements -------------------------------------------------------------------------------------------
    ESTIMATE_SUM = '//md-card-content[@id="resultBlock"]//h2[2]'
    ESTIMATE_INSTANCES = '//div[@aria-level="2"]//span'
    ESTIMATE_REGION = '//div[contains(text(), "Region:")]'
    ESTIMATE_HOURS = '//div[contains(text(), "total hours per month")]'
    ESTIMATE_TERM = '//div[contains(text(), "Commitment term:")]'
    ESTIMATE_PROV_MODEL = '//div[contains(text(), "Provisioning model:")]'
    ESTIMATE_INSTANCE_TYPE = '//div[contains(text(), "Instance type:")]'
    ESTIMATE_BINDING_SUMS = '//div[@class="ng-binding"]'
    ESTIMATE_OS_SOFTWARE = (
        '//div[contains(text(), "Operating System / Software:")]//span'
    )
    ESTIMATE_SSD = '//div[contains(text(), "Local SSD:")]'
    ESTIMATE_TOTAL = "//h2/b"


    # Email page elements --------------------------------------------------------------------------------------------
    EMAIL = '//span[@id="email"]'
    MAIL_URL = "https://www.minuteinbox.com/"
    LETTER = '//tbody//tr[1]//td[2][contains(text(),"Google Cloud Price Estimate")]'
    IFRAME = "iframeMail"
    SPAM_MAIN_IFRAME = "aswift_3"
    SPAM_NEXT_IFRAME = "ad_iframe"
    SPAM_CLOSE_BTN = "//div[@id='dismiss-button']"
    SUM = "//td[2]//h3"


    def __init__(self):
        super().__init__()


    # Methods that add additional info string in logs about start/end of testing this module. ------------------------    
    def start(self):
        text = "TESTING GOOGLE CALCULATOR UI"
        LOG.warning(f"{text:.^75}")


    def end(self):
        text = "SUCCESSFUL END OF TESTING - GOOGLE CALCULATOR UI"
        LOG.warning(f"{text:.^75}")


    ####### SEARCH CALCULATOR ----------------------------------------------------------------------------------------
    def go_to(self, url):
        return super().go_to(url)


    def get_search_field(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.SEARCH_FIELD)


    def click_on_search_field(self):
        self.get_search_field().click()


    def enter_search_value(self, searched_value):
        self.get_search_field().send_keys(searched_value)
        self.wait_until_text_to_be_present_in_element_value(By.XPATH, self.SEARCH_FIELD, searched_value)
        self.get_search_field().send_keys(Keys.ENTER)


    def find_calculator(self, searched_value):
        self.click_on_search_field()
        self.enter_search_value(searched_value)
        LOG.debug("Search google cloud calculator.")


    ####### OPEN CALCULATOR FROM SEARCH RESULTS METHODS --------------------------------------------------------------
    def get_search_result(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.SEARCH_RESULT)
    

    def click_on_search_result(self):
        self.get_search_result().click()
        LOG.debug("Select needed search result.")

    
    ###### WORK WITH CALCUCATOR METHODS ------------------------------------------------------------------------------
    # Iframe handling ------------------------------------------------------------------------------------------------
    def switch_to_frame(self, iframe):
        self.driver.switch_to.frame(iframe)


    def enter_both_iframes(self, ext_iframe, int_iframe):
        self.switch_to_frame(ext_iframe)
        LOG.debug("Enter into external  calc iframe.")
        self.switch_to_frame(int_iframe)
        LOG.debug("Enter into inner calc iframe.")


    def get_out_of_frames(self):
        self.driver.switch_to.default_content()


    #  Compute engine ------------------------------------------------------------------------------------------------
    def get_compute_engine_btn(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.COMPUTE_ENGINE_BTN)


    def click_on_compute_engine_btn(self):
        self.get_compute_engine_btn().click()
        LOG.debug("Click on the Compute Engine btn.")


    # Instances ------------------------------------------------------------------------------------------------------
    def get_instances(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.INSTANCES)


    def set_instances_value(self, value):
        self.get_instances().click()
        self.get_instances().send_keys(value)
        LOG.debug("Enter instances value.")


    # OS/Software ----------------------------------------------------------------------------------------------------
    def get_os_software(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.OSSOFTWARE__DD)


    def set_os_software(self, os_software):
        self.get_os_software().click()
        os_software_list = self.wait_for_presence_of_all_elements(By.XPATH, self.OS_SOFTWARE_VALUES)
        AdditionalFunctions.select_item_from_list(os_software_list, os_software)
        LOG.debug("Select Operating System/Software.")


    # Series ---------------------------------------------------------------------------------------------------------
    def get_series(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.SERIES)


    def set_series(self, series):
        self.get_series().click()
        series_list = self.wait_for_presence_of_all_elements(By.XPATH, self.SERIES_VALUES)
        AdditionalFunctions.select_item_from_list(series_list, series)
        LOG.debug("Select Series.")


    # Machine Type ---------------------------------------------------------------------------------------------------
    def get_machine_type(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.MACHINE_TYPE)


    def set_machine_type(self, machine_type):
        self.get_machine_type().click()
        machine_types_list = self.wait_for_presence_of_all_elements(By.XPATH, self.MACHINE_TYPE_VALUES)
        AdditionalFunctions.select_item_from_list(machine_types_list, machine_type)
        LOG.debug("Select Machine type.")


    # GPUs -----------------------------------------------------------------------------------------------------------
    def get_add_gpus_checkbox(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.ADD_GPUS_CHECKBOX)


    def get_gpus_type_select(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.GPUS_TYPE)


    def get_gpus_type_values(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GPUS_TYPE_VALUES)


    def get_gpus_num_select(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.NUMBER_OF_GPUS)


    def get_gpus_num_values(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.NUMBER_OF_GPUS_VALUES)


    def add_gpus_config(self, gpus_type, num_gpus):
        self.get_add_gpus_checkbox().click()
        LOG.debug("Turn on GPUs checkbox.")

        self.get_gpus_type_select().click()
        gpus_type_list = self.get_gpus_type_values()
        AdditionalFunctions.select_item_from_list(gpus_type_list, gpus_type)
        LOG.debug("Select GPUs type.")

        self.get_gpus_num_select().click()
        num_gpus_list = self.get_gpus_num_values()
        AdditionalFunctions.select_item_from_list(num_gpus_list, num_gpus)
        LOG.debug("Select GPUs number.")


    # SSD ------------------------------------------------------------------------------------------------------------
    def get_ssd(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.SSD)


    def get_ssd_values(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SSD_VALUES)


    def ssd_config(self, num_ssd):
        self.get_ssd().click()
        ssd_conf_list = self.get_ssd_values()
        AdditionalFunctions.select_item_from_list(ssd_conf_list, num_ssd)
        LOG.debug("Select SSD number.")


    # Datacenter -----------------------------------------------------------------------------------------------------
    def get_datacenter(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.DATACENTER)


    def get_datacenter_values(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.DATACENTER_VALUES)


    def datacenter_config(self, location):
        self.get_datacenter().click()
        dc_conf_list = self.get_datacenter_values()
        AdditionalFunctions.select_item_from_list(dc_conf_list, location)
        LOG.debug("Select Datacenter location.")


    # Commited usage -------------------------------------------------------------------------------------------------
    def get_com_usage(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.COMMITTED_USAGE)


    def get_com_usage_values(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.COMMITTED_USAGE_VALUES)


    def com_usage_config(self, com_usage):
        self.get_com_usage().click()
        com_usage_list = self.get_com_usage_values()
        AdditionalFunctions.select_item_from_list(com_usage_list, com_usage)
        LOG.debug("Select Committed usage.")


    # Estimate btn ---------------------------------------------------------------------------------------------------
    def get_estimate(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.ESTIMATE_BTN)


    def estimate_btn_click(self):
        self.get_estimate().click()
        LOG.debug("Click on Estimate btn.")


    # Filling the form with previous methods (WITHOUT SENDING EMAIL) ------------------------------------------------
    def fill_the_calc_form(
        self,
        instances,
        os_software,
        series,
        machine_type,
        gpus_type,
        num_gpus,
        num_ssd,
        location,
        com_usage,
    ):
        self.enter_both_iframes(self.EXTERNAL_IFRAME, self.INNER_IFRAME)
        self.click_on_compute_engine_btn()
        self.set_instances_value(instances)
        self.set_os_software(os_software)
        self.set_series(series)
        self.set_machine_type(machine_type)
        self.add_gpus_config(gpus_type, num_gpus)
        self.ssd_config(num_ssd)
        self.datacenter_config(location)
        self.com_usage_config(com_usage)
        self.estimate_btn_click()


    # Email estimate -------------------------------------------------------------------------------------------------
    def get_email_estimate_btn(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.EMAIL_ESTIMATE)


    def email_estimate_btn_click(self):
        self.get_email_estimate_btn().click()
        LOG.debug("Click on Email estimate.")


    # Email field ----------------------------------------------------------------------------------------------------
    def get_email_field(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.EMAIL_FIELD)


    def set_email_field(self, email):
        self.get_email_field().click()
        self.get_email_field().send_keys(email)
        LOG.debug("Set Email field value.")


    # Send email btn -------------------------------------------------------------------------------------------------
    def get_send_email_btn(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.SEND_EMAIL_BTN)


    def send_email_btn_click(self):
        self.get_send_email_btn().click()
        LOG.debug("Click on Send Email btn.")


    # Send email with the cost calculation ---------------------------------------------------------------------------
    def send_email(self, email):
        self.enter_both_iframes(self.EXTERNAL_IFRAME, self.INNER_IFRAME)
        self.set_email_field(email)
        self.send_email_btn_click()
        LOG.debug("Email successfuly send.")


    # CALC ASSERTIONS METHODS ---------------------------------------------------------------------------------------------
    def get_page_title(self):
        title = self.driver.title
        LOG.info("Get page title for assertion.")
        
        return title


    def get_estimate_sum(self):
        sum = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_SUM)
        LOG.info("Get sum for assertion.")
        
        return sum.text[0:8]


    def get_estimate_instances(self):
        instances = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_INSTANCES)
        LOG.info("Get instances for assertion.")
        
        return instances.text


    def get_estimate_os_software(self):
        os_soft = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_OS_SOFTWARE)
        LOG.info("Get os/software for assertion.")
        
        return os_soft.text


    def get_estimate_instance_type(self):
        instance_type = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_INSTANCE_TYPE)
        LOG.info("Get instances type for assertion.")
        
        return instance_type.text


    def get_estimate_ssd(self):
        ssd = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_SSD)
        LOG.info("Get SSD for assertion.")
        
        return ssd.text
    

    def get_estimate_region(self):
        region = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_REGION)
        LOG.info("Get region for assertion.")
        
        return region.text


    def get_estimate_term(self):
        term = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_TERM)
        LOG.info("Get term for assertion.")
        
        return term.text
    

    def get_estimate_hours(self):
        hours = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_HOURS)
        LOG.info("Get hours for assertion.")
        
        return hours.text


    def get_estimate_prov_model(self):
        prov_model = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_PROV_MODEL)
        LOG.info("Get provision model for assertion.")
        
        return prov_model.text


    def get_estimate_binding_sums(self):
        binding_sums = self.wait_for_presence_of_all_elements(By.XPATH, self.ESTIMATE_BINDING_SUMS)
        LOG.info("Get binding sums for assertion.")
        
        return binding_sums[0].text


    def get_estimate_total(self):
        total = self.wait_until_presence_of_element_located(By.XPATH, self.ESTIMATE_TOTAL)
        LOG.info("Get estimate total for assertion.")
        
        return total
    

    ###### EMAIL PAGE METHODS ---------------------------------------------------------------------------------------
    # Page ----------------------------------------------------------------------------------------------------------
    def open_mail_page(self):
        self.driver.execute_script(f"""window.open("{self.MAIL_URL}","_blank");""")


    def get_email_address(self):
        email_field = self.wait_until_presence_of_element_located(By.XPATH, self.EMAIL)
        
        return email_field.text


    def copy_email_address(self):
        self.wait_until_next_page_open()
        email = self.get_email_address()
        LOG.debug("Copy email.")
        
        return email


    # Letter --------------------------------------------------------------------------------------------------------
    def get_letter(self):
        return self.wait_until_presence_of_element_located(By.XPATH, self.LETTER)


    def letter_click(self):
        self.get_letter().click()
        LOG.debug("Click on letter.")


    def open_letter(self):
        self.letter_click()
        LOG.debug("Letter is opened.")


    # Window handling ------------------------------------------------------------------------------------------------
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    

    def get_window_handles(self):
        return self.driver.window_handles
    

    def switch_window(self, window):
        return self.driver.switch_to.window(window)
    

    # Iframe handling ------------------------------------------------------------------------------------------------
    def enter_letter_iframe(self, iframe):
        self.switch_to_frame(iframe)
        LOG.debug("Enter into letter iframe.")


    # Spam handling -------------------------------------------------------------------------------------------------- 
    def spam_box_close(self):
        return self.wait_until_element_is_clicable(By.XPATH, self.SPAM_CLOSE_BTN)
    

    def spam_close(self):
        self.switch_to_frame(self.SPAM_MAIN_IFRAME)
        LOG.debug("Enter into external mail iframe.")
        self.switch_to_frame(self.SPAM_NEXT_IFRAME)
        LOG.debug("Enter into inner mail iframe.")
        self.spam_box_close().click()
        self.get_out_of_frames()
        LOG.debug("Spam closed.")


    # Sum ------------------------------------------------------------------------------------------------------------
    def get_sum(self):
        sum = self.wait_until_presence_of_element_located(By.XPATH, self.SUM)
        LOG.info("Get sum to assert.")
        
        return sum.text

    def get_sum_in_letter(self):
        self.enter_letter_iframe(self.IFRAME)
        
        return self.get_sum()
    

