import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as nn_func
import json


def one_hot_decoder(one_hot):
    return torch.argmax(one_hot).item()


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(7, 14)
        self.fc2 = nn.Linear(14, 14)
        self.fc3 = nn.Linear(14, 3)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x


# Load Seeds
seeds_data = None
with open("D01Seeds.json", "rb") as f:
    seeds_data = f.read().decode("utf-8")
    seeds_data = json.loads(seeds_data)

data = torch.tensor(seeds_data["data"], dtype=torch.float)
target = torch.tensor(seeds_data["target"], dtype=torch.long)

x_train = data
y_train = nn_func.one_hot(target, num_classes=3).float()

# Define Network Stuff
net = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.01)

# Train
for i in range(0, 10000):
    y_hat = net(x_train)
    loss = criterion(y_hat, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if i % 1000 == 999:
        print("Epoch: [%s/%s]; Loss: %s" % (i+1, 10000, loss.item()))

# Save
torch.save(net.state_dict(), "M04Seeds.pth")

