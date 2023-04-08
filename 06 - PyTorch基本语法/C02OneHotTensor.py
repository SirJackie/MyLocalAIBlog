import torch
import torch.nn.functional as nn_func

alist = [0, 0, 0, 1, 1, 2]
tensor = torch.tensor(alist)
tensor_long = tensor.long()  # 将标签张量转换为长整型
tensor_one_hot = nn_func.one_hot(tensor_long, num_classes=3)
print(tensor_one_hot)
