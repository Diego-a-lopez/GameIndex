import elastic_transport
from elasticsearch import Elasticsearch, helpers
import json
from elasticsearch_dsl import Search
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from summarizer import Summarizer
from elasticsearch import Elasticsearch

# COMANDO DE DOCKER: docker run --rm -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.10.0

client = Elasticsearch("http://localhost:9200/")
INDEX = 'steam_games'
JSON_FILE = 'SteamScrap/GAMES4.json'

# resp = client.indices.delete(
#     index=INDEX,
# )
# print(resp)

mappings = {
    "properties": {
        "title": {"type": "text", "analyzer": "english"},
        "description": {"type": "text", "analyzer": "english"},
        "price": {"type": "float"},
        "genre": {"type": "keyword"},
        "developers": {"type": "keyword"},
        "publishers": {"type": "keyword"},
        "franchise": {"type": "keyword"},
        "release_date": {"type": "date", "format": "strict_date_optional_time"},
        "header_image": {"type": "keyword"},
        "image_list": {"type": "keyword"},
        "url": {"type": "keyword"},
        "score": {"type": "keyword"},
        "reviews": {"type": "text", "analyzer": "english"}
    }
}


def create_index(mappings=mappings):
    client.indices.create(index=INDEX, body={"mappings": mappings})


def read_all_games():
    with open(JSON_FILE, 'r', encoding='utf8') as f:
        games_data = json.load(f)
        return games_data


test_search_query = {
    "query": {
        "bool": {
            "must": {
                "match_phrase": {
                    'title': 'Mortal Kombat 1'
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

search_query = {
    "size": 10000,  # Max number of results
    "query": {
        "match_all": {}
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


document_count = 0
try:
    document_count = client.count(index=INDEX)['count']
except Exception as e:
    print(f"The index '{INDEX}' is does not exist.")
    create_index()
    all_games_data = read_all_games()
    helpers.bulk(client, gen_data(all_games_data))
    client.indices.refresh(index=INDEX)
    document_count = client.count(index=INDEX)['count']

if document_count > 0:
    print(f"The index '{INDEX}' has {document_count} documents.")


def cluster_search_results(search_results, num_clusters=3, field="description"):
    # Extract text data for clustering
    documents = [result['_source'][field] for result in search_results]

    # Convert text data to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(tfidf_matrix)
    clusters = kmeans.labels_

    # Assign clusters to search results
    for i, result in enumerate(search_results):
        result['_source']['cluster'] = clusters[i]

    return search_results, clusters




# Usage example
search_results = client.search(index=INDEX, body=search_query)
# test_Search = client.search(index=INDEX, body={"query": {"match_phrase": {"genre": "Action"}}})
search_results = search_results['hits']['hits']
print("Search results:\n")
print(search_results)

# Example of clustering
search_results, clusters = cluster_search_results(search_results)
for i, result in enumerate(search_results):
    print(f"Game name: {result['_source']['title']}, Cluster: {clusters[i]}")


