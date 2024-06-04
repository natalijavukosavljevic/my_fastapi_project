import requests

# These requests work:
requested = requests.get("http://127.0.0.1:8000").json()

def test_home_page():
    return_value={"message": "Hello, World!"}
    assert return_value == requested


