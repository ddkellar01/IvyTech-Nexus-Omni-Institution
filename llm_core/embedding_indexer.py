import numpy as np

class AcademicVectorIndexer:
    """Vector database indexing engine for fast similarity search across research repositories."""
    def __init__(self, dimension: int = 768):
        self.dimension = dimension
        self.vectors = []
        self.metadata = []

    def add_document(self, vector: list, meta: dict):
        if len(vector) != self.dimension:
            raise ValueError(f"Vector dimension mismatch. Expected {self.dimension}.")
        self.vectors.append(np.array(vector, dtype=np.float32))
        self.metadata.append(meta)

    def search(self, query_vector: list, top_k: int = 3) -> list:
        q = np.array(query_vector, dtype=np.float32)
        scores = [np.dot(q, v) / (np.linalg.norm(q) * np.linalg.norm(v) + 1e-8) for v in self.vectors]
        top_indices = np.argsort(scores)[-top_k:][::-1]
        return [{"meta": self.metadata[i], "score": float(scores[i])} for i in top_indices]
