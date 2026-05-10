from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_score(text):
    emb = model.encode(text)
    return {"semantic_vector": float(np.mean(emb))}