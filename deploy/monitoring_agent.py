import time
import psutil
import torch

class SwarmTelemetryCollector:
    def __init__(self, node_id: str):
        self.node_id = node_id

    def collect_metrics(self) -> dict:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        gpu_active = torch.cuda.is_available()
        gpu_vram = torch.cuda.memory_allocated() if gpu_active else 0

        return {
            "node_id": self.node_id,
            "timestamp": time.time(),
            "cpu_percent": cpu_usage,
            "ram_percent": ram_usage,
            "gpu_available": gpu_active,
            "gpu_vram_allocated_bytes": gpu_vram
        }

if __name__ == "__main__":
    collector = SwarmTelemetryCollector(node_id="Professor-Node-01")
    print("Telemetry Metrics:", collector.collect_metrics())
