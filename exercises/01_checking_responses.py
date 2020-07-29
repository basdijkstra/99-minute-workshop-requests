import requests


# Exercise 1.1
# Perform a GET call to https://restful-booker.herokuapp.com/ping
# Assert that the response status code is equal to 201
def test_get_ping_check_status_code_expect_200():
    pass


# Exercise 1.2
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Assert that the response status code is equal to 200
def test_get_booking_1_check_status_code_expect_200():
    pass


# Exercise 1.3
# Perform a GET call to https://restful-booker.herokuapp.com/booking/999
# Assert that the response status code is equal to 404
def test_get_booking_999_check_status_code_expect_404():
    pass


# Exercise 1.4
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Assert that the response header 'Content-Type' exists
def test_get_booking_1_check_content_type_exists_expect_true():
    pass


# Exercise 1.5
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Assert that the response header 'Content-Type' has value 'application/json; charset=utf-8'
def test_get_booking_1_check_content_type_expect_application_json():
    pass


# Exercise 1.6
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Assert that the response encoding is equal to 'utf-8'
def test_get_booking_1_check_encoding_expect_utf8():
    pass


# Exercise 1.7
# Perform a GET call to https://restful-booker.herokuapp.com/booking/1
# Assert that the response header 'Connection' has value 'keep-alive'
def test_get_booking_1_check_connection_expect_keep_alive():
    pass
