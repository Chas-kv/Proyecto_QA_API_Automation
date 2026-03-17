import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UsersAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_users(self):
        url = f"{self.base_url}/users"
        logger.info(f"GET Request -> {url}")
        
        response = requests.get(url)
        
        logger.info(f"Response Status Code: {response.status_code}")
        return response

    def get_user_by_id(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}")

    def create_user(self, user_data):
        return requests.post(f"{self.base_url}/users", json=user_data)