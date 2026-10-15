import sys
import os
import torch
import pytest

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.nnl_activations import IvyAdaptiveGaussianGELU
from algorithms.evolutionary_optimizer import EvolutionaryNeuralBreeder

def test_adaptive_gaussian_gelu_forward():
    activation = IvyAdaptiveGaussianGELU()
    x = torch.randn(2, 4, 16)
    out = activation(x)
    assert out.shape == x.shape

def test_evolutionary_breeder_population():
    breeder = EvolutionaryNeuralBreeder(population_size=5)
    pop = breeder.initialize_population()
    assert len(pop) == 5
    
    child = breeder.crossover_and_mutate(pop[0], pop[1])
    assert "embed_dim" in child
    assert "num_heads" in child
