import time

class SwarmSecurityHoneypot:
    """Deploys decoy endpoints within the container network to trap and isolate unauthorized agents."""
    def __init__(self, decoy_port: int = 9999):
        self.port = decoy_port
        self.captured_intrusions = []

    def monitor_decoy_traffic(self, incoming_ip: str, payload: str):
        print(f"[Honeypot-Alert] Unauthorized probe intercepted from {incoming_ip} on port {self.port}!")
        intrusion_log = {
            "timestamp": time.time(),
            "ip": incoming_ip,
            "payload_snippet": payload[:100],
            "action": "IP_BLACKLISTED"
        }
        self.captured_intrusions.append(intrusion_log)
        return intrusion_log
