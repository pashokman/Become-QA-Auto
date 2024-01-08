""" 
Here I learned how to:
    - test CRUD operetions through API;
    - used prepeared objects for testing;
    - how to add logs. 
"""

import pytest
import test_objects.restfool_booker as rb

    
# Test objects (data) ------------------------------------------------------------------------------------------------
AUTH_DATA = rb.AUTH_DATA
NEW_BOOKING_DATA = rb.NEW_BOOKING_DATA
UPDATE_BOOKING_DATA = rb.NEW_BOOKING_DATA


# Tests --------------------------------------------------------------------------------------------------------------
# Method that add additional info string in logs about start of testing this module. ---------------------------------
@pytest.mark.restfool_booker_api
def test_start(restbooker):
    restbooker.start()


@pytest.mark.restfool_booker_api
def test_auth(restbooker):
    token = restbooker.auth(AUTH_DATA)

    assert len(token) != 0, "There is some problems with a token"


@pytest.mark.restfool_booker_api
def test_booking_creating(restbooker):
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)

    expected_result = {}
    expected_result["booking"] = NEW_BOOKING_DATA
    id = new_booking_response['bookingid']
    expected_result["bookingid"] = id     

    assert expected_result == new_booking_response, "There is some problem with booking creating"


@pytest.mark.restfool_booker_api
def test_booking_getting(restbooker):
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
    get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

    assert get_booking_response == NEW_BOOKING_DATA, "There is some problem with booking getting"


@pytest.mark.restfool_booker_api
def test_booking_updating(restbooker):
    token = restbooker.auth(AUTH_DATA)
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
    update_booking_response = restbooker.update_booking(token, new_booking_response["bookingid"], UPDATE_BOOKING_DATA)
    get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

    assert update_booking_response == UPDATE_BOOKING_DATA, "There is some problem with booking updating"    
    assert get_booking_response == UPDATE_BOOKING_DATA, "There is some problem with booking getting after updating"



@pytest.mark.restfool_booker_api
def test_booking_deleting(restbooker):
    token = restbooker.auth(AUTH_DATA)
    new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
    restbooker.delete_booking(token, new_booking_response)
    get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 404)

    assert get_booking_response == None, "There is some problem with booking deleting"


# Method that add additional info string in logs about end of testing this module. -----------------------------------
@pytest.mark.restfool_booker_api
def test_end(restbooker):
    restbooker.end()
