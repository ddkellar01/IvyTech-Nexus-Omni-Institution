import torch
import torch.nn as nn

class AcademicKnowledgeGNN(nn.Module):
    """Graph Neural Network for mapping citation networks and collaborative professor research domains."""
    def __init__(self, in_features: int, hidden_dim: int, out_features: int):
        super().__init__()
        self.layer1 = nn.Linear(in_features, hidden_dim)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_dim, out_features)

    def forward(self, node_features: torch.Tensor, adjacency_matrix: torch.Tensor) -> torch.Tensor:
        aggregated = torch.matmul(adjacency_matrix, node_features)
        h = self.relu(self.layer1(aggregated))
        return self.layer2(h)
