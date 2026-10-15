import random
from typing import List

class SwarmLoadBalancer:
    """Distributes peer-review and code synthesis workloads across optimal GPU worker nodes."""
    def __init__(self):
        self.nodes = []

    def register_worker(self, node_id: str, available_vram_gb: float):
        self.nodes.append({"node_id": node_id, "vram": available_vram_gb, "active_tasks": 0})

    def assign_task(self, task_name: str) -> str:
        if not self.nodes:
            raise RuntimeError("No worker nodes available in cluster.")
        # Select node with highest available VRAM and lowest active tasks
        optimal_node = min(self.nodes, key=lambda n: (n["active_tasks"], -n["vram"]))
        optimal_node["active_tasks"] += 1
        print(f"[LoadBalancer] Assigned task '{task_name}' to node {optimal_node['node_id']}")
        return optimal_node["node_id"]
