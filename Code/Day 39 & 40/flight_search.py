import requests
import datetime as dt
from flight_data import FlightData

FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
FLIGHT_API = ""
FLIGHT_LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

header = {
            "apikey": FLIGHT_API
        }

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flights = []


    def get_flights(self, flight_code):
        tomorrow = dt.datetime.today() + dt.timedelta(days=1)
        six_months_later = tomorrow + dt.timedelta(days=30 * 12)
        # print(flight_code)
        #
        # print(tomorrow.strftime("%d/%m/%Y"))
        # print(six_months_later.strftime("%d/%m/%Y"))
        self.parameters = {
            "fly_from": "DEL",
            "fly_to": flight_code,
            "date_from": str(tomorrow.strftime("%d/%m/%Y")),
            "date_to": str(six_months_later.strftime("%d/%m/%Y")),
            "flight-type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "INR",
            "one_for_city": 1,
            "max_stopovers": 0,
        }

        self.flight_response = requests.get(url=FLIGHT_ENDPOINT, params=self.parameters, headers=header)
        self.flight_response.raise_for_status()
        self.flight_response_data = self.flight_response.json()["data"]

        # print(self.flight_response_data)
        flight_data = FlightData()

        try:
            available_flight = flight_data.structure_flight_data(self.flight_response_data[0])
        except IndexError:
            print(f"No Flight Found for {flight_code}")
            return None

        # print(available_flight)
        # print(f"{available_flight['cityTo']} - ${available_flight['price']:,}")
        return available_flight


    def get_destination_codes(self, city_name):
        parameters = {
            "term": city_name
        }

        self.response = requests.get(url=FLIGHT_LOCATION_ENDPOINT, params=parameters, headers=header)
        self.response.raise_for_status()

        # print(self.response.json()["locations"][0]["code"])
        return self.response.json()["locations"][0]["code"]