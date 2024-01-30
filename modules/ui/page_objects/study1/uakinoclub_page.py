"""
Here I continue practise to work with elements selectors, 
saving multiple elements into a list and work with the list of these elements, 
adding logging,
making complex methods, like "search_some_movie" for a DRY (don't repeat yourself) practice in tests
"""

from modules.ui.page_objects.study1.base_page import BasePage
from utils.logger import Logger


logger_instance = Logger()
UA_KINOCLUB_LOG = logger_instance.get_logger()


class UAKinoClubPage(BasePage):
    MAIN_URL = 'https://uakino.club/'


    def __init__(self):
        super().__init__()


    # Methods that add additional info string in logs about start/end of testing this module. ------------------------    
    def start(self):
        text = "TESTING UAKINOCLUB_UI"
        UA_KINOCLUB_LOG.warning(f"{text:.^75}")


    def end(self):
        text = "SUCCESSFUL END OF TESTING - UAKINOCLUB_UI"
        UA_KINOCLUB_LOG.warning(f"{text:.^75}")


    # Steps to reproduce methods -------------------------------------------------------------------------------------
    def search_some_movie(self, movie_name):
        self.go_to(UAKinoClubPage.MAIN_URL)
        
        search_btn = self.find_element_by_id('show-search')
        search_btn.click()
        UA_KINOCLUB_LOG.debug("Open search field.")

        search_field = self.find_element_by_id('ajax_search')
        search_field.send_keys(f'{movie_name}')
        UA_KINOCLUB_LOG.debug(f"Enter searched value into search field - {movie_name}.")

        submit_search_btn = self.find_element_by_xpath("//button[contains(text(),'Знайти')]")
        submit_search_btn.click()
        UA_KINOCLUB_LOG.debug("Start searching.")


    def get_movie_message(self):
        return self.find_element_by_id("dle-speedbar").text
    

    def get_searched_movie_count(self):
        return self.find_elements_by_xpath("//div[@class='movie-item short-item']")
    

    def get_movie_name(self):
        return self.find_element_by_class("origintitle").text
    
    
    def get_relative_movies(self):
        movie_list_element = self.find_elements_by_xpath("//div[@class='rel-item']")[0]
        self.scroll_into_view(movie_list_element)        
        movie_list = self.find_elements_by_xpath("//div[@class='rel-item']//a")
        text_movie_list = []
        
        for i in range(len(movie_list)):
            text_movie_list.append(movie_list[i].text)
        
        UA_KINOCLUB_LOG.debug("Save relative movies into a list.")

        return text_movie_list


    def open_first_result_movie(self):
        first_movie = self.find_elements_by_xpath("//div[@class='movie-item short-item']")[0]
        self.scroll_into_view(first_movie)
        first_movie.click()
        UA_KINOCLUB_LOG.debug("Open first result movie.")


    def save_relative_movies_years(self):
        relative_movies_years = self.find_elements_by_xpath("//div[@class='rel-item']//div[@class='related-date']")
        text_relative_movies_years = []
        for i in range(len(relative_movies_years)):
            text_relative_movies_years.append(relative_movies_years[i].text)
        UA_KINOCLUB_LOG.debug("Save movie years into a list.")
        
        return text_relative_movies_years
    

    def open_relative_movie(self, number): #starts from 1
        movie = self.find_element_by_xpath(f"//div[@class='rel-item'][{number}]") # Подвійний форсаж
        movie.click()
        UA_KINOCLUB_LOG.debug(f"Open relative movie {number}.")
