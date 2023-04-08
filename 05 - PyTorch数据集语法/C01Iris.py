import torch
from sklearn.datasets import load_iris
import torch.nn.functional as nn_func

iris_data = load_iris()

data = torch.tensor(iris_data.data, dtype=torch.float)
labels = torch.tensor(iris_data.target)

print(data)
print(labels)

labels_long = labels.long()  # 将标签张量转换为长整型
labels_one_hot = nn_func.one_hot(labels_long, num_classes=3)
print(labels_one_hot)
