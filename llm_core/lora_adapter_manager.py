import os

class LoRAAdapterManager:
    """Dynamically loads and unloads Low-Rank Adaptation (LoRA) weights for specialized professor roles."""
    def __init__(self, base_model_path: str):
        self.base_path = base_model_path
        self.loaded_adapters = {}

    def load_adapter(self, adapter_name: str, adapter_path: str):
        print(f"[LoRA] Loading adapter '{adapter_name}' from {adapter_path}...")
        self.loaded_adapters[adapter_name] = adapter_path

    def switch_adapter(self, model, adapter_name: str):
        if adapter_name not in self.loaded_adapters:
            raise KeyError(f"Adapter {adapter_name} not loaded.")
        print(f"[LoRA] Switched active model weights to adapter: {adapter_name}")
