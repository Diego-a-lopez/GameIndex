import json
from elasticsearch import Elasticsearch, helpers
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


class SteamGameIndexer:
    def __init__(self, index_name='steam_games', json_file='SteamScrap/GAMES4.json',
                 elasticsearch_url='http://localhost:9200/'):
        self.index = index_name
        self.json_file = json_file
        self.client = Elasticsearch(elasticsearch_url)

        # Define the mapping for your index
        self.mappings = {
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

    def create_index(self, mappings=None):
        if mappings is None:
            mappings = self.mappings
        self.client.indices.create(index=self.index, body={"mappings": mappings})

    def read_all_games(self):
        with open(self.json_file, 'r', encoding='utf8') as f:
            games_data = json.load(f)
        return games_data

    def generate_data(self, game_data):
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
            data.append({"_index": self.index, "_source": document})
        return data

    def index_games(self):
        document_count = 0
        try:
            document_count = self.client.count(index=self.index)['count']
        except Exception as e:
            print(f"The index '{self.index}' does not exist.")
            self.create_index()
            all_games_data = self.read_all_games()
            helpers.bulk(self.client, self.generate_data(all_games_data))
            self.client.indices.refresh(index=self.index)
            document_count = self.client.count(index=self.index)['count']

        if document_count > 0:
            print(f"The index '{self.index}' has {document_count} documents.")

    def search_games(self, search_query):
        search_results = self.client.search(index=self.index, body=search_query)
        return search_results['hits']['hits']

    def cluster_search_results(self, search_results, num_clusters=3, field="description"):
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

    def delete_index(self):
        resp = self.client.indices.delete(
            index=self.index,
        )
        print(resp)


game_indexer = SteamGameIndexer()
game_indexer.index_games()

search_query = {
    "size": 10000,
    "query": {
        "match_all": {}
    }
}

results = game_indexer.search_games(search_query)
print("Search results:\n", results)

# clustering
results, clusters = game_indexer.cluster_search_results(results)
for i, result in enumerate(results):
    print(f"Game name: {result['_source']['title']}, Cluster: {clusters[i]}")
