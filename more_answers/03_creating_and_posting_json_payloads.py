import requests

# Exercise 3.1
# Create a dict object new_order that has the following structure:
# {
#   "petId": 1,
#   "quantity": 1,
#   "shipDate": "2020-07-29T12:40:17.237Z",
#   "status": "placed",
#   "complete": False
# }
new_order = {
  "petId": 1,
  "quantity": 1,
  "shipDate": "2020-07-29T12:40:17.237Z",
  "status": "placed",
  "complete": False
}


# Exercise 3.2
# Perform a POST call to https://petstore.swagger.io/v2/store/order
# Pass the object created in exercise 3.1 as the JSON request payload
# Check that the response status code equals 200
def test_post_new_booking_from_object_check_status_code_equals_200():
    response = requests.post('https://petstore.swagger.io/v2/store/order', json=new_order)
    assert response.status_code == 200


# Exercise 3.3
# Create a method that:
# 1. Creates a copy of the new_order object
# 2. Updates the 'complete' element and sets it to True
# 3. Returns the updated order
def update_order_complete():
    updated_order = new_order
    updated_order['complete'] = True
    return updated_order


# Exercise 3.4
# Perform a POST call to https://petstore.swagger.io/v2/store/order
# Pass the object returned by the method created in exercise 3.3 as the JSON request payload
# Check that the response status code equals 200
def test_post_new_order_from_method_check_status_code_equals_200():
    response = requests.post('https://petstore.swagger.io/v2/store/order', json=update_order_complete())
    assert response.status_code == 200


# Exercise 3.5 (extra)
# Extend exercise 3.4 with the following steps:
# 1. Extract the value of the 'id' element in the response and store it in a variable
# 2. Perform a GET call to https://petstore.swagger.io/v2/store/order/<your_order_id>
# 3. Check that the value of the 'complete' response body element is equal to True
def test_post_new_order_from_method_check_status_code_equals_200_extended():
    response_post = requests.post('https://petstore.swagger.io/v2/store/order', json=update_order_complete())
    response_post_body = response_post.json()
    order_id = response_post_body['id']
    response_get = requests.get(f'https://petstore.swagger.io/v2/store/order/{order_id}')
    response_get_body = response_get.json()
    assert response_get_body['complete'] is True
