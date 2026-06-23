from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def search_tickets(query: str, tickets):
    corpus = [t.title + " " + t.description for t in tickets]

    # add query as last item
    corpus.append(query)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)

    query_vector = vectors[-1]
    ticket_vectors = vectors[:-1]

    scores = cosine_similarity(query_vector, ticket_vectors)[0]

    results = list(zip(tickets, scores))

    results.sort(key=lambda x: x[1], reverse=True)

    return results