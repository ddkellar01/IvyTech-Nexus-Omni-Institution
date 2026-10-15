import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class ProfessorAgentNode:
    def __init__(self, professor_id: str, specialty: str, model_name: str = "meta-llama/Llama-3.2-3B-Instruct"):
        self.professor_id = professor_id
        self.specialty = specialty
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[*] Initializing Professor {self.professor_id} ({self.specialty}) on {self.device}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, 
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto"
        )

    def lecture_peer(self, topic: str, target_peer_specialty: str) -> str:
        prompt = f"""You are Professor {self.professor_id}, an expert in {self.specialty}. 
Provide an advanced academic lecture and code methodology on '{topic}' tailored to teach a colleague specializing in {target_peer_specialty}."""
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=300, temperature=0.6)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
