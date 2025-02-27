import torch
import numpy

a = torch.tensor([[[1,2,3,7],[7,8,9,2]],[[3,4,5,8],[0,0,0,1]],[[9,8,7,6],[6,5,4,2]]], dtype=torch.float)

std_for_features = a.std((0,1),unbiased=False)
mean_for_features = a.mean((0,1))
max_for_features = a.amax((0,1), keepdim=True)
min_for_features = a.amin((0,1), keepdim=True)
std_across_featues = a.std(-1,unbiased=False, keepdim=True)
mean_across_features = a.mean(-1, keepdim=True)
std_for_seqfeatures = a.std(0,unbiased=False)
mean_for_seqfeatures = a.mean(0)

print(a)
# Z-Score Normalization across whole dataset (samples, seq) for features
c = (a - mean_for_features) / std_for_features

# Min-Max Normalization across whole dataset for features
f = (a - min_for_features) / (max_for_features - min_for_features)
print(f)
# Z-score Normalization across all samples for features
d = (a - mean_for_seqfeatures) / std_for_seqfeatures

# Z-score Normalization across features
e = (a - mean_across_features) / std_across_featues

# Torch layer norm gleich wie across features
b = torch.nn.LayerNorm((4), eps=0,elementwise_affine=False)(a)

# L2 Normalization across features
g = a / torch.sqrt(a.square().sum(-1, keepdim=True))
