import torch

one_hot = torch.tensor([0, 0, 1], dtype=torch.long)
de_one_hot = torch.argmax(one_hot).item()

print(one_hot, de_one_hot)
