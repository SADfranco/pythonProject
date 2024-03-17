import requests
from jsonschema import validators
#from configuration import SERVICE_URL
#from src.schema.post import POST_SCHEMA



def test_getting_post():
    response = requests.get(url='https://my-json-server.typicode.com/typicode/demo/posts')
    recieved_post = response.json()
    assert response.status_code == 200
    assert len(response.json()) == 3