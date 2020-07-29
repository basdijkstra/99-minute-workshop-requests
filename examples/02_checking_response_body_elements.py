import requests


def test_get_user_with_id_1_check_name_element_exists():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    response_body = response.json()
    assert 'name' in response_body


def test_get_user_with_id_1_check_id_is_integer():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    response_body = response.json()
    assert isinstance(response_body['id'], int)


def test_get_user_with_id_1_check_name_equals_leanne_graham():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    response_body = response.json()
    assert response_body['name'] == 'Leanne Graham'


def test_get_user_with_id_1_check_company_name_equals_romaguera_crona():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    response_body = response.json()
    assert response_body['company']['name'] == 'Romaguera-Crona'


def test_get_all_users_check_number_of_users_equals_10():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    response_body = response.json()
    assert len(response_body) == 10
