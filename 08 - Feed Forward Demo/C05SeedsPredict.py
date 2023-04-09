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
net.load_state_dict(torch.load("M04Seeds.pth"))

# Predict
with torch.no_grad():
    y_hat = net(x_train)

    for i in range(0, len(y_hat)):
        hat = one_hot_decoder(y_hat[i])
        train = one_hot_decoder(y_train[i])

        if hat == train:
            print("Succeeded. Hat: %s; Train: %s; HatOH: %s; TrainOH: %s" % (hat, train, y_hat[i], y_train[i]))
        else:
            print("Failed. Hat: %s; Train: %s; HatOH: %s; TrainOH: %s" % (hat, train, y_hat[i], y_train[i]))
