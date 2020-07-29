import requests


# Exercise 2.1
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Extract the JSON body from the response
# Assert that the response body contains an element called 'firstname'
def test_get_booking_with_id_1_check_firstname_element_exists():
    pass


# Exercise 2.2
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Extract the JSON body from the response
# Assert that the value of the response body element 'lastname' is 'Brown'
def test_get_booking_with_id_1_check_lastname_equals_brown():
    pass


# Exercise 2.3
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Extract the JSON body from the response
# Assert that the value of the response body element 'totalprice' is an integer
def test_get_booking_with_id_1_check_totalprice_is_integer():
    pass


# Exercise 2.4
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Extract the JSON body from the response
# Assert that the response body element 'bookingdates' has both a 'checkin'
# and a 'checkout' child element
def test_get_booking_with_id_1_check_bookingdates_has_checking_and_checkout_dates():
    pass


# Exercise 2.5
# Perform a GET call to http://api.zippopotam.us/de/24848
# Extract the JSON body from the response
# Assert that the list of places contains exactly 4 elements
def test_get_data_for_de_zip_24848_check_number_of_places_equals_4():
    pass
