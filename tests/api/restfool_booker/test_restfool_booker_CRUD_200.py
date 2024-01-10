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
UPDATE_BOOKING_DATA = rb.UPDATE_BOOKING_DATA


# Tests --------------------------------------------------------------------------------------------------------------
@pytest.mark.restfool_booker_api
def test_start(restbooker):
    """Method adds additional info string in logs about start of testing this module."""
    restbooker.start()


@pytest.mark.restfool_booker_api
def test_auth(restbooker):
    """Successful test authorization method."""
    try:
        token = restbooker.auth(AUTH_DATA)

        err_message = "There is some problems with a token"
        assert len(token) != 0, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api
def test_booking_creating(restbooker):
    """Successful test of booking creation method."""
    try:
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)

        expected_result = {}
        expected_result["booking"] = NEW_BOOKING_DATA
        id = new_booking_response['bookingid']
        expected_result["bookingid"] = id     

        err_message = "There is some problem with booking creating"
        assert expected_result == new_booking_response, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api
def test_booking_getting(restbooker):
    """Successful test of booking getting method."""
    try:
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        err_message = "There is some problem with booking getting"
        assert get_booking_response == NEW_BOOKING_DATA, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api
def test_booking_updating(restbooker):
    """Successful test of booking updating method."""
    try:
        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        update_booking_response = restbooker.update_booking(token, new_booking_response["bookingid"], UPDATE_BOOKING_DATA, 200)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        err_upd_message = "There is some problem with booking updating"
        assert update_booking_response == UPDATE_BOOKING_DATA, err_upd_message    
        err_get_message = "There is some problem with booking getting after updating"
        assert get_booking_response == UPDATE_BOOKING_DATA, err_get_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api
def test_booking_deleting(restbooker):
    """Successful test of booking deleting method."""
    try:
        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        restbooker.delete_booking(token, new_booking_response['bookingid'], 201)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 404)

        err_message = "There is some problem with booking deleting"
        assert get_booking_response == 404, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api
def test_end(restbooker):
    """Method adds additional info string in logs about end of testing this module."""
    restbooker.end()
