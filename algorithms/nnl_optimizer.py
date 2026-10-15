import torch
import torch.nn as nn

class PeerOptimizedAttention(nn.Module):
    def __init__(self, embed_dim: int, num_heads: int):
        super().__init__()
        self.mha = nn.MultiheadAttention(embed_dim=embed_dim, num_heads=num_heads, batch_first=True)
        self.norm = nn.LayerNorm(embed_dim)
        self.feedback_gate = nn.Parameter(torch.tensor(0.5))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        normed = self.norm(x)
        attn_out, _ = self.mha(normed, normed, normed)
        return x + (self.feedback_gate * attn_out)
