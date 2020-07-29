import requests


# Exercise 2.1
# Perform a GET call to http://api.zippopotam.us/us/90210
# Extract the JSON body from the response
# Assert that the response body contains an element called 'country'
def test_get_data_for_us_zip_90210_check_country_element_exists():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert 'country' in response_body


# Exercise 2.2
# Perform a GET call to http://api.zippopotam.us/us/90210
# Extract the JSON body from the response
# Assert that the value of the response body element 'country' is 'United States'
def test_get_data_for_us_zip_90210_check_country_equals_united_states():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert response_body['country'] == 'United States'


# Exercise 2.3
# Perform a GET call to http://api.zippopotam.us/us/90210
# Extract the JSON body from the response
# Assert that the value of the response body element 'post code' is a string
def test_get_data_for_us_zip_90210_check_post_code_is_string():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert isinstance(response_body['post code'], str)


# Exercise 2.4
# Perform a GET call to http://api.zippopotam.us/us/90210
# Extract the JSON body from the response
# Assert that the first entry of the response body element 'places' has both a 'latitude'
# and a 'longitude' child element
def test_get_data_for_us_zip_90210_check_first_place_has_latitude_and_longitude():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert 'latitude' in response_body['places'][0]
    assert 'longitude' in response_body['places'][0]


# Exercise 2.5
# Perform a GET call to http://api.zippopotam.us/de/24848
# Extract the JSON body from the response
# Assert that the list of places contains exactly 4 elements
def test_get_data_for_de_zip_24848_check_number_of_places_equals_4():
    response = requests.get('http://api.zippopotam.us/de/24848')
    response_body = response.json()
    assert len(response_body['places']) == 4
