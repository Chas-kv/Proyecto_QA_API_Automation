import requests
import pytest




def test_get_users_status_code(users_api):
    response =  users_api.get_all_users()
    assert response.status_code == 200


def test_get_users_response_structure(users_api):
    response =  users_api.get_all_users()
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_user = data[0]

    required_keys = [
        "id",
        "name",
        "username",
        "email",
        "address",
        "phone",
        "website",
        "company"
    ]

    for key in required_keys:
        assert key in first_user


def test_single_user_by_id(users_api):
    response = users_api.get_user_by_id(1)
    assert response.status_code == 200

    user = response.json()

    assert user["id"] == 1
    assert isinstance(user["name"], str)
    assert "@" in user["email"]
    
def test_user_not_found(users_api):
    response =  users_api.get_user_by_id(9999)
    
    # JSONPlaceholder devuelve objeto vacío {}
    assert response.status_code == 404 or response.json() == {}
    
def test_create_user(users_api):
    new_user = {
        "name": "Kevin Test",
        "username": "kevtest",
        "email": "kevin@test.com"
    }

    response = users_api.create_user(new_user)


    assert response.status_code == 201

    data = response.json()

    assert data["name"] == new_user["name"]
    assert data["username"] == new_user["username"]
    assert data["email"] == new_user["email"]
    
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_multiple_users_exist(users_api, user_id):
    response =  users_api.get_user_by_id(user_id)
    
    assert response.status_code == 200
    
    user = response.json()
    
    assert user["id"] == user_id
    assert isinstance(user["username"], str)
    assert "@" in user["email"]