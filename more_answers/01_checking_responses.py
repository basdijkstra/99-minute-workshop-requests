import requests


# Exercise E.1
# Perform a GET call to http://api.zippopotam.us/us/90210
# Assert that the response status code is equal to 200
def test_get_data_for_us_zip_90210_check_status_code_expect_200():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.status_code == 200


# Exercise E.2
# Perform a GET call to http://api.zippopotam.us/us/99999
# Assert that the response status code is equal to 404
def test_get_data_for_us_zip_99999_check_status_code_expect_404():
    response = requests.get('http://api.zippopotam.us/us/99999')
    assert response.status_code == 404


# Exercise E.3
# Perform a GET call to http://api.zippopotam.us/us/90210
# Assert that the response header 'Content-Type' exists
def test_get_data_for_us_zip_90210_check_content_type_exists_expect_true():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert 'Content-Type' in response.headers


# Exercise E.4
# Perform a GET call to http://api.zippopotam.us/us/90210
# Assert that the response header 'Content-Type' has value 'application/json; charset=utf-8'
def test_get_data_for_us_zip_90210_check_content_type_expect_application_json():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.headers['Content-Type'] == 'application/json'


# Exercise E.5
# Perform a GET call to http://api.zippopotam.us/us/90210
# Assert that the response header 'Server' has value 'cloudflare'
def test_get_data_for_us_zip_90210_check_connection_expect_keep_alive():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.headers['Server'] == 'cloudflare'
