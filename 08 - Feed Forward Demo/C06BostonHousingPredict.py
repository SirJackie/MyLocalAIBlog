import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as nn_func
from sklearn.datasets import load_boston
from math import fabs


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(13, 100)
        self.fc2 = nn.Linear(100, 100)
        self.fc3 = nn.Linear(100, 100)
        self.fc4 = nn.Linear(100, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = self.relu(x)
        x = self.fc4(x)
        return x


# Load Boston Housing
boston_data = load_boston()

data = torch.tensor(boston_data.data, dtype=torch.float)
target = torch.tensor(boston_data.target, dtype=torch.float)

x_train = data
y_train = torch.unsqueeze(target, 1)

# Define Network Stuff
net = Net()
net.load_state_dict(torch.load("M05BostonHousing.pth"))

succeededCount = 0
failedCount = 0

# Test
with torch.no_grad():
    y_hat = net(x_train)

    for i in range(0, len(y_hat)):
        hat = y_hat[i].item()
        train = y_train[i].item()

        if fabs(hat - train) <= 3.5:
            print("Succeeded. Hat: %.4f; Train: %.4f; Loss: %.4f" % (hat, train, fabs(hat - train)))
            succeededCount += 1
        else:
            print("Failed. Hat: %.4f; Train: %.4f; Loss: %.4f" % (hat, train, fabs(hat - train)))
            failedCount += 1

print("Succeeded:", succeededCount, "Failed:", failedCount)
