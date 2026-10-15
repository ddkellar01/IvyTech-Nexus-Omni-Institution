import time
from typing import Dict, List

class ProfessorNodeRegistry:
    def __init__(self):
        self.registry: Dict[str, dict] = {}

    def register_node(self, node_id: str, specialty: str, endpoint: str):
        self.registry[node_id] = {
            "specialty": specialty,
            "endpoint": endpoint,
            "last_heartbeat": time.time(),
            "status": "ACTIVE"
        }
        print(f"[Registry] Professor node registered: {node_id} ({specialty}) at {endpoint}")

    def get_active_faculty(self) -> List[dict]:
        current_time = time.time()
        active_nodes = []
        for node_id, data in self.registry.items():
            if current_time - data["last_heartbeat"] < 60:
                active_nodes.append({"node_id": node_id, **data})
        return active_nodes
