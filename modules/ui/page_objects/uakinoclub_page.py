from modules.ui.page_objects.base_page import BasePage
from utils.logger import Loger


class UAKinoClubPage(BasePage):
    log = Loger.custom_logger()

    MAIN_URL = 'https://uakino.club/'
    RELATIVE_MOVIES = [
        'Форсаж', 'Подвійний Форсаж', 'Потрійний форсаж: Токійський дрифт', 
        'Бандити [передісторія Форсаж 4]', 'Форсаж 4', 'Форсаж 5: Пограбування в Ріо', 
        'Форсаж 6 [Розширена версія]', 'Форсаж 7 [Розширена версія]', 'Форсаж 8', 
        'Форсаж 9: Нестримна сага', 'Форсаж X'
        ]

    def __init__(self):
        super().__init__()

    
    def start(self):
        text = "TESTING PERSONAL_UI"
        self.log.critical(f"{text:.^75}")

    def end(self):
        text = "SUCCESSFUL END OF TESTING - PERSONAL_UI"
        self.log.critical(f"{text:.^75}")


        # Steps to reproduce methods
    def search_some_movie(self, movie_name):
        self.go_to(UAKinoClubPage.MAIN_URL)
        
        search_btn = self.find_element_by_id('show-search')
        search_btn.click()
        self.log.debug("Open search field.")

        search_field = self.find_element_by_id('ajax_search')
        self.paste_value_into_field(search_field, movie_name)
        self.log.debug(f"Enter searched value into search field - {movie_name}.")

        submit_search_btn = self.find_element_by_xpath("//button[contains(text(),'Знайти')]")
        submit_search_btn.click()
        self.log.debug("Start searching.")

    def open_first_result_movie(self):
        first_movie = self.find_elements_by_xpath("//div[@class='movie-item short-item']")[0]
        self.scroll_into_view(first_movie)
        first_movie.click()
        self.log.debug("Open first result movie.")

    def save_relative_movies_years(self):
        relative_movies_years = self.find_elements_by_xpath("//div[@class='rel-item']//div[@class='related-date']")
        text_relative_movies_years = []
        for i in range(len(relative_movies_years)):
            text_relative_movies_years.append(relative_movies_years[i].text)
        self.log.debug("Save movie years into a list.")
        return text_relative_movies_years
    

    def open_relative_movie(self, number): #starts from 1
        movie = self.find_element_by_xpath(f"//div[@class='rel-item'][{number}]") # Подвійний форсаж
        movie.click()
        self.log.debug(f"Open relative movie {number}.")


        # Assertions
    def result_movie_count_assertion(self, count):
        result_movie_count = self.find_elements_by_xpath("//div[@class='movie-item short-item']")
        assert len(result_movie_count) == count
        self.log.info(f"! Successful ! Result movies count is equal to needed value - {count}.")

    def movie_name_assertion(self, name):
        movie_name = self.find_element_by_class("origintitle")
        assert movie_name.text == name
        self.log.info(f"! Successful ! Movie name is equal to needed value - {name}.")
        

    def first_movie_relatives_assertion(self):
        movie_list_element = self.find_elements_by_xpath("//div[@class='rel-item']")[0]
        self.scroll_into_view(movie_list_element)        
        movie_list = self.find_elements_by_xpath("//div[@class='rel-item']//a")
        text_movie_list = []
        for i in range(len(movie_list)):
            text_movie_list.append(movie_list[i].text)

        assert UAKinoClubPage.RELATIVE_MOVIES == text_movie_list
        self.log.info(f"! Successful ! Relative movie list is equal to needed value - {UAKinoClubPage.RELATIVE_MOVIES}.")
        
    def movie_year_assertion(self, year_from_list, year):
        assert year_from_list == year
        self.log.info(f"! Successful ! Movie year is equal to needed value - {year}.")

    def movie_message_assertion(self, message):
        result = self.find_element_by_id("dle-speedbar")

        assert result.text == message
        self.log.info(f"! Successful ! Movie message is equal to needed value - {message}.")