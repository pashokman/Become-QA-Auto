import pytest

    # Test objects
AUTH_DATA = {
    "username" : "admin",
    "password" : "password123"
}

NEW_BOOKING_DATA = {
    "firstname" : "Lester",
    "lastname" : "Tester",
    "totalprice" : 12000,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-11-11",
        "checkout" : "2023-11-12"
    },
    "additionalneeds" : "two bathrooms"
}

UPDATE_BOOKING_DATA = {
    "firstname" : "Toster",
    "lastname" : "Rester",
    "totalprice" : 5000,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2023-11-12",
        "checkout" : "2023-11-13"
    },
    "additionalneeds" : "additional key"
}


    # Tests
@pytest.mark.restbooker
def test_start(restbooker):
    restbooker.start()


@pytest.mark.restbooker
def test_auth(restbooker):
    restbooker.auth_assertion(AUTH_DATA)


@pytest.mark.restbooker
def test_booking_creating(restbooker):
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA)

    restbooker.create_booking_assertion(NEW_BOOKING_DATA, new_booking_response)


@pytest.mark.restbooker
def test_booking_getting(restbooker):
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA)
    get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

    restbooker.get_booking_assertion(NEW_BOOKING_DATA, get_booking_response)


@pytest.mark.restbooker
def test_booking_updating(restbooker):
    token = restbooker.auth(AUTH_DATA)
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA)
    update_booking_response = restbooker.update_booking(token, new_booking_response["bookingid"], UPDATE_BOOKING_DATA)

    restbooker.update_booking_assertion(UPDATE_BOOKING_DATA, update_booking_response)
    
    get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)
    restbooker.get_booking_assertion(UPDATE_BOOKING_DATA, get_booking_response)


@pytest.mark.restbooker
def test_booking_deleting(restbooker):
    token = restbooker.auth(AUTH_DATA)
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA)

    restbooker.delete_booking(token, new_booking_response)
    restbooker.delete_booking_assertion(new_booking_response, 404)


@pytest.mark.restbooker
def test_end(restbooker):
    restbooker.end()
