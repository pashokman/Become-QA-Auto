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
    def auth(self, auth_data):
        request = requests.post(f"{Restbooker.MAIN_URL}/auth", json=auth_data)

        assert request.status_code == 200
        self.log.debug("Auth successful.")

        body = request.json()
        return body["token"]
        

    def create_booking(self, new_booking):
        request = requests.post(f"{Restbooker.MAIN_URL}/booking", json=new_booking)

        assert request.status_code == 200
        self.log.debug("Create booking successful.")

        body = request.json()
        return body
    

    def get_booking(self, booking_id, status_code):
        request = requests.get(f"{Restbooker.MAIN_URL}/booking/{booking_id}")

        assert request.status_code == status_code
        self.log.debug("Get booking successful.")
        if status_code == 200:
            body = request.json()
            return body
    

    def update_booking(self, token, booking_id, update_booking_data):
        request = requests.put(f"{Restbooker.MAIN_URL}/booking/{booking_id}", 
                               json=update_booking_data, 
                               headers={"Cookie": f"token={token}"})

        assert request.status_code == 200
        self.log.debug("Update booking successful.")

        body = request.json()
        return body
    

    def delete_booking(self, token, request_body):
        booking_id = request_body['bookingid']

        request = requests.delete(f"{Restbooker.MAIN_URL}/booking/{booking_id}", 
                               headers={"Cookie": f"token={token}"})

        assert request.status_code == 201
        self.log.debug("Delete booking successful.")
    

        # Assertions
    def auth_assertion(self, auth_data):
        token = self.auth(auth_data)
        
        assert len(token) != 0


    def create_booking_assertion(self, new_booking, request_body):
        expected_result = {}
        expected_result["booking"] = new_booking
        
        id = request_body['bookingid']
        expected_result["bookingid"] = id     

        assert expected_result == request_body
        self.log.info("Created booking object is equal to expected booking object.")


    def get_booking_assertion(self, new_booking, request_body):
        expected_result = new_booking

        assert expected_result == request_body
        self.log.info("Getted booking object is equal to expected booking object.")


    def update_booking_assertion(self, update_booking_data, request_body):
        assert update_booking_data == request_body
        self.log.info("Updated booking object is equal to expected booking object.")


    def delete_booking_assertion(self, request_body, status_code):
        self.get_booking(request_body["bookingid"], status_code)