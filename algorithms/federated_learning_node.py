import torch
import copy

class FederatedLearningAggregator:
    """Aggregates decentralized weight updates from autonomous professor worker nodes using FedAvg."""
    def __init__(self, global_model: torch.nn.Module):
        self.global_model = global_model

    def aggregate_weights(self, client_weights_list: list) -> torch.nn.Module:
        print(f"[FederatedLearning] Aggregating updates from {len(client_weights_list)} professor worker nodes...")
        new_state_dict = copy.deepcopy(self.global_model.state_dict())
        for key in new_state_dict.keys():
            if new_state_dict[key].is_floating_point():
                stack = torch.stack([weights[key] for weights in client_weights_list])
                new_state_dict[key] = torch.mean(stack, dim=0)
        self.global_model.load_state_dict(new_state_dict)
        return self.global_model
