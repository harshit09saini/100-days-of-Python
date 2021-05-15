import requests

SHEETY_ENDPOINT = "https://api.sheety.co/cbc529d238ca12e3e1d04ea9697cdd09/flightDeals/prices"
SHEETY_ENDPOINT_USERS = "https://api.sheety.co/cbc529d238ca12e3e1d04ea9697cdd09/flightDeals/users"

header = {
    "Authorization": "Bearer flightdealsappauthentication",
    "Content-Type": "application/json"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_sheet_data(self):
        self.sheet_response = requests.get(url=SHEETY_ENDPOINT, headers=header)
        self.sheet_response.raise_for_status()
        self.sheet_data = self.sheet_response.json()
        self.destination_data = self.sheet_data["prices"]

        return self.destination_data

    def update_sheet_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            self.response_put = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(self.response_put.text)

    def get_emails(self):
        self.sheet_response = requests.get(url=SHEETY_ENDPOINT_USERS, headers=header)
        self.sheet_response.raise_for_status()
        self.sheet_data = self.sheet_response.json()["users"]
        return self.sheet_data