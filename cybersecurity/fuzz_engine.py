import random
import string

class ProtocolFuzzingEngine:
    """Differential fuzzer utilized by security professor agents to test system robustness."""
    def __init__(self, target_function):
        self.target_function = target_function

    def generate_fuzz_payload(self, length: int = 64) -> str:
        letters = string.printable
        return ''.join(random.choice(letters) for _ in range(length))

    def run_fuzz_campaign(self, iterations: int = 100) -> dict:
        crashes = 0
        for _ in range(iterations):
            payload = self.generate_fuzz_payload()
            try:
                self.target_function(payload)
            except Exception as e:
                crashes += 1
        return {"iterations": iterations, "crashes_detected": crashes}
