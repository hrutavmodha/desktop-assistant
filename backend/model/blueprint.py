import torch
import torch.nn as nn
class CommandTransformer(nn.Module):
    def __init__(
        self, 
        vocab_size,
        embed_dim,
        num_heads, 
        ff_dim, 
        num_layers,
        max_len = 128
    ):
        super(
            CommandTransformer, 
            self
        ).__init__()
        self.embedding = nn.Embedding(
            vocab_size, 
            embed_dim
        )
        self.positional = nn.Parameter(
            torch.zeros(
                1,
                max_len, 
                embed_dim
            )
        )
        encoder_layer = nn.TransformerEncoderLayer(
            d_model = embed_dim, 
            nhead = num_heads, 
            dim_feedforward = ff_dim, 
            batch_first = True
        )
        self.transformer = nn.TransformerEncoder(
            encoder_layer,
            num_layers = num_layers
        )
        self.fc_out = nn.Linear(
            embed_dim, 
            vocab_size
        )
    def forward(self, x):
        seq_len = x.size(1)
        x = self.embedding(x) + self.positional[:, :seq_len, :]
        x = self.transformer(x)
        return self.fc_out(x)
