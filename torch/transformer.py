import torch

class Transformer(torch.nn.Module):
    def __init__(self, args):
        super(Transformer, self).__init__()
        self.dim_features = args['dim_features']
        self.dim_sequence = args['dim_sequence']
        self.dim_layers = args['transformer_dim_layers']
        self.dim_heads = args['transformer_dim_heads']
        self.dim_feedforward = args['transformer_dim_feedforward']
        self.dim_predictor = args['transformer_dim_predictor']
        self.position_encoding = args['transformer_position_encoding']
        self.normalising = args['transformer_normalising']
        self.dropout = args['transformer_dropout']
        self.encoder = TransformerEncoder(self.dim_features, self.dim_sequence, self.dim_layers, self.dim_heads, self.dim_feedforward, self.position_encoding, self.normalising, self.dropout)
        self.dense1 = torch.nn.Linear(self.dim_sequence*self.dim_features, self.dim_predictor)
        self.relu1 = torch.nn.ReLU()
        self.dense2 = torch.nn.Linear(self.dim_predictor, 3)

    def forward(self, tensor:torch.Tensor) -> torch.Tensor:
        tensor = self.encoder(tensor)
        tensor = tensor.flatten(start_dim=1, end_dim=2)
        tensor = self.dense1(tensor)
        tensor = self.relu1(tensor)
        tensor = self.dense2(tensor)
        return tensor

class TransformerEncoder(torch.nn.Module):
    def __init__(self, dim_features:int, dim_sequence:int, dim_layers:int, dim_heads:int, dim_feedforward:int, position_encoding:bool, normalising:bool, dropout:float):
        super(TransformerEncoder, self).__init__()
        self.dim_features = dim_features
        self.dim_sequence = dim_sequence
        self.dim_layers = dim_layers
        self.position_encoding = position_encoding
        self.layers = torch.nn.ModuleList([TransformerEncoderLayer(dim_features, dim_sequence, dim_heads, dim_feedforward, normalising, dropout) for _ in range(self.dim_layers)])
    def forward(self, tensor:torch.Tensor) -> torch.Tensor:
        if self.position_encoding:
            pos = torch.arange(self.dim_sequence, dtype=deftype, device=device).reshape(1, -1, 1)
            dim = torch.arange(self.dim_features, dtype=deftype, device=device).reshape(1, 1, -1)
            phase = pos / (1e4 ** torch.div(dim, self.dim_features, rounding_mode='floor'))
            position_encoding = torch.where(dim.long() % 2 == 0, torch.sin(phase), torch.cos(phase))
            tensor += position_encoding
        for layer in self.layers:
            tensor = layer(tensor)
        return tensor

class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, dim_features:int, dim_sequence:int, dim_heads:int, dim_feedforward:int, normalising:bool, dropout:float):
        super(TransformerEncoderLayer, self).__init__()
        self.dim_features = dim_features
        self.dim_sequence = dim_sequence
        self.dim_heads = dim_heads
        self.dim_feedforward = dim_feedforward
        self.normalising = normalising
        self.dropout = dropout
        self.residual = Residual(dim_features, normalising, dropout)
        self.attention = MultiHeadAttention(dim_features, dim_sequence, dim_heads)
        self.feedforward = torch.nn.Sequential(
            torch.nn.Linear(dim_features, dim_feedforward),
            torch.nn.ReLU(),
            torch.nn.Linear(dim_feedforward, dim_features),
        )
    def forward(self, tensor:torch.Tensor) -> torch.Tensor:
        tensor = self.residual(self.attention, tensor, tensor, tensor)
        tensor = self.residual(self.feedforward, tensor)
        return tensor

class Residual(torch.nn.Module):
    def __init__(self, dim_features:int, normalising:bool, dropout:float):
        super(Residual, self).__init__()
        self.dim_features = dim_features
        self.normalising = normalising
        self.normalising_layer = torch.nn.LayerNorm(dim_features)
        self.dropout = dropout
        self.dropout_layer = torch.nn.Dropout(dropout)
    def forward(self, sublayer:torch.nn.Module, *tensors:torch.Tensor) -> torch.Tensor:
        if self.normalising:
            return self.normalising_layer(tensors[0] + self.dropout_layer(sublayer(*tensors)))
        else:
            return tensors[0] + self.dropout(sublayer(*tensors))

