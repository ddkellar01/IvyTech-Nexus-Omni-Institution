import torch
import torch.nn as nn
import torch.optim as optim

class ProfessorPPOAlignment(nn.Module):
    """Reinforcement Learning from AI Feedback (RLHF) to optimize professor pedagogical tone."""
    def __init__(self, model_dim: int):
        super().__init__()
        self.value_head = nn.Sequential(
            nn.Linear(model_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )
        self.optimizer = optim.Adam(self.parameters(), lr=1e-5)

    def compute_reward_loss(self, rewards: torch.Tensor, values: torch.Tensor) -> torch.Tensor:
        advantages = rewards - values.detach()
        loss = -(advantages * values).mean()
        return loss
