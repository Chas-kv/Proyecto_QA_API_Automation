def test_get_all_posts(posts_api):
    response = posts_api.get_all_posts()
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_post(posts_api):
    response = posts_api.get_post_by_id(1)
    assert response.status_code == 200

    post = response.json()

    assert post["id"] == 1
    assert isinstance(post["title"], str)