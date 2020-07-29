import requests

# Exercise 3.1
# Create a dict object new_booking that has the following structure:
# {
#     'firstname': '<your_first_name>',
#     'lastname': '<your_last_name>',
#     'totalprice': 123,
#     'depositpaid': False,
#     'bookingdates': {
#         'checkin': '<yyyy-mm-dd>',
#         'checkout': '<yyyy-mm-dd>'
#     },
#     'additionalneeds': 'Breakfast'
# }
new_booking = {}


# Exercise 3.2
# Perform a POST call to https://restful-booker.herokuapp.com/booking
# Pass the object created in exercise 3.1 as the JSON request payload
# Check that the response status code equals 200
def test_post_new_booking_from_object_check_status_code_equals_200():
    pass


# Exercise 3.3
# Create a method that:
# 1. Creates a copy of the new_booking object
# 2. Updates the 'depositpaid' element and sets it to True
# 3. Returns the updated booking
def update_booking_deposit_paid():
    pass


# Exercise 3.4
# Perform a POST call to https://restful-booker.herokuapp.com/booking
# Pass the object returned by the method created in exercise 3.3 as the JSON request payload
# Check that the response status code equals 200
def test_post_new_booking_from_method_check_status_code_equals_200():
    pass


# Exercise 3.5 (extra)
# Extend exercise 3.4 with the following steps:
# 1. Extract the value of the 'bookingid' element in the response and store it in a variable
# 2. Perform a GET call to https://restful-booker.herokuapp.com/booking/<your_booking_id>
# 3. Check that the value of the 'firstname' response body element is equal to the name you supplied
def test_post_new_booking_from_method_check_status_code_equals_200_extended():
    pass
