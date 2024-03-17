from jsonschema import validate
import requests


POST_SCHEMA = {
    "type": "array",
    "items":{
        "type": "object",
        "properties": {
                    "id": {"type": "number"},
                    "title": {"type": "string"},

                        }
    },
    #"required": ["id", "title" , "name"]
}


response = requests.get(url='https://my-json-server.typicode.com/typicode/demo/posts')

recieved_post = [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
print(recieved_post)
    #assert response.status_code == 200
    #assert len(response.json()) == 3

validate(recieved_post, POST_SCHEMA)