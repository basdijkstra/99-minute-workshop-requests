import requests


# Exercise 1.1
# Perform a GET call to https://restful-booker.herokuapp.com/ping
# Assert that the response status code is equal to 201
def test_get_ping_check_status_code_expect_200():
    response = requests.get('https://restful-booker.herokuapp.com/ping')
    assert response.status_code == 201


# Exercise 1.2
# Perform a GET call to https://restful-booker.herokuapp.com/booking/7
# Assert that the response status code is equal to 200
def test_get_booking_7_check_status_code_expect_200():
    response = requests.get('https://restful-booker.herokuapp.com/booking/7')
    assert response.status_code == 200


# Exercise 1.3
# Perform a GET call to https://restful-booker.herokuapp.com/booking/999
# Assert that the response status code is equal to 404
def test_get_booking_999_check_status_code_expect_404():
    response = requests.get('https://restful-booker.herokuapp.com/booking/999')
    assert response.status_code == 404


# Exercise 1.4
# Perform a GET call to https://restful-booker.herokuapp.com/booking/7
# Assert that the response header 'Content-Type' exists
def test_get_booking_7_check_content_type_exists_expect_true():
    response = requests.get('https://restful-booker.herokuapp.com/booking/7')
    assert 'Content-Type' in response.headers


# Exercise 1.5
# Perform a GET call to https://restful-booker.herokuapp.com/booking/7
# Assert that the response header 'Content-Type' has value 'application/json; charset=utf-8'
def test_get_booking_7_check_content_type_expect_application_json():
    response = requests.get('https://restful-booker.herokuapp.com/booking/7')
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'


# Exercise 1.6
# Perform a GET call to https://restful-booker.herokuapp.com/booking/7
# Assert that the response encoding is equal to 'utf-8'
def test_get_booking_7_check_encoding_expect_utf8():
    response = requests.get('https://restful-booker.herokuapp.com/booking/7')
    assert response.encoding == 'utf-8'


# Exercise 1.7
# Perform a GET call to https://restful-booker.herokuapp.com/booking/7
# Assert that the response header 'Connection' has value 'keep-alive'
def test_get_booking_7_check_connection_expect_keep_alive():
    response = requests.get('https://restful-booker.herokuapp.com/booking/7')
    assert response.headers['Connection'] == 'keep-alive'
