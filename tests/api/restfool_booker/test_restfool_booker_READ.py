""" 
Here I learned how to:
    - added test to check status code when there is no booking with such id. 
"""

import pytest

    
# Test objects (data) ------------------------------------------------------------------------------------------------
OBJECT_DOES_NOT_EXIST_ID = 999999
OBJECT_DOES_NOT_EXIST_STATUS_CODE = 404


# Tests --------------------------------------------------------------------------------------------------------------
@pytest.mark.restfool_booker_api3
def test_start(restbooker):
    """Method adds additional info string in logs about start of testing this module."""
    restbooker.start()


@pytest.mark.restfool_booker_api3
def test_booking_getting(restbooker):
    try:
        get_booking_response = restbooker.get_booking(OBJECT_DOES_NOT_EXIST_ID, OBJECT_DOES_NOT_EXIST_STATUS_CODE)

        err_message = f"There is another status code error - {get_booking_response}"
        assert get_booking_response == OBJECT_DOES_NOT_EXIST_STATUS_CODE, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api3
def test_end(restbooker):
    """Method adds additional info string in logs about end of testing this module."""
    restbooker.end()
