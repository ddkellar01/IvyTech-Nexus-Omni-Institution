import time
from typing import Dict

class MeshHeartbeatMonitor:
    """Tracks continuous liveness across distributed professor worker nodes in the omni-swarm."""
    def __init__(self, timeout_threshold: float = 15.0):
        self.threshold = timeout_threshold
        self.node_heartbeats: Dict[str, float] = {}

    def record_heartbeat(self, node_id: str):
        self.node_heartbeats[node_id] = time.time()

    def get_dead_nodes(self) -> list:
        current_time = time.time()
        dead_nodes = []
        for node_id, last_seen in self.node_heartbeats.items():
            if current_time - last_seen > self.threshold:
                dead_nodes.append(node_id)
        return dead_nodes
