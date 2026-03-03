import requests


class PostsAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_posts(self):
        return requests.get(f"{self.base_url}/posts")

    def get_post_by_id(self, post_id):
        return requests.get(f"{self.base_url}/posts/{post_id}")