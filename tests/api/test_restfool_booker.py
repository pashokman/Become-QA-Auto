import pytest

@pytest.mark.restbooker
def test_start(restbooker):
    restbooker.start()


@pytest.mark.restbooker
def test_auth(restbooker):
    restbooker.auth_assertion()


@pytest.mark.restbooker
def test_user_creation(restbooker):
    booking = restbooker.create_booking("Lester", "Tester", 12000, True, "2023-11-11", "2023-11-12", "two bathrooms")

    restbooker.create_booking_assertion("Lester", "Tester", 12000, True, "2023-11-11", "2023-11-12", "two bathrooms", booking)


@pytest.mark.restbooker
def test_end(restbooker):
    restbooker.end()