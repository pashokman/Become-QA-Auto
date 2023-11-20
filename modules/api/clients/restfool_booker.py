import requests
from utils.logger import Loger


LOG = Loger.custom_logger()


class RestBooker():
    
    MAIN_URL = "https://restful-booker.herokuapp.com"
    
    # Methods that add additional info string in logs about start/end of testing this module. ------------------------
    def start(self):
        text = "TESTING REQRES"
        LOG.critical(f"{text:.^75}")        


    def end(self):
        text = "SUCCESSFUL END OF TESTING - REQRES"
        LOG.critical(f"{text:.^75}")        


    # Steps to reproduce methods -------------------------------------------------------------------------------------
    def auth(self, auth_data):
        request = requests.post(f"{RestBooker.MAIN_URL}/auth", json=auth_data)

        assert request.status_code == 200
        LOG.debug("Auth successful.")

        body = request.json()
        return body["token"]
        

    def create_booking(self, new_booking):
        request = requests.post(f"{RestBooker.MAIN_URL}/booking", json=new_booking)

        assert request.status_code == 200
        LOG.debug("Create booking successful.")

        body = request.json()
        return body
    

    def get_booking(self, booking_id, status_code):
        request = requests.get(f"{RestBooker.MAIN_URL}/booking/{booking_id}")

        assert request.status_code == status_code
        LOG.debug("Get booking successful.")
        
        if status_code == 200:
            body = request.json()
            return body
    

    def update_booking(self, token, booking_id, update_booking_data):
        request = requests.put(f"{RestBooker.MAIN_URL}/booking/{booking_id}", 
                                json=update_booking_data, 
                                headers={"Cookie": f"token={token}"})

        assert request.status_code == 200
        LOG.debug("Update booking successful.")

        body = request.json()
        return body
    

    def delete_booking(self, token, request_body):
        booking_id = request_body['bookingid']

        request = requests.delete(f"{RestBooker.MAIN_URL}/booking/{booking_id}", 
                                    headers={"Cookie": f"token={token}"})

        assert request.status_code == 201
        LOG.debug("Delete booking successful.")
