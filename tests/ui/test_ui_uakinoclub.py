import pytest
import logging
from utils.logger import Loger


log = Loger.custom_logger(log_level=logging.INFO)


@pytest.mark.personal_ui
def test_start():
    text = "Testing personal_ui"
    log.critical(f"{text:.^75}")


@pytest.mark.personal_ui
def test_search_non_existing_movie_message(uakinoclub):
    uakinoclub.search_some_movie("Dragon Heat")

    uakinoclub.movie_message_assertion("UAKINO.CLUB » Пошук за фразою Dragon Heat, знайдено: 0 результатів")


@pytest.mark.personal_ui
def test_search_existing_movie_message(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")

    uakinoclub.movie_message_assertion(
        "UAKINO.CLUB » Пошук за фразою the fast and the furious, знайдено: 3 результатів"
    )


@pytest.mark.personal_ui
def test_search_results_count_validation(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")

    uakinoclub.result_movie_count_assertion(3)


@pytest.mark.personal_ui
def test_first_search_result_validation(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    uakinoclub.open_first_result_movie()

    uakinoclub.movie_name_assertion("The Fast and the Furious")


@pytest.mark.personal_ui
def test_first_searched_result_relative_movies(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    uakinoclub.open_first_result_movie()

    uakinoclub.first_movie_relatives_assertion()


@pytest.mark.personal_ui
def test_second_related_movie_year(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    uakinoclub.open_first_result_movie()
    years_list = uakinoclub.save_relative_movies_years()
    uakinoclub.open_relative_movie(2)

    uakinoclub.movie_year_assertion(years_list[1], "(2003 рік)")


@pytest.mark.personal_ui
def test_third_related_movie_year(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    uakinoclub.open_first_result_movie()
    years_list = uakinoclub.save_relative_movies_years()
    uakinoclub.open_relative_movie(3)

    uakinoclub.movie_year_assertion(years_list[2], "(2006 рік)")


@pytest.mark.personal_ui
def test_end():
    text = "SUCCESSFUL END OF TESTING - personal_ui tests"
    log.critical(f"{text:.^75}")
