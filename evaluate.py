from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-mpnet-base-v2")

def semantic_score(generated: str, ideal: str) -> float:
    emb_gen = model.encode([generated])
    emb_ideal = model.encode([ideal])
    return float(cosine_similarity(emb_gen, emb_ideal)[0][0])

def politeness_score(reply: str) -> float:
    polite_words = ["thank you", "please", "sorry"]
    return 1.0 if any(word in reply.lower() for word in polite_words) else 0.5

def completeness_score(reply: str, customer: str) -> float:
    # crude heuristic: check if reply mentions key nouns from customer query
    keywords = [w.lower() for w in customer.split() if len(w) > 4]
    return 1.0 if any(k in reply.lower() for k in keywords) else 0.6

def evaluate_reply(generated: str, ideal: str, customer: str) -> dict:
    return {
        "semantic": round(semantic_score(generated, ideal), 3),
        "politeness": politeness_score(generated),
        "completeness": completeness_score(generated, customer)
    }

def hybrid_score(scores: dict) -> float:
    # Weighted average: semantic (0.5), politeness (0.25), completeness (0.25)
    return round(
        0.5 * scores["semantic"] +
        0.25 * scores["politeness"] +
        0.25 * scores["completeness"], 3
    )
