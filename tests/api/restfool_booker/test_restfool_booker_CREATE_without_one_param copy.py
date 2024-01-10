""" 
Here I learned how to:
    - add additional conditions into page methods to return status code if it does not match to input status code;
    - import test date from another file;
    - I solved problem vs copy (use deepcopy), to change only copied dictionary, not original one;
    - made test of creating booking without body parameters;
    - add error messages into variable,
    - add try/except blocks.
"""

import copy
import pytest
import test_objects.restfool_booker as rb

    
# Test objects (data) ------------------------------------------------------------------------------------------------
NEW_BOOKING_DATA = rb.NEW_BOOKING_DATA

WITHOUT_MANDATORY_PARAM_STATUS_CODE = 500
WITHOUT_ADDITIONAL_PARAM_STATUS_CODE = 200


# Tests without one parameter ------------------------------------------------------------------------------------------
@pytest.mark.restfool_booker_api2
def test_start(restbooker):
    """Method adds additional info string in logs about start of testing this module."""
    restbooker.start()


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_firstname(restbooker):
    """Test booking creation without the firstname."""
    try:
        DATA = copy.deepcopy(NEW_BOOKING_DATA)
        del DATA['firstname']

        new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

        err_message = f"There is another status code error - {new_booking_response}"
        assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_lastname(restbooker):
    """Test booking creation without the lastname."""
    try:
        DATA = copy.deepcopy(NEW_BOOKING_DATA)
        del DATA['lastname']

        new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

        err_message = f"There is another status code error - {new_booking_response}"
        assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_totalprice(restbooker):
    """Test booking creation without the totalprice."""
    try:
        DATA = copy.deepcopy(NEW_BOOKING_DATA)
        del DATA['totalprice']

        new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

        err_message = f"There is another status code error - {new_booking_response}"
        assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_depositpaid(restbooker):
    """Test booking creation without the depositpaid."""
    try:
        DATA = copy.deepcopy(NEW_BOOKING_DATA)
        del DATA['depositpaid']

        new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

        err_message = f"There is another status code error - {new_booking_response}"
        assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_booking(restbooker):
    """Test booking creation without the booking."""
    try:
        DATA = copy.deepcopy(NEW_BOOKING_DATA)
        del DATA['bookingdates']

        new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

        err_message = f"There is another status code error - {new_booking_response}"
        assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_booking_dates_checkin(restbooker):
    """Test booking creation without the booking dates checkin."""
    try:
        DATA = copy.deepcopy(NEW_BOOKING_DATA)
        del DATA['bookingdates']['checkin']

        new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

        err_message = f"There is another status code error - {new_booking_response}"
        assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_booking_dates_checkout(restbooker):
    """Test booking creation without the booking dates checkout."""
    try:
        DATA = copy.deepcopy(NEW_BOOKING_DATA)
        del DATA['bookingdates']['checkout']

        new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

        err_message = f"There is another status code error - {new_booking_response}"
        assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_additionalneeds(restbooker):
    """Test booking creation without the booking dates additionalneeds."""
    try:
        DATA = copy.deepcopy(NEW_BOOKING_DATA)
        del DATA['additionalneeds']

        new_booking_response = restbooker.create_booking(DATA, WITHOUT_ADDITIONAL_PARAM_STATUS_CODE)

        expected_result = {}
        expected_result["booking"] = DATA
        id = new_booking_response['bookingid']
        expected_result["bookingid"] = id     

        err_message = f"There is another status code error - {new_booking_response}"
        assert expected_result == new_booking_response, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


# Tests with another datatype of one of the parameters -----------------------------------------------------------------
@pytest.mark.restfool_booker_api2
def test_booking_updating_enother_type_additionalneeds(restbooker):
    """Test booking updating with integer value of additionalneeds parameter."""
    try:
        DATA = copy.deepcopy(NEW_BOOKING_DATA)
        DATA['additionalneeds'] = 123456

        new_booking_response = restbooker.create_booking(DATA, WITHOUT_ADDITIONAL_PARAM_STATUS_CODE)

        expected_result = {}
        expected_result["booking"] = DATA
        id = new_booking_response['bookingid']
        expected_result["bookingid"] = id     

        err_message = f"There is another status code error - {new_booking_response}"
        assert expected_result == new_booking_response, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api2
def test_end(restbooker):
    """Method adds additional info string in logs about end of testing this module."""
    restbooker.end()
