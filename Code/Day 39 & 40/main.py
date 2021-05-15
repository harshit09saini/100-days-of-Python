# Flight Deal Tracker

# #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
flight_search = FlightSearch()
# flight_search.get_flights("BER")

data_manager = DataManager()

sheet_data = data_manager.get_sheet_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_codes(row["city"])
    print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_sheet_data()

users = data_manager.get_emails()
firstNames = [item['firstName'] for item in users]
lastNames = [item['lastName'] for item in users]
emails = [item['email'] for item in users]

for row in sheet_data:
    # print(row)
    flight = flight_search.get_flights(row["iataCode"])
    lowest_price = row["lowestPrice"]
    if flight is not None:
        if flight["price"] < lowest_price:
            notification_manager = NotificationManager()
            # notification_manager.send_message(flight)
            notification_manager.send_mail(
                flight=flight, fnames=firstNames, lnames=lastNames, emails=emails)
