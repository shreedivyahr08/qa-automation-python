
import requests

BASE_URL = "https://petstore.swagger.io/v2"

#  test data
pet_id = 8889
pet_name = "Cat"


# 1. CREATE
def test_create_pet():

    url = BASE_URL + "/pet"

    data = {
        "id": pet_id,
        "name": pet_name,
        "status": "available"
    }

    response = requests.post(url, json=data)

    print("Create Response:", response.text)

    assert response.status_code == 200
    assert response.json()["id"] == pet_id
    assert response.json()["name"] == pet_name


# 2. READ 
def test_read_pet():

    url = BASE_URL + "/pet/" + str(pet_id)

    response = requests.get(url)

    print("Read Response:", response.text)

    assert response.status_code == 200
    assert response.json()["id"] == pet_id
    assert response.json()["name"] == pet_name


# 3. UPDATE 
def test_update_pet():

    url = BASE_URL + "/pet"

    updated_name = "Dog"

    data = {
        "id": pet_id,
        "name": updated_name,
        "status": "available"
    }

    response = requests.put(url, json=data)

    print("Update Response:", response.text)

    assert response.status_code == 200
    assert response.json()["name"] == updated_name


# 4. DELETE 
def test_delete_pet():

    url = BASE_URL + "/pet/" + str(pet_id)

    response = requests.delete(url)

    print("Delete Response:", response.text)

    assert response.status_code == 200

    # Verify pet is deleted
    response = requests.get(url)

    print("Get After Delete:", response.text)

    assert response.status_code == 404
