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


# Tests --------------------------------------------------------------------------------------------------------------
@pytest.mark.restfool_booker_api5
def test_start(restbooker):
    """Method adds additional info string in logs about start of testing this module."""
    restbooker.start()


@pytest.mark.restfool_booker_api5
def test_booking_deleting_non_existing_object(restbooker):
    """Try to delete non existing object."""
    try:
        token = restbooker.auth(AUTH_DATA)
        result = restbooker.delete_booking(token, 999999, 405)

        err_message = "There is some problem with booking deleting"
        assert result == 405, err_message
    except Exception as e:
        pytest.fail(f"Test failed. Error: {str(e)}")


@pytest.mark.restfool_booker_api5
def test_end(restbooker):
    """Method adds additional info string in logs about end of testing this module."""
    restbooker.end()
