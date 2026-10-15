import time
import requests

class SwarmCoordinator:
    def __init__(self, host: str = "0.0.0.0", port: int = 8000):
        self.host = host
        self.port = port
        self.registered_nodes = []

    def register_professor_node(self, node_endpoint: str):
        self.registered_nodes.append(node_endpoint)
        print(f"[+] Registered Professor Worker Node: {node_endpoint}")

    def broadcast_curriculum(self, payload: dict):
        print(f"[*] Broadcasting curriculum across {len(self.registered_nodes)} professor nodes...")
        for node in self.registered_nodes:
            try:
                requests.post(f"{node}/receive-lecture", json=payload, timeout=5)
            except Exception as e:
                print(f"[!] Failed to reach node {node}: {e}")

if __name__ == "__main__":
    coordinator = SwarmCoordinator()
    print("Swarm Coordinator initialized successfully.")
