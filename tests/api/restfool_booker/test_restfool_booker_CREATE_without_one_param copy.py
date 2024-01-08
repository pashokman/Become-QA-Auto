""" 
Here I learned how to:
    - add additional conditions into page methods to return status code if it does not match to input status code;
    - import test date from another file;
    - I solved problem vs copy (use deepcopy), to change only copied dictionary, not original one;
    - made test of creating booking without body parameters;
    - add error messages into variable.
"""

import pytest
import test_objects.restfool_booker as rb
import copy

    
# Test objects (data) ------------------------------------------------------------------------------------------------
NEW_BOOKING_DATA = rb.NEW_BOOKING_DATA

WITHOUT_MANDATORY_PARAM_STATUS_CODE = 500
WITHOUT_ADDITIONAL_PARAM_STATUS_CODE = 200


# Tests --------------------------------------------------------------------------------------------------------------
# Method that add additional info string in logs about start of testing this module. ---------------------------------
@pytest.mark.restfool_booker_api2
def test_start(restbooker):
    restbooker.start()


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_firstname(restbooker):
    DATA = copy.deepcopy(NEW_BOOKING_DATA)
    del DATA['firstname']

    new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

    err_message = f"There is another status code error - {new_booking_response}"
    assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_lastname(restbooker):
    DATA = copy.deepcopy(NEW_BOOKING_DATA)
    del DATA['lastname']

    new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

    err_message = f"There is another status code error - {new_booking_response}"
    assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_totalprice(restbooker):
    DATA = copy.deepcopy(NEW_BOOKING_DATA)
    del DATA['totalprice']

    new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

    err_message = f"There is another status code error - {new_booking_response}"
    assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_depositpaid(restbooker):
    DATA = copy.deepcopy(NEW_BOOKING_DATA)
    del DATA['depositpaid']

    new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

    err_message = f"There is another status code error - {new_booking_response}"
    assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_booking_dates_checkin(restbooker):
    DATA = copy.deepcopy(NEW_BOOKING_DATA)
    del DATA['bookingdates']['checkin']

    new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

    err_message = f"There is another status code error - {new_booking_response}"
    assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_booking_dates_checkout(restbooker):
    DATA = copy.deepcopy(NEW_BOOKING_DATA)
    del DATA['bookingdates']['checkout']

    new_booking_response = restbooker.create_booking(DATA, WITHOUT_MANDATORY_PARAM_STATUS_CODE)

    err_message = f"There is another status code error - {new_booking_response}"
    assert new_booking_response == WITHOUT_MANDATORY_PARAM_STATUS_CODE, err_message


@pytest.mark.restfool_booker_api2
def test_booking_creating_without_additionalneeds(restbooker):
    DATA = copy.deepcopy(NEW_BOOKING_DATA)
    del DATA['additionalneeds']

    new_booking_response = restbooker.create_booking(DATA, WITHOUT_ADDITIONAL_PARAM_STATUS_CODE)

    expected_result = {}
    expected_result["booking"] = DATA
    id = new_booking_response['bookingid']
    expected_result["bookingid"] = id     

    err_message = f"There is another status code error - {new_booking_response}"
    assert expected_result == new_booking_response, err_message


# Method that add additional info string in logs about end of testing this module. -----------------------------------
@pytest.mark.restfool_booker_api2
def test_end(restbooker):
    restbooker.end()
