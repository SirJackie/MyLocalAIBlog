import torch
from sklearn.datasets import load_iris
import torch.nn.functional as nn_func

iris_data = load_iris()

data = torch.tensor(iris_data.data, dtype=torch.float)
target = torch.tensor(iris_data.target, dtype=torch.long)

x_train = data
y_train = nn_func.one_hot(target, num_classes=3).float()

print(x_train)
print(y_train)
print(target)
