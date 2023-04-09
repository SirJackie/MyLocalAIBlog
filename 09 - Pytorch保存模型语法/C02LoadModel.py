import torch
import torch.nn as nn
import torch.optim as optim


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
        x = self.fc3(x)
        return x


net = Net()
net.load_state_dict(torch.load("model.pth"))

# Prediction
x_test = torch.randn(3, 5)
with torch.no_grad():
    y_test = net(x_test)
    print(y_test)
