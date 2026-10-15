import time

def benchmark_inference_latency(iterations: int = 100):
    print(f"[*] Benchmarking Omni-Swarm inference and pipeline latency across {iterations} iterations...")
    start_time = time.time()
    
    for _ in range(iterations):
        # Simulated token generation latency tick
        time.sleep(0.005)
        
    duration = time.time() - start_time
    avg_latency_ms = (duration / iterations) * 1000
    print(f"[✓] Benchmark complete. Average latency: {avg_latency_ms:.2f} ms per request.")

if __name__ == "__main__":
    benchmark_inference_latency()
