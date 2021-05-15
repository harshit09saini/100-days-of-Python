class FlightData:
    #This class is responsible for structuring the flight data.
    def structure_flight_data(self, flight):
        flight_dict = {
            "cityFrom": flight["cityFrom"],
            "cityTo": flight["cityTo"],
            "price": flight["conversion"]["INR"],
            "flyFrom": flight["route"][0]["flyFrom"],
            "flyTo": flight["route"][0]["flyTo"],
            "departureDate": flight["route"][0]["local_departure"].split("T")[0],
            "returnDate": flight["route"][1]["local_departure"].split("T")[0]
        }
        return flight_dict

