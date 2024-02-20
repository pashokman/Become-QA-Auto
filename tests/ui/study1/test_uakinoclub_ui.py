"""
Hear I learned:
    - how to work with multiple elements;
    - how to use DRY (don't repeat yourself) practise - method "search_some_movie";
    - add testing in different browsers
"""

import pytest
import allure


# Constants (input data and expected results data) -------------------------------------------------------------------
NONE_EXISTING_MOVIE_NAME = "Dragon Heat"
NONE_EXISTING_MOVIE_MESSAGE = "UAKINO.CLUB » Пошук за фразою Dragon Heat, знайдено: 0 результатів"

EXISTING_MOVIE_SEARCH_NAME = "the fast and the furious"
EXISTING_MOVIE_MESSAGE = "UAKINO.CLUB » Пошук за фразою the fast and the furious, знайдено: 3 результатів"

EXISTING_MOVIE_COUNT = 3

EXPECTED_SEARCHED_MOVIE_NAME = "The Fast and the Furious"

EXPECTED_RELATIVE_MOVIES = [
    'Форсаж', 'Подвійний Форсаж', 'Потрійний форсаж: Токійський дрифт', 
    'Бандити [передісторія Форсаж 4]', 'Форсаж 4', 'Форсаж 5: Пограбування в Ріо', 
    'Форсаж 6 [Розширена версія]', 'Форсаж 7 [Розширена версія]', 'Форсаж 8', 
    'Форсаж 9: Нестримна сага', 'Форсаж X'
    ]

EXPECTED_SECOND_RELATIVE_MOVIE_YEAR = "(2003 рік)"
EXPECTED_THIRD_RELATIVE_MOVIE_YEAR = "(2006 рік)"


# Tests --------------------------------------------------------------------------------------------------------------
# Method that add additional info string in logs about start of testing this module. ---------------------------------
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.uakinoclub_ui
def test_start(uakinoclub):
    uakinoclub.start()


@allure.severity(allure.severity_level.MINOR)
@pytest.mark.uakinoclub_ui
def test_non_existing_movie_search_message(uakinoclub):
    uakinoclub.search_some_movie(NONE_EXISTING_MOVIE_NAME)

    assert uakinoclub.get_movie_message() == NONE_EXISTING_MOVIE_MESSAGE, "Non existing movie message test error"


@allure.severity(allure.severity_level.MINOR)
@pytest.mark.uakinoclub_ui
def test_existing_movie_search_message(uakinoclub):
    uakinoclub.search_some_movie(EXISTING_MOVIE_SEARCH_NAME)
    
    assert uakinoclub.get_movie_message() == EXISTING_MOVIE_MESSAGE, "Existing movie meessage test error"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.uakinoclub_ui
def test_search_results_count_validation(uakinoclub):
    uakinoclub.search_some_movie(EXISTING_MOVIE_SEARCH_NAME)
    result_movie_count = uakinoclub.get_searched_movie_count()

    assert len(result_movie_count) == EXISTING_MOVIE_COUNT, "Search results count validation test error"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.uakinoclub_ui
def test_first_search_result_validation(uakinoclub):
    uakinoclub.search_some_movie(EXISTING_MOVIE_SEARCH_NAME)
    uakinoclub.open_first_result_movie()

    assert uakinoclub.get_movie_name() == EXPECTED_SEARCHED_MOVIE_NAME, "First search result validation test error"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.uakinoclub_ui
def test_first_searched_result_relative_movies(uakinoclub):
    uakinoclub.search_some_movie(EXISTING_MOVIE_SEARCH_NAME)
    uakinoclub.open_first_result_movie()

    assert uakinoclub.get_relative_movies() == EXPECTED_RELATIVE_MOVIES, "First search result relative movies test error"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.uakinoclub_ui
def test_second_related_movie_year(uakinoclub):
    uakinoclub.search_some_movie(EXISTING_MOVIE_SEARCH_NAME)
    uakinoclub.open_first_result_movie()
    years_list = uakinoclub.save_relative_movies_years()
    uakinoclub.open_relative_movie(2)

    assert years_list[1] == EXPECTED_SECOND_RELATIVE_MOVIE_YEAR, "Second related movie year test error"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.uakinoclub_ui
def test_third_related_movie_year(uakinoclub):
    uakinoclub.search_some_movie(EXISTING_MOVIE_SEARCH_NAME)
    uakinoclub.open_first_result_movie()
    years_list = uakinoclub.save_relative_movies_years()
    uakinoclub.open_relative_movie(3)

    assert years_list[2] == EXPECTED_THIRD_RELATIVE_MOVIE_YEAR, "Third related movie year test error"


# Method that add additional info string in logs about end of testing this module. -----------------------------------
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.uakinoclub_ui
def test_end(uakinoclub):
    uakinoclub.end()
