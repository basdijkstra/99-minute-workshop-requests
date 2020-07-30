import requests


# Exercise 2.1
# Perform a GET call to https://restful-booker.herokuapp.com/booking/7
# Extract the JSON body from the response
# Assert that the response body contains an element called 'firstname'
def test_get_booking_with_id_7_check_firstname_element_exists():
    pass


# Exercise 2.2
# Perform a GET call to https://restful-booker.herokuapp.com/booking/7
# Extract the JSON body from the response
# Assert that the value of the response body element 'additionalneeds' is 'Breakfast'
def test_get_booking_with_id_7_check_additionalneeds_equals_breakfast():
    pass


# Exercise 2.3
# Perform a GET call to https://restful-booker.herokuapp.com/booking/7
# Extract the JSON body from the response
# Assert that the value of the response body element 'totalprice' is an integer
def test_get_booking_with_id_7_check_totalprice_is_integer():
    pass


# Exercise 2.4
# Perform a GET call to https://restful-booker.herokuapp.com/booking/7
# Extract the JSON body from the response
# Assert that the response body element 'bookingdates' has both a 'checkin'
# and a 'checkout' child element
def test_get_booking_with_id_7_check_bookingdates_has_checkin_and_checkout_dates():
    pass


# Exercise 2.5
# Perform a GET call to https://restful-booker.herokuapp.com/booking
# Extract the JSON body from the response
# Assert that the list of booking IDs contains more than 3 elements
def test_get_all_bookings_check_number_of_bookings_larger_than_3():
    pass
