from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TrainingArguments, Trainer
from datasets import load_dataset, Dataset
import json
import sys
with open("backend/model/data/data.json") as f:
    raw_data = json.load(f)
train_data = []
for entry in raw_data:
    for variant in entry["input"]:
        train_data.append({
            "input": variant,
            "output": entry["output"][sys.platform()]
        })
dataset = Dataset.from_list(train_data)
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
def preprocess(example):
    inputs = tokenizer(
        example["input"], 
        truncation = True, 
        padding = "max_length",
        max_length = 32
    )
    labels = tokenizer(
        example["output"],
        truncation = True, 
        padding = "max_length",
        max_length = 32
    )
    inputs["labels"] = labels["input_ids"]
    return inputs
tokenized_dataset = dataset.map(preprocess)
training_args = TrainingArguments(
    output_dir = "./backend/model/checkpoint",
    per_device_train_batch_size = 4,
    num_train_epochs = 5,
    logging_steps = 10,
    save_total_limit = 1
)
trainer = Trainer(
    model = model,
    args = training_args,
    train_dataset = tokenized_dataset
)
trainer.train()
print("Model trained successfully")
model.save_pretrained("backend/model/checkpoint")
tokenizer.save_pretrained("backend/model/checkpoint")
print("Model saved successfully")
