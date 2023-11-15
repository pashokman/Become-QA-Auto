import pytest


@pytest.mark.uakino_club
def test_start(uakinoclub):
    uakinoclub.start()


@pytest.mark.skip
@pytest.mark.uakino_club
def test_non_existing_movie_search_message(uakinoclub):
    uakinoclub.search_some_movie("Dragon Heat")
    message = "UAKINO.CLUB » Пошук за фразою Dragon Heat, знайдено: 0 результатів"

    assert uakinoclub.get_movie_message() == message
    uakinoclub.log.info(f"! Successful ! Movie message is equal to needed value (not exist).")


@pytest.mark.skip
@pytest.mark.uakino_club
def test_existing_movie_search_message(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    message = "UAKINO.CLUB » Пошук за фразою the fast and the furious, знайдено: 3 результатів"

    assert uakinoclub.get_movie_message == message
    uakinoclub.log.info(f"! Successful ! Movie message is equal to needed value (exist).")

@pytest.mark.uakino_club
def test_search_results_count_validation(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    result_movie_count = uakinoclub.get_searched_movie_count()
    count = 3

    assert len(result_movie_count) == count
    uakinoclub.log.info(f"! Successful ! Result movies count is equal to needed value - {count}.")


@pytest.mark.skip
@pytest.mark.uakino_club
def test_first_search_result_validation(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    uakinoclub.open_first_result_movie()

    uakinoclub.movie_name_assertion("The Fast and the Furious")


@pytest.mark.skip
@pytest.mark.uakino_club
def test_first_searched_result_relative_movies(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    uakinoclub.open_first_result_movie()

    uakinoclub.first_movie_relatives_assertion()


@pytest.mark.skip
@pytest.mark.uakino_club
def test_second_related_movie_year(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    uakinoclub.open_first_result_movie()
    years_list = uakinoclub.save_relative_movies_years()
    uakinoclub.open_relative_movie(2)

    uakinoclub.movie_year_assertion(years_list[1], "(2003 рік)")


@pytest.mark.skip
@pytest.mark.uakino_club
def test_third_related_movie_year(uakinoclub):
    uakinoclub.search_some_movie("the fast and the furious")
    uakinoclub.open_first_result_movie()
    years_list = uakinoclub.save_relative_movies_years()
    uakinoclub.open_relative_movie(3)

    uakinoclub.movie_year_assertion(years_list[2], "(2006 рік)")


@pytest.mark.skip
@pytest.mark.uakino_club
def test_end(uakinoclub):
    uakinoclub.end()
