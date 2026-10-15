import torch
import torch.nn as nn

class FacultyRewardModel(nn.Module):
    """Evaluates the pedagogical tone and academic rigor of generated text for RLHF alignment."""
    def __init__(self, hidden_dim: int = 4096):
        super().__init__()
        self.scorer = nn.Sequential(
            nn.Linear(hidden_dim, 512),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(512, 1)
        )

    def forward(self, embedding_features: torch.Tensor) -> torch.Tensor:
        return self.scorer(embedding_features)
