import requests
from utils.logger import Loger

class Restbooker:
    log = Loger.custom_logger()

    MAIN_URL = "https://restful-booker.herokuapp.com"

    def start(self):
        text = "TESTING REQRES"
        self.log.critical(f"{text:.^75}")        

    def end(self):
        text = "SUCCESSFUL END OF TESTING - REQRES"
        self.log.critical(f"{text:.^75}")        


        # Steps to reproduce methods

    def auth(self):
        auth_data = {
            "username" : "admin",
            "password" : "password123"
        }
        request = requests.post(f"{Restbooker.MAIN_URL}/auth", json=auth_data)

        body = request.json()
        assert request.status_code == 200
        self.log.debug("Auth successful.")
        return body["token"]
        

    def create_booking(self, firstname: str, lastname: str, totalprice: int, depositpaid: bool, 
                       checkin: str, checkout: str, additionalneeds: str):

        new_booking = {
            "firstname" : f"{firstname}",
            "lastname" : f"{lastname}",
            "totalprice" : totalprice,
            "depositpaid" : depositpaid,
            "bookingdates" : {
                "checkin" : f"{checkin}",
                "checkout" : f"{checkout}"
            },
            "additionalneeds" : f"{additionalneeds}"
        }

        request = requests.post(f"{Restbooker.MAIN_URL}/booking", json=new_booking)

        body = request.json()
        assert request.status_code == 200
        self.log.debug("Create booking successful.")

        return body
    



        # Assertions
    def auth_assertion(self):
        token = self.auth()
        
        assert len(token) != 0


    def create_booking_assertion(self, firstname: str, lastname: str, totalprice: int, depositpaid: bool, 
                            checkin: str, checkout: str, additionalneeds: str, request_body):
        
        id = request_body['bookingid']

        expected_booking_object = {
            "bookingid": id,
            "booking": {
                "firstname" : f"{firstname}",
                "lastname" : f"{lastname}",
                "totalprice" : totalprice,
                "depositpaid" : depositpaid,
                "bookingdates" : {
                    "checkin" : f"{checkin}",
                    "checkout" : f"{checkout}"
                },
                "additionalneeds" : f"{additionalneeds}"
            }
        }     

        assert request_body == expected_booking_object
        self.log.info("Created booking object is equal to expected booking object.")
