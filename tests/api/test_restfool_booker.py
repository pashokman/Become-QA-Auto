import pytest


@pytest.mark.restbooker
def test_start(restbooker):
    restbooker.start()


@pytest.mark.restbooker
def test_auth(restbooker):
    restbooker.auth_assertion()


@pytest.mark.restbooker
def test_booking_creation(restbooker):
    new_booking = restbooker.create_booking("Lester", "Tester", 12000, True, "2023-11-11", "2023-11-12", "two bathrooms")

    restbooker.create_booking_assertion("Lester", "Tester", 12000, True, "2023-11-11", "2023-11-12", "two bathrooms", new_booking)


@pytest.mark.restbooker
def test_booking_getting(restbooker):
    new_booking = restbooker.create_booking("Lester", "Tester", 12000, True, "2023-11-11", "2023-11-12", "two bathrooms")
    get_booking = restbooker.get_booking(new_booking["bookingid"], 200)

    restbooker.get_booking_assertion("Lester", "Tester", 12000, True, "2023-11-11", "2023-11-12", "two bathrooms", get_booking)


@pytest.mark.restbooker
def test_booking_updating(restbooker):
    token = restbooker.auth()
    new_booking = restbooker.create_booking("Lester", "Tester", 12000, True, "2023-11-11", "2023-11-12", "two bathrooms")
    update_booking = restbooker.update_booking(token, new_booking["bookingid"], 
                                               "Toster", "Rester", 5000, False, "2023-11-12", "2023-11-13", "additional key")

    restbooker.update_booking_assertion("Toster", "Rester", 5000, False, "2023-11-12", "2023-11-13", "additional key", update_booking)
    
    get_booking = restbooker.get_booking(new_booking["bookingid"], 200)
    restbooker.get_booking_assertion("Toster", "Rester", 5000, False, "2023-11-12", "2023-11-13", "additional key", get_booking)


@pytest.mark.restbooker
def test_booking_deleting(restbooker):
    token = restbooker.auth()
    new_booking = restbooker.create_booking("Lester", "Tester", 12000, True, "2023-11-11", "2023-11-12", "two bathrooms")

    restbooker.delete_booking(token, new_booking)
    restbooker.delete_booking_assertion(new_booking, 404)


@pytest.mark.restbooker
def test_end(restbooker):
    restbooker.end()