import requests


class UsersAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_users(self):
        return requests.get(f"{self.base_url}/users")

    def get_user_by_id(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}")

    def create_user(self, user_data):
        return requests.post(f"{self.base_url}/users", json=user_data)