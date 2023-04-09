import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as nn_func
from sklearn.datasets import load_boston


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
criterion = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=0.005)

# Train
for i in range(0, 10000):
    y_hat = net(x_train)
    loss = criterion(y_hat, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if i % 100 == 99:
        print("Epoch: [%s/%s]; Loss: %s" % (i+1, 10000, loss.item()))

# Save
torch.save(net.state_dict(), "M05BostonHousing.pth")
