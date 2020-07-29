import requests


# Exercise 2.1
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Extract the JSON body from the response
# Assert that the response body contains an element called 'firstname'
def test_get_booking_with_id_1_check_firstname_element_exists():
    response = requests.get('https://restful-booker.herokuapp.com/booking/1')
    response_body = response.json()
    assert 'firstname' in response_body


# Exercise 2.2
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Extract the JSON body from the response
# Assert that the value of the response body element 'lastname' is 'Brown'
def test_get_booking_with_id_1_check_lastname_equals_brown():
    response = requests.get('https://restful-booker.herokuapp.com/booking/1')
    response_body = response.json()
    assert response_body['lastname'] == 'Brown'


# Exercise 2.3
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Extract the JSON body from the response
# Assert that the value of the response body element 'totalprice' is an integer
def test_get_booking_with_id_1_check_totalprice_is_integer():
    response = requests.get('https://restful-booker.herokuapp.com/booking/1')
    response_body = response.json()
    assert isinstance(response_body['totalprice'], int)


# Exercise 2.4
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Extract the JSON body from the response
# Assert that the response body element 'bookingdates' has both a 'checkin'
# and a 'checkout' child element
def test_get_booking_with_id_1_check_bookingdates_has_checking_and_checkout_dates():
    response = requests.get('https://restful-booker.herokuapp.com/booking/1')
    response_body = response.json()
    assert 'checkin' in response_body['bookingdates']
    assert 'checkout' in response_body['bookingdates']


# Exercise 2.5
# Perform a GET call to https://restful-booker.herokuapp.com/booking
# Extract the JSON body from the response
# Assert that the list of booking IDs contains more than 3 elements
def test_get_all_bookings_check_number_of_bookings_larger_than_3():
    response = requests.get('https://restful-booker.herokuapp.com/booking')
    response_body = response.json()
    assert len(response_body) > 3
