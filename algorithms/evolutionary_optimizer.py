import random
import torch

class EvolutionaryNeuralBreeder:
    """Genetic algorithm framework allowing professor nodes to cross-breed neural network layer configurations."""
    def __init__(self, population_size: int = 10):
        self.population_size = population_size

    def initialize_population(self) -> list:
        population = []
        for _ in range(self.population_size):
            config = {
                "embed_dim": random.choice([256, 512, 1024]),
                "num_heads": random.choice([4, 8, 16]),
                "dropout_rate": round(random.uniform(0.05, 0.3), 2)
            }
            population.append(config)
        return population

    def crossover_and_mutate(self, parent_a: dict, parent_b: dict) -> dict:
        child = {
            "embed_dim": random.choice([parent_a["embed_dim"], parent_b["embed_dim"]]),
            "num_heads": random.choice([parent_a["num_heads"], parent_b["num_heads"]]),
            "dropout_rate": parent_a["dropout_rate"] if random.random() > 0.5 else parent_b["dropout_rate"]
        }
        # Mutation step
        if random.random() < 0.2:
            child["dropout_rate"] = round(random.uniform(0.05, 0.4), 2)
        return child
