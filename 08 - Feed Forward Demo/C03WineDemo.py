import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as nn_func
from sklearn.datasets import load_wine


def one_hot_decoder(one_hot):
    return torch.argmax(one_hot).item()


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(13, 26)
        self.fc2 = nn.Linear(26, 26)
        self.fc3 = nn.Linear(26, 3)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x


# Load Wine
wine_data = load_wine()

data = torch.tensor(wine_data.data, dtype=torch.float)
target = torch.tensor(wine_data.target, dtype=torch.long)

x_train = data
y_train = nn_func.one_hot(target, num_classes=3).float()

# Define Network Stuff
net = Net()
criterion = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=0.01)

# Train
for i in range(0, 6000):
    y_hat = net(x_train)
    loss = criterion(y_hat, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if i % 1000 == 999:
        print("Epoch: [%s/%s]; Loss: %s" % (i+1, 6000, loss.item()))

# Save
torch.save(net.state_dict(), "M02Wine.pth")

# Test
with torch.no_grad():
    y_hat = net(x_train)

    for i in range(0, len(y_hat)):
        print(one_hot_decoder(y_hat[i]), one_hot_decoder(y_train[i]))
