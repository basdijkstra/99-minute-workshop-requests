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
new_booking = {
    'firstname': 'Bas',
    'lastname': 'Dijkstra',
    'totalprice': 123,
    'depositpaid': False,
    'bookingdates': {
        'checkin': '2020-01-01',
        'checkout': '2020-01-31'
    },
    'additionalneeds': 'Breakfast'
}


# Exercise 3.2
# Perform a POST call to https://restful-booker.herokuapp.com/booking
# Pass the object created in exercise 3.1 as the JSON request payload
# Check that the response status code equals 200
def test_post_new_booking_from_object_check_status_code_equals_200():
    response = requests.post('https://restful-booker.herokuapp.com/booking', json=new_booking)
    assert response.status_code == 200


# Exercise 3.3
# Create a method that:
# 1. Creates a copy of the new_booking object
# 2. Updates the 'depositpaid' element and sets it to True
# 3. Returns the updated booking
def update_booking_deposit_paid():
    updated_booking = new_booking
    updated_booking['depositpaid'] = True
    return updated_booking


# Exercise 3.4
# Perform a POST call to https://restful-booker.herokuapp.com/booking
# Pass the object returned by the method created in exercise 3.3 as the JSON request payload
# Check that the response status code equals 200
def test_post_new_booking_from_method_check_status_code_equals_200():
    response = requests.post('https://restful-booker.herokuapp.com/booking', json=update_booking_deposit_paid())
    assert response.status_code == 200


# Exercise 3.5 (extra)
# Extend exercise 3.4 with the following steps:
# 1. Extract the value of the 'bookingid' element in the response and store it in a variable
# 2. Perform a GET call to https://restful-booker.herokuapp.com/booking/<your_booking_id>
# 3. Check that the value of the 'firstname' response body element is equal to the name you supplied
def test_post_new_booking_from_method_check_status_code_equals_200_extended():
    response_post = requests.post('https://restful-booker.herokuapp.com/booking', json=update_booking_deposit_paid())
    response_post_body = response_post.json()
    booking_id = response_post_body['bookingid']
    response_get = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
    response_get_body = response_get.json()
    assert response_get_body['firstname'] == 'Bas'
