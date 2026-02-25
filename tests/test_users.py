import requests




def test_get_users_status_code(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200


def test_get_users_response_structure(base_url):
    response = requests.get(f"{base_url}/users")
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


def test_single_user_by_id(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200

    user = response.json()

    assert user["id"] == 1
    assert isinstance(user["name"], str)
    assert "@" in user["email"]
    
def test_user_not_found(base_url):
    response = requests.get(f"{base_url}/users/9999")
    
    # JSONPlaceholder devuelve objeto vacío {}
    assert response.status_code == 404 or response.json() == {}
    
def test_create_user(base_url):
    new_user = {
        "name": "Kevin Test",
        "username": "kevtest",
        "email": "kevin@test.com"
    }

    response = requests.post(f"{base_url}/users", json=new_user)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == new_user["name"]
    assert data["username"] == new_user["username"]
    assert data["email"] == new_user["email"]