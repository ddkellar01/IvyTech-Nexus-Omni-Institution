import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from datasets import Dataset

class AcademicModelFineTuner:
    def __init__(self, model_name: str = "meta-llama/Llama-3.2-3B-Instruct"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    def tokenize_dataset(self, data: list):
        raw_dataset = Dataset.from_dict({"text": data})
        return raw_dataset.map(lambda x: self.tokenizer(x["text"], truncation=True, max_length=512), batched=True)

    def configure_trainer(self, train_dataset, output_dir: str = "./results"):
        args = TrainingArguments(
            output_dir=output_dir,
            per_device_train_batch_size=2,
            gradient_accumulation_steps=4,
            learning_rate=2e-4,
            logging_steps=10,
            save_strategy="epoch",
            fp16=True
        )
        return Trainer(model=self.model, args=args, train_dataset=train_dataset)
