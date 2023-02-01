import os
import requests


def get_articles_count(author_id):
    BASE_URL = os.getenv("BASE_URL")
    response = requests.get(
        BASE_URL + f"/api/authors/{author_id}/event_get_articles_count/"
    ).json()
    return response.get("count")
