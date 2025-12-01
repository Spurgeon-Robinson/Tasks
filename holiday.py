# This code calculates the total cost of a holiday trip including flight,
# hotel, and car rental.
# Asks user for input on destination city, number of nights, and rental days.
city_flight = input("What city are you flying to? Cape Town,"
                    " Durban, or Johannesburg? ")
if city_flight.lower() != "cape town" and \
        city_flight.lower() != "durban" and \
        city_flight.lower() != "johannesburg":
    print("Invalid city. Please enter Cape Town, Durban, or Johannesburg.")
    exit()
num_nights = input("How many nights will you be staying? ")
if not num_nights.isdigit() or int(num_nights) <= 0:
    print("Invalid number of nights. Please enter a positive integer.")
    exit()
rental_days = input("How many days will you be renting a car? ")
if not rental_days.isdigit() or int(rental_days) <= 0:
    print("Invalid number of rental days. Please enter a positive integer.")
    exit()

# This function calculates the cost of a hotel stay
# based on the number of nights.


def hotel_cost(num_nights):
    """
    Calculate the cost of hotel stay based on the number of nights.

    Parameters:
    num_nights (int): The number of nights to stay.

    Returns:
    int: The total cost of the hotel stay.
    """
    return num_nights * 140


# This function calculates the cost of a flight
# based on the city to which the flight is booked.


def plane_cost(city_flights):
    """
    Calculate the cost of a flight based on the city.

    Parameters:
    city_flights (str): The city to which the flight is booked.

    Returns:
    int: The cost of the flight.
    """

    if city_flights.lower() == "cape town":
        return 900
    elif city_flights.lower() == "durban":
        return 1050
    elif city_flights.lower() == "johannesburg":
        return 1150
    else:
        return 0  # Return 0 if the city is not recognized


# This function calculates the cost of car rental
# based on the number of days the car is rented.


def car_rental(rental_days):
    """
    Calculate the cost of car rental
    based on the number of days.

    Parameters:
    rental_days (int): The number of days to rent the car.

    Returns:
    int: The total cost of the car rental.
    """

    return rental_days * 330


# This function calculates the total cost of a holiday
# including flight, hotel, and car rental.


def holiday_cost(city_flight, num_nights, rental_days):
    """
    Calculate the total cost of a holiday including
    flight, hotel, and car rental.

    Parameters:
    city_flight (str): The city to which the flight is booked.
    num_nights (int): The number of nights for hotel stay.
    rental_days (int): The number of days for car rental.

    Returns:
    int: The total cost of the holiday.
    """

    return (
        plane_cost(city_flight) +
        hotel_cost(num_nights) +
        car_rental(rental_days)
    )


# Prints the costs of the flight, hotel, car rental, and total holiday cost.
print("The cost of the plane ticket is R" + str(plane_cost(city_flight)))
print("The cost of the hotel is R" + str(hotel_cost(int(num_nights))))
print("The cost of the car rental is R" + str(car_rental(int(rental_days))))
print("The total cost of the holiday is R" +
      str(holiday_cost(city_flight, int(num_nights), int(rental_days))))
