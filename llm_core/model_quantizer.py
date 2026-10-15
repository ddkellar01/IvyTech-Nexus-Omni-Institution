import torch
import torch.nn as nn

class AcademicModelQuantizer:
    """Quantizes model weights to INT8 to reduce memory footprint across resource-constrained worker nodes."""
    @staticmethod
    def quantize_linear_layer(layer: nn.Linear) -> nn.quantized.DynamicQuantizedLinear:
        print(f"[Quantizer] Converting Linear layer to dynamic INT8 quantization...")
        quantized_layer = torch.quantization.quantize_dynamic(
            layer, {nn.Linear}, dtype=torch.qint8
        )
        return quantized_layer
