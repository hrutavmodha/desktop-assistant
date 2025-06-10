import torch
import sys
from blueprint import CommandTransformer
vocab_list = ["<pad>", "<unk>"] + list(set("Open Google".split()))
vocab = {word: i for i, word in enumerate(vocab_list)}
inv_vocab = {i: w for w, i in vocab.items()}
vocab_size = len(vocab)
def tokenize(text):
  return [vocab.get(t, vocab["<unk>"]) for t in text.lower().split()]
def detokenize(toks): 
  return " ".join([inv_vocab[i] for i in toks if i in inv_vocab])
model = CommandTransformer(
  vocab_size, 
  64,
  4, 
  128,
  2
)
model.load_state_dict(
  torch.load("model.pth"))
model.eval()
def predict(text):
    x = torch.tensor(tokenize(text)).unsqueeze(0)
    with torch.no_grad():
        output = model(x)
        pred_ids = output.argmax(dim = -1).squeeze().tolist()
        print("Predicted Command:", detokenize(pred_ids))
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        predict(" ".join(sys.argv[1:]))
    else:
        predict("No command provided")
