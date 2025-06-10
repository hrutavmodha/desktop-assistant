import json
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from blueprint import CommandTransformer
def tokenize(text, vocab):
    return [
      vocab.get(
        t, 
        vocab["<unk>"
        ]
      ) 
      for t in text.lower().split()
    ]
class CommandDataset(Dataset):
    def __init__(
      self, 
      path,
      vocab
    ):
        self.data = json.load(open(path))
        self.vocab = vocab
        self.inputs = self.outputs = []
        for sample in self.data:
            for inp in sample["input"]:
                self.inputs.append(
                  tokenize(
                    inp, 
                    vocab
                  )
                )
                self.outputs.append(
                  tokenize(
                    sample["output"]["windows"], 
                    vocab
                  )
                )
    def __len__(self): 
      return len(self.inputs)
    def __getitem__(self, idx):
        x = torch.tensor(
          self.inputs[idx], 
          dtype = torch.long
        )
        y = torch.tensor(
          self.outputs[idx], 
          dtype = torch.long
        )
        return x, y
data = json.load(open("data.json"))
vocab_list = ["<pad>", "<unk>"] + list(set(data).split()))
vocab = {word: i for i, word in enumerate(vocab_list)}
vocab_size = len(vocab)
model = CommandTransformer(
  vocab_size, 
  64,
  4, 
  128,
  2
)
loss_fn = nn.CrossEntropyLoss(
  ignore_index = vocab["<pad>"]
)
optim = torch.optim.Adam(
  model.parameters(),
  lr = 1e-3
)
dataset = CommandDataset(
  "backend/model/data/data.json",
  vocab
)
loader = DataLoader(
  dataset, 
  batch_size = 2, 
  shuffle = True, 
  collate_fn = lambda b: (
    nn.utils.rnn.pad_sequence([
      x for x,
      _ in b
    ]
  ),
    batch_first = True, 
    padding_value = vocab["<pad>"]
    , nn.utils.rnn.pad_sequence([
      y for _, 
      y in b
    ],
    batch_first = True,
    padding_value = vocab["<pad>"]
)
for epoch in range(10):
    for batch_x, batch_y in loader:
        out = model(batch_x)
        loss = loss_fn(
          out.view(
            -1,
            vocab_size
          ), batch_y.view(-1))
        optim.zero_grad()
        loss.backward()
        optim.step()
    print(f"Epoch {epoch+1}\nLoss: {loss.item()}\n")
torch.save(
  model.state_dict(), 
  "model.pth"
)
