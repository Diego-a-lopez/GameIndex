from elasticsearch import Elasticsearch, helpers
import json

# COMANDO DE DOCKER: docker run --rm -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.10.0

client = Elasticsearch("http://localhost:9200/")
INDEX = 'steam_games'
JSON_FILE = 'SteamScrap/GAMES3.json'


def create_index():
    client.indices.create(index=INDEX, body={"mappings": mappings})
    # res = index.create()
    # print(res)


def read_all_games():
    with open(JSON_FILE, 'r', encoding='utf8') as f:
        games_data = json.load(f)
        return games_data


test_search_query = {
    "query": {
        "bool": {
            "must": {
                "match_phrase": {
                    "developers": "Entwell Co., Ltd."
                }
            },
            "filter": {
                "bool": {
                    "must_not": {
                        "match_phrase": {
                            "publishers": "Entwell Co., Ltd."
                        }
                    }
                }
            }
        }
    }
}

# Modify the mappings to use lowercase property names
mappings = {
    "properties": {
        "title": {"type": "text", "analyzer": "english"},
        "description": {"type": "text", "analyzer": "english"},
        "price": {"type": "float"},
        "genre": {"type": "keyword", "multi": True},
        "developers": {"type": "text", "analyzer": "standard", "multi": True},
        "publishers": {"type": "text", "analyzer": "standard", "multi": True},
        "franchise": {"type": "text", "analyzer": "standard", "multi": True},
        "release_date": {"type": "date", "format": "dd MMM, yyyy"},
        "header_image": {"type": "keyword"},
        "image_list": {"type": "keyword", "multi": True},
        "url": {"type": "keyword"},
        "score": {"type": "integer"},
        "reviews": {"type": "text", "analyzer": "english"}
    }
}


def gen_data(game_data):
    data = []
    for game in game_data:
        title = game.get("title", None)
        description = game.get("descrition", None)
        price = game.get("price", None)
        genre = game.get("genre", [])
        developers = game.get("developers", [])
        publishers = game.get("publishers", [])
        franchise = game.get("franchise", [])
        release_date = game.get("release_date", None)
        header_image = game.get("header_Image", None)
        image_list = game.get("image_List", [])
        url = game.get("url", None)
        score = game.get("score", None)
        reviews = game.get("reviews", None)
        document = {
            "title": title,
            "description": description,
            "price": price,
            "genre": genre,
            "developers": developers,
            "publishers": publishers,
            "franchise": franchise,
            "release_date": release_date,
            "header_image": header_image,
            "image_list": image_list,
            "url": url,
            "score": score,
            "reviews": reviews
        }
        data.append({"_index": INDEX, "_source": document})
    return data


all_games_data = read_all_games()
helpers.bulk(client, gen_data(all_games_data))
# client.indices.refresh(index=INDEX)
# client.cat.count(index=INDEX, format="json")

resp = client.search(index="steam_games", body=test_search_query)

# Get the response body
result = resp['hits']['hits']
for hit in result:
    print(hit["_source"])
