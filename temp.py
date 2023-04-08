import torch.nn as nn


class Net(nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(5, 7)
        self.fc2 = nn.Linear(7, 7)
        self.fc3 = nn.Linear(7, 4)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc(3)
        return x
