import uuid

import requests

new_post = {
    'userId': 1,
    'title': 'My amazing new post title',
    'body': 'The quick brown fox jumps over the lazy dog'
}


def create_unique_new_post():
    modified_post = new_post
    modified_post['title'] = str(uuid.uuid4())
    print(f'Modified post title is {modified_post["title"]}')
    return modified_post


def test_post_new_post_from_object_check_status_code_equals_201():
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
    assert response.status_code == 201


def test_post_new_post_from_method_check_status_code_equals_201():
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=create_unique_new_post())
    assert response.status_code == 201
