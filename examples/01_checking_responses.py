import requests


def test_get_user_with_id_1_check_status_code_equals_200():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200


def test_get_user_with_id_99_check_status_code_equals_404():
    response = requests.get("https://jsonplaceholder.typicode.com/users/99")
    assert response.status_code == 404


def test_get_user_with_id_1_check_content_type_equals_json():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_get_user_with_id_1_check_encoding_equals_utf8():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.encoding == "utf-8"


def test_get_user_with_id_1_check_server_header_equals_cloudflare():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.headers['Server'] == 'cloudflare'
