import requests


# Exercise 2.1
# Perform a GET call to http://api.zippopotam.us/us/90210
# Extract the JSON body from the response
# Assert that the response body contains an element called 'country'
def test_get_data_for_us_zip_90210_check_country_element_exists():
    pass


# Exercise 2.2
# Perform a GET call to http://api.zippopotam.us/us/90210
# Extract the JSON body from the response
# Assert that the value of the response body element 'country' is 'United States'
def test_get_data_for_us_zip_90210_check_country_equals_united_states():
    pass


# Exercise 2.3
# Perform a GET call to http://api.zippopotam.us/us/90210
# Extract the JSON body from the response
# Assert that the value of the response body element 'post code' is a string
def test_get_data_for_us_zip_90210_check_post_code_is_string():
    pass


# Exercise 2.4
# Perform a GET call to http://api.zippopotam.us/us/90210
# Extract the JSON body from the response
# Assert that the first entry of the response body element 'places' has both a 'latitude'
# and a 'longitude' child element
def test_get_data_for_us_zip_90210_check_first_place_has_latitude_and_longitude():
    pass


# Exercise 2.4
# Perform a GET call to https://restful-booker.herokuapp.com/booking
# Extract the JSON body from the response
# Assert that the list of booking IDs contains more than 3 elements
def test_get_all_bookings_check_number_of_bookings_larger_than_3():
    response = requests.get('https://restful-booker.herokuapp.com/booking')
    response_body = response.json()
    assert len(response_body) > 3
