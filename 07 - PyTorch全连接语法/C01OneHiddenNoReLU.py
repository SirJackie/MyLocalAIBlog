import torch.nn as nn


# 2 fc layers without relu
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(5, 7)
        self.fc2 = nn.Linear(7, 4)

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        return x
