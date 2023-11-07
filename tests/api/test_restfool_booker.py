import pytest

    # Test objects
auth_data = {
    "username" : "admin",
    "password" : "password123"
}

new_booking_data = {
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

update_booking_data = {
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
    restbooker.auth_assertion(auth_data)


@pytest.mark.restbooker
def test_booking_creating(restbooker):
    new_booking_response = restbooker.create_booking(new_booking_data)

    restbooker.create_booking_assertion(new_booking_data, new_booking_response)


@pytest.mark.restbooker
def test_booking_getting(restbooker):
    new_booking = restbooker.create_booking(new_booking_data)
    get_booking = restbooker.get_booking(new_booking["bookingid"], 200)

    restbooker.get_booking_assertion(new_booking_data, get_booking)


@pytest.mark.restbooker
def test_booking_updating(restbooker):
    token = restbooker.auth(auth_data)
    new_booking = restbooker.create_booking(new_booking_data)
    update_booking = restbooker.update_booking(token, new_booking["bookingid"], update_booking_data)

    restbooker.update_booking_assertion(update_booking_data, update_booking)
    
    get_booking = restbooker.get_booking(new_booking["bookingid"], 200)
    restbooker.get_booking_assertion(update_booking_data, get_booking)


@pytest.mark.restbooker
def test_booking_deleting(restbooker):
    token = restbooker.auth(auth_data)
    new_booking = restbooker.create_booking(new_booking_data)

    restbooker.delete_booking(token, new_booking)
    restbooker.delete_booking_assertion(new_booking, 404)


@pytest.mark.restbooker
def test_end(restbooker):
    restbooker.end()
