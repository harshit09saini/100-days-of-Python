# Data Entry Automation - Rental finder

from find_rentals import FindRentals
from save_data import SaveData

find_rentals = FindRentals()

find_rentals.find_rentals()

prices = find_rentals.price
addresses = find_rentals.address
links = find_rentals.links

save_data = SaveData(prices, addresses, links)