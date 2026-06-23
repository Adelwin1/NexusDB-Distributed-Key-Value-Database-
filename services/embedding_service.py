from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()


def embed_text(text: str):
    return text


def search_by_embedding(query: str, tickets):
    corpus = [t.title + " " + t.description for t in tickets]

    if len(corpus) == 0:
        return []

    X = vectorizer.fit_transform(corpus + [query])

    query_vec = X[-1]
    docs_vec = X[:-1]

    scores = cosine_similarity(query_vec, docs_vec)[0]

    results = list(zip(tickets, scores))
    results.sort(key=lambda x: x[1], reverse=True)

    return results