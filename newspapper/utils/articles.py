import os
import requests


def get_articles_by_api():
    BASE_URL = os.getenv("BASE_URL")
    articles_url = (
        BASE_URL
        + "/api/articles/?include=author%2Ctags&fields%5Barticle%5D=id,title,body,author,tags&fields%5Bauthor%5D=id,user&fields%5Btag%5D=name,id"
    )
    authors_url = (
        BASE_URL
        + "/api/authors/?include=user%2Carticles&fields%5Bauthor%5D=id,user&fields%5Buser%5D=first_name,id,last_name"
    )
    articles_response = requests.get(articles_url).json()
    authors_response = requests.get(authors_url).json()

    authors_list = {
        author["id"]: author["relationships"]["user"]["data"]["id"]
        for author in authors_response["data"]
    }

    users = {
        user["id"]: {
            "user": {
                "first_name": user["attributes"].get("first_name"),
                "last_name": user["attributes"].get("last_name"),
            }
        }
        for user in authors_response["included"]
    }

    tags = {
        item["id"]: {"name": item["attributes"].get("name")}
        for item in articles_response["included"]
        if item["type"] == "tag"
    }

    articles = [
        {
            "id": item["id"],
            "title": item["attributes"]["title"],
            "body": item["attributes"]["body"],
            "author": users[
                authors_list[item["relationships"]["author"]["data"]["id"]]
            ],
            "tags": [
                tags[tag.get("id")]
                for tag in item.get("relationships").get("tags").get("data")
            ],
        }
        for item in articles_response["data"]
    ]

    count = requests.get(BASE_URL + "/api/articles/event_get_count/").json()

    return articles, count
