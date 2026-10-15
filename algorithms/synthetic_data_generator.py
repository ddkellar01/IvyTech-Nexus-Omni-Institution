import random

class SyntheticAcademicDataGenerator:
    """Generates synthetic training datasets for privacy-preserving machine learning experiments."""
    def __init__(self, seed: int = 42):
        random.seed(seed)

    def generate_research_batch(self, size: int = 100) -> list:
        topics = ["Quantum Computing", "Zero-Knowledge Proofs", "Neural Architecture Search", "Federated Learning"]
        dataset = []
        for _ in range(size):
            entry = {
                "topic": random.choice(topics),
                "citation_count": random.randint(5, 250),
                "peer_review_score": round(random.uniform(3.2, 5.0), 2),
                "synthetic_flag": True
            }
            dataset.append(entry)
        return dataset
