import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification

model_path = "models/buggy_model.pt"
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaForSequenceClassification.from_pretrained("microsoft/codebert-base")

model.load_state_dict(torch.load(model_path))
model.eval()

def detect_bugs(code_snippet):
    inputs = tokenizer(code_snippet, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    return "Buggy Code Detected" if prediction == 1 else "No Bugs Detected"

if __name__ == "__main__":
    code = """def example(): return 1/0"""
    print(detect_bugs(code))
