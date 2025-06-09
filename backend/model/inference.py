from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
tokenizer = AutoTokenizer.from_pretrained("backend/model/checkpoint")
model = AutoModelForSeq2SeqLM.from_pretrained("backend/model/checkpoint")
def predict(user_input):
    inputs = tokenizer(
        user_input, 
        return_tensors = "pt", 
        truncation = True,
        padding = True
    )
    output_ids = model.generate(
        **inputs,
        max_length = 32, 
        num_beams = 4, 
        early_stopping = True)
    result = tokenizer.decode(
        output_ids[0], 
        skip_special_tokens = True
    )
    return result
if __name__ == "__main__":
    prompt = input("You: ")
    if prompt.lower() in ["bye", "go off", "see you later", "see you soon", "goodbye"]:
        print(f"Bot: Bye")
    else:
        print(f"Bot: {predict(prompt)}")
