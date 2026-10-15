import time

class SwarmNodeFirewall:
    """Monitors inter-node communications and blocks unauthorized payloads."""
    def __init__(self, allowed_subnets: list):
        self.allowed_subnets = allowed_subnets
        self.blocked_ips = set()

    def inspect_packet(self, source_ip: str, payload_size: int) -> bool:
        if source_ip in self.blocked_ips:
            print(f"[Security Warning] Dropped packet from blocked IP: {source_ip}")
            return False
        if payload_size > 1048576: # 1 MB limit
            print(f"[Security Warning] Payload size exceeded limit from {source_ip}")
            self.blocked_ips.add(source_ip)
            return False
        return True
