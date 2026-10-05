from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

sentences = [
    "My cat is nice to me",
    "My dog is nice to me"
]

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(sentences)

similarity_matrix = cosine_similarity(vectors[0:1], vectors[1:2])

match_score = similarity_matrix[0][0] * 100

print(match_score)

"""
Here, we used TF-IDF vectorization to convert the sentences into numerical vectors.
But the issue is that TF-IDF does not capture the semantic meaning of the sentences. For example, "My cat is nice to me" and "My dog is nice to me" are semantically similar, but TF-IDF may not reflect that similarity accurately.
But it can be used to generally maatch sentences based on the frequency of words. For example :-
"""

A = 'Cats are wonderful pets.'
B = 'Cats are the best pets in this wonderful world.'
C = 'The stock market fell today.'

Sentences = [A, B, C]
vectors = vectorizer.fit_transform(Sentences) #used capital S here

AB = cosine_similarity(vectors[0:1], vectors[1:2])
AC = cosine_similarity(vectors[0:1], vectors[2:3])

print("A ↔ B:", AB[0][0])
print("A ↔ C:", AC[0][0])
#when we run this we can obviously see that A & B are more similar but this is coming mainly from the frequency of words rather than the semantic meaning of the sentences. This is a limitation of TF-IDF vectorization.
#TO get over this we can use embeddings which are more semantically aware and can capture the meaning of the sentences better. Embeddings are dense vector representations of text that capture semantic relationships between words and phrases.

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Cats are wonderful pets.",
    "I really like having a cat at home.",
    "The stock market fell today."
]

embeddings = model.encode(sentences)

similarity_matrix = cosine_similarity(
    embeddings[0:1],
    embeddings[1:2]
)

match_score = similarity_matrix[0][0] * 100

print(embeddings)
print(match_score)
"""
We got much higher similarity score between the first two sentences. This is because embeddings capture the semantic meaning of the sentences better than TF-IDF vectorization.
We should also note that when I used TF-IDF witht the same sentences, it gave me really low similarity and then I had to change the sentence to have more word frequency, then only it went up.
while with embedding, it gave me a high similarity score even though the sentences were not exactly the same but they were semantically similar. This is the power of embeddings and why they are preferred for semantic similarity tasks.
"""