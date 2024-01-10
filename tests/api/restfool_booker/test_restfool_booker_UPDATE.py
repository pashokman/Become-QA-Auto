""" 
Here I learned how to:
    - test CRUD operetions through API;
    - used prepeared objects for testing;
    - how to add logs. 
"""

import copy
import pytest
import test_objects.restfool_booker as rb

    
# Test objects (data) ------------------------------------------------------------------------------------------------
AUTH_DATA = rb.AUTH_DATA
NEW_BOOKING_DATA = rb.NEW_BOOKING_DATA
UPDATE_BOOKING_DATA = rb.UPDATE_BOOKING_DATA

WITHOUT_MANDATORY_PARAM_STATUS_CODE = 400
WITHOUT_ADDITIONAL_PARAM_STATUS_CODE = 200


# Tests --------------------------------------------------------------------------------------------------------------
@pytest.mark.restfool_booker_api4
def test_start(restbooker):
    """Method adds additional info string in logs about start of testing this module."""
    restbooker.start()

# @pytest.mark.skip
@pytest.mark.restfool_booker_api4
def test_booking_updating_without_firstname(restbooker):
    """Test booking updating without the firstname."""
    try:
        DATA = copy.deepcopy(UPDATE_BOOKING_DATA)
        del DATA["firstname"]

        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        update_booking_response = restbooker.update_booking(token, 
                                                            new_booking_response["bookingid"], 
                                                            DATA, 
                                                            WITHOUT_MANDATORY_PARAM_STATUS_CODE)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        err_upd_message = "There is some problem with booking updating"
        assert update_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_upd_message    
        err_get_message = "There is some problem with booking getting after updating"
        assert get_booking_response == NEW_BOOKING_DATA, err_get_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api4
def test_booking_updating_without_lastname(restbooker):
    """Test booking updating without the lastname."""
    try:
        DATA = copy.deepcopy(UPDATE_BOOKING_DATA)
        del DATA["lastname"]

        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        update_booking_response = restbooker.update_booking(token, 
                                                            new_booking_response["bookingid"], 
                                                            DATA, 
                                                            WITHOUT_MANDATORY_PARAM_STATUS_CODE)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        err_upd_message = "There is some problem with booking updating"
        assert update_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_upd_message    
        err_get_message = "There is some problem with booking getting after updating"
        assert get_booking_response == NEW_BOOKING_DATA, err_get_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api4
def test_booking_updating_without_totalprice(restbooker):
    """Test booking updating without the totalprice."""
    try:
        DATA = copy.deepcopy(UPDATE_BOOKING_DATA)
        del DATA["totalprice"]

        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        update_booking_response = restbooker.update_booking(token, 
                                                            new_booking_response["bookingid"], 
                                                            DATA, 
                                                            WITHOUT_MANDATORY_PARAM_STATUS_CODE)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        err_upd_message = "There is some problem with booking updating"
        assert update_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_upd_message    
        err_get_message = "There is some problem with booking getting after updating"
        assert get_booking_response == NEW_BOOKING_DATA, err_get_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api4
def test_booking_updating_without_depositpaid(restbooker):
    """Test booking updating without the depositpaid."""
    try:
        DATA = copy.deepcopy(UPDATE_BOOKING_DATA)
        del DATA["depositpaid"]

        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        update_booking_response = restbooker.update_booking(token, 
                                                            new_booking_response["bookingid"], 
                                                            DATA, 
                                                            WITHOUT_MANDATORY_PARAM_STATUS_CODE)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        err_upd_message = "There is some problem with booking updating"
        assert update_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_upd_message    
        err_get_message = "There is some problem with booking getting after updating"
        assert get_booking_response == NEW_BOOKING_DATA, err_get_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api4
def test_booking_updating_without_bookingdates(restbooker):
    """Test booking updating without the bookingdates."""
    try:
        DATA = copy.deepcopy(UPDATE_BOOKING_DATA)
        del DATA["bookingdates"]

        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        update_booking_response = restbooker.update_booking(token, 
                                                            new_booking_response["bookingid"], 
                                                            DATA, 
                                                            WITHOUT_MANDATORY_PARAM_STATUS_CODE)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        err_upd_message = "There is some problem with booking updating"
        assert update_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_upd_message    
        err_get_message = "There is some problem with booking getting after updating"
        assert get_booking_response == NEW_BOOKING_DATA, err_get_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api4
def test_booking_updating_without_bookingdates_checkin(restbooker):
    """Test booking updating without the bookingdates checkin."""
    try:
        DATA = copy.deepcopy(UPDATE_BOOKING_DATA)
        del DATA["bookingdates"]["checkin"]

        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        update_booking_response = restbooker.update_booking(token, 
                                                            new_booking_response["bookingid"], 
                                                            DATA, 
                                                            WITHOUT_MANDATORY_PARAM_STATUS_CODE)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        err_upd_message = "There is some problem with booking updating"
        assert update_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_upd_message    
        err_get_message = "There is some problem with booking getting after updating"
        assert get_booking_response == NEW_BOOKING_DATA, err_get_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api4
def test_booking_updating_without_bookingdates_checkout(restbooker):
    """Test booking updating without the bookingdates checkout."""
    try:
        DATA = copy.deepcopy(UPDATE_BOOKING_DATA)
        del DATA["bookingdates"]["checkout"]

        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        update_booking_response = restbooker.update_booking(token, 
                                                            new_booking_response["bookingid"], 
                                                            DATA, 
                                                            WITHOUT_MANDATORY_PARAM_STATUS_CODE)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        err_upd_message = "There is some problem with booking updating"
        assert update_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_upd_message    
        err_get_message = "There is some problem with booking getting after updating"
        assert get_booking_response == NEW_BOOKING_DATA, err_get_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api4
def test_booking_updating_without_additionalneeds(restbooker):
    """Test booking updating without the additionalneeds."""
    try:
        DATA = copy.deepcopy(UPDATE_BOOKING_DATA)
        del DATA["additionalneeds"]
        ADDITIONALNEEDS = NEW_BOOKING_DATA["additionalneeds"]

        token = restbooker.auth(AUTH_DATA)
        new_booking_response = restbooker.create_booking(NEW_BOOKING_DATA, 200)
        update_booking_response = restbooker.update_booking(token, 
                                                            new_booking_response["bookingid"], 
                                                            DATA, 
                                                            WITHOUT_ADDITIONAL_PARAM_STATUS_CODE)
        get_booking_response = restbooker.get_booking(new_booking_response["bookingid"], 200)

        DATA["additionalneeds"]  = ADDITIONALNEEDS
        err_upd_message = "There is some problem with booking updating"
        assert update_booking_response == DATA, err_upd_message    
        err_get_message = "There is some problem with booking getting after updating"
        assert get_booking_response == DATA, err_get_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api4
def test_end(restbooker):
    """Method adds additional info string in logs about end of testing this module."""
    restbooker.end()
