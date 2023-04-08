import torch
from sklearn.datasets import load_iris
import torch.nn.functional as F

iris_data = load_iris()

data = torch.tensor(iris_data.data, dtype=torch.float)
labels = torch.tensor(iris_data.target)

print(data)
print(labels)

labels_idx = labels.long()  # 将标签张量转换为长整型
labels_one_hot = F.one_hot(labels_idx, num_classes=3)
print(labels_one_hot)
