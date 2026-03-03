import pytest
from api.users_api import UsersAPI
from api.posts_api import PostsAPI

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def users_api(base_url):
    return UsersAPI(base_url)

@pytest.fixture
def posts_api(base_url):
    return PostsAPI(base_url)