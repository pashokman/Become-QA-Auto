""" 
Here I learned how to:
    - test CRUD operetions through API;
    - used prepeared objects for testing;
    - how to add logs. 
"""

import pytest

    
# Test objects ---------------------------------------------------------------------------------------------
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


# Tests ---------------------------------------------------------------------------------------------
# Method that add additional info string in logs about start of testing this module.
@pytest.mark.restfool_booker_api
def test_start(restbooker):
    restbooker.start()


@pytest.mark.restfool_booker_api
def test_auth(restbooker):
    token = restbooker.auth(AUTH_DATA)

    assert len(token) != 0


@pytest.mark.restfool_booker_api
def test_booking_creating(restbooker):
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA)

    expected_result = {}
    expected_result["booking"] = NEW_BOOKING_DATA
    id = new_booking_response['bookingid']
    expected_result["bookingid"] = id     

    assert expected_result == new_booking_response

    restbooker.log.info("Created booking object is equal to expected booking object.")


@pytest.mark.restfool_booker_api
def test_booking_getting(restbooker):
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA)
    get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

    assert get_booking_response == NEW_BOOKING_DATA

    restbooker.log.info("Getted booking object is equal to expected booking object.")


@pytest.mark.restfool_booker_api
def test_booking_updating(restbooker):
    token = restbooker.auth(AUTH_DATA)
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA)
    update_booking_response = restbooker.update_booking(token, new_booking_response["bookingid"], UPDATE_BOOKING_DATA)
    get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

    assert update_booking_response == UPDATE_BOOKING_DATA    
    assert get_booking_response == UPDATE_BOOKING_DATA

    restbooker.log.info("Updated booking object is equal to expected booking object.")


@pytest.mark.restfool_booker_api
def test_booking_deleting(restbooker):
    token = restbooker.auth(AUTH_DATA)
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA)
    restbooker.delete_booking(token, new_booking_response)
    get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 404)

    assert get_booking_response == None
    restbooker.log.info("Deleting of booking object is successful.")


# Method that add additional info string in logs about end of testing this module.
@pytest.mark.restfool_booker_api
def test_end(restbooker):
    restbooker.end()
