import torch
import torch.nn as nn

class IvyAdaptiveGaussianGELU(nn.Module):
    """Custom advanced activation function synthesized by Professor nodes for neural architecture search."""
    def __init__(self):
        super().__init__()
        self.alpha = nn.Parameter(torch.tensor(1.0))
        self.beta = nn.Parameter(torch.tensor(0.0))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        gelu_val = 0.5 * x * (1.0 + torch.erf(x / torch.tensor(1.41421356)))
        return self.alpha * gelu_val + self.beta * torch.sin(x)