class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim_features:int, dim_sequence:int, dim_heads:int):
        super(MultiHeadAttention, self).__init__()
        self.dim_features = dim_features
        self.dim_sequence = dim_sequence
        self.dim_heads = dim_heads
        self.dim_qkv = max(1, dim_features // dim_heads)
        self.heads = torch.nn.ModuleList([AttentionHead(dim_features, self.dim_qkv) for _ in range(self.dim_heads)])
        self.linear = torch.nn.Linear(dim_heads*self.dim_qkv, dim_features)
    def forward(self, query:torch.Tensor, key:torch.Tensor, value:torch.Tensor) -> torch.Tensor:
        return self.linear(torch.cat([head(query, key, value) for head in self.heads], dim=-1))

class AttentionHead(torch.nn.Module):
    def __init__(self, dim_features:int, dim_qkv:int):
        super(AttentionHead, self).__init__()
        self.dim_features = dim_features
        self.dim_qkv = dim_qkv
        self.q = torch.nn.Linear(dim_features, dim_qkv)
        self.k = torch.nn.Linear(dim_features, dim_qkv)
        self.v = torch.nn.Linear(dim_features, dim_qkv)
    def forward(self, query:torch.Tensor, key:torch.Tensor, value:torch.Tensor) -> torch.Tensor:
        Q = self.q(query)
        K = self.k(key)
        V = self.v(value)
        scale = Q.size(-1) ** 0.5
        attention_score = torch.nn.functional.softmax(Q.bmm(K.transpose(1,2)) / scale, dim=-1)
        return attention_score.bmm(V)
    

class Attention(torch.nn.Module):
    def __init__(self,
        dim_embedding:int,
        num_head:int,
        pos_bias:torch.nn.Parameter,
        dropout:float,
    ) -> None:
        super().__init__()
        self.num_head = num_head
        self.dim_head = dim_embedding // num_head
        self.scale = self.dim_head**-0.5
        self.q = torch.nn.Linear(dim_embedding, self.dim_head*num_head)
        self.k = torch.nn.Linear(dim_embedding, self.dim_head*num_head)
        self.v = torch.nn.Linear(dim_embedding, self.dim_head*num_head)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.proj = torch.nn.Linear(self.dim_head*num_head, dim_embedding)
        self.pos_bias = pos_bias
        self.dropout = torch.nn.Dropout(dropout)

    def forward(self,
        x:torch.Tensor,
        mask:torch.Tensor=None
    ) -> torch.Tensor:
        d = self.dim_head
        h = self.num_head
        b, w, s, e = x.shape                                            # batch, windows, sequence, embedding
        q = self.q(x)                                                   # batch, windows, sequence, heads*q_dim
        k = self.k(x)                                                   # batch, windows, sequence, heads*k_dim
        v = self.v(x)                                                   # batch, windows, sequence, heads*v_dim
        q = self.scale * q                                              # batch, windows, sequence, heads*q_dim

        q = torch.reshape(q, (b, w, s, h, d))                           # batch, windows, sequence, heads, q_dim
        q = torch.permute(q, (0, 1, 3, 2, 4))                           # batch, windows, heads, sequence, q_dim
        k = torch.reshape(k, (b, w, s, h, d))                           # batch, windows, sequence, heads, k_dim
        k = torch.permute(k, (0, 1, 3, 2, 4))                           # batch, windows, heads, sequence, k_dim
        v = torch.reshape(v, (b, w, s, h, d))                           # batch, windows, sequence, heads, v_dim
        v = torch.permute(v, (0, 1, 3, 2, 4))                           # batch, windows, heads, sequence, v_dim

        attention = q @ k.transpose(-2,-1)                              # batch, windows, heads, sequence, sequence
        attention = attention + self.pos_bias                           # batch, windows, heads, sequence, sequence
        
        if mask is not None:
            attention = attention + mask                                # batch, windows, heads, sequence, sequence

        attention = self.softmax(attention)                             # batch, windows, heads, sequence, sequence
        attention = self.dropout(attention)                             # attention dropout
        z = attention @ v                                               # batch, windows, heads, sequence, v_dim
        z = torch.transpose(z, 2, 3)                                    # batch, windows, sequence, heads, v_dim
        z = torch.reshape(z, (b, w, s, h*d))                            # batch, windows, sequence, heads*v_dim
        z = self.proj(z)                                                # batch, windows, sequence, embedding
        return z


class MLP(torch.nn.Module):
    def __init__(self, 
        dim_embedding,
        dim_hidden,
        dropout,
    ) -> None:
        super().__init__()
        self.layers = torch.nn.Sequential(
            torch.nn.Linear(dim_embedding, dim_hidden),
            torch.nn.GELU(),
            torch.nn.Linear(dim_hidden, dim_embedding),
            torch.nn.GELU(),
            torch.nn.Dropout(dropout)
        )

    def forward(self,
        x:torch.Tensor
    ) -> torch.Tensor:
        return self.layers(x)