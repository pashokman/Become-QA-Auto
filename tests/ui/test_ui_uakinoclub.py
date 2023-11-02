import pytest
from modules.ui.page_objects.uakinoclub_page import UAKinoClubPage
import logging
from utils.logger import Loger


log = Loger.custom_logger(log_level=logging.INFO)

log.critical("      ---     Testing personal_ui     ---     ")

@pytest.mark.skip()
@pytest.mark.personal_ui
def test_search_non_existing_movie_message():
    page = UAKinoClubPage()
    page.search_some_movie("Dragon Heat")
    
    page.movie_message_assertion("UAKINO.CLUB » Пошук за фразою Dragon Heat, знайдено: 0 результатів")


@pytest.mark.skip()
@pytest.mark.personal_ui
def test_search_existing_movie_message():
    page = UAKinoClubPage()
    page.search_some_movie("the fast and the furious")
    
    page.movie_message_assertion("UAKINO.CLUB » Пошук за фразою the fast and the furious, знайдено: 3 результатів")


@pytest.mark.skip()
@pytest.mark.personal_ui 
def test_search_results_count_validation():
    page = UAKinoClubPage()
    page.search_some_movie('the fast and the furious')

    page.result_movie_count_assertion(3)


@pytest.mark.skip()
@pytest.mark.personal_ui
def test_first_search_result_validation():
    page = UAKinoClubPage()
    page.search_some_movie('the fast and the furious')
    page.open_first_result_movie()

    page.movie_name_assertion("The Fast and the Furious")


@pytest.mark.skip()
@pytest.mark.personal_ui
def test_first_searched_result_relative_movies():
    page = UAKinoClubPage()
    page.search_some_movie('the fast and the furious')
    page.open_first_result_movie()

    page.first_movie_relatives_assertion()
    
    
@pytest.mark.skip()
@pytest.mark.personal_ui
def test_second_related_movie_year():
    page = UAKinoClubPage()
    page.search_some_movie('the fast and the furious')
    page.open_first_result_movie()
    years_list = page.save_relative_movies_years()
    page.open_relative_movie(2)
    
    page.movie_year_assertion(years_list[1], "(2003 рік)")


# @pytest.mark.skip()
@pytest.mark.personal_ui
def test_third_related_movie_year():
    page = UAKinoClubPage()
    page.search_some_movie('the fast and the furious')
    page.open_first_result_movie()
    years_list = page.save_relative_movies_years()
    page.open_relative_movie(3)
    
    page.movie_year_assertion(years_list[2], "(2006 рік)")

log.critical("      ---     SUCCESSFUL END OF TESTING - personal_ui tests     ---     ")
