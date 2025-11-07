# utils/helpers.py
import numpy as np

def cosine_distance(a, b):
    """Compute cosine distance between two embeddings."""
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    return 1.0 - float(np.dot(a, b))

