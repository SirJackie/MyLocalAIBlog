import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt


# Defining Network
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(1, 1)

    def forward(self, x):
        x = self.fc1(x)
        return x


# Training
net = Net()
criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.005)


# Preparing Dataset
n = 20
k = 2
b = 3

x_train = torch.rand(n)
y_train = k * x_train + b + torch.randn(n) * 0.02

x_train = torch.unsqueeze(x_train, 1)
y_train = torch.unsqueeze(y_train, 1)


# Pre-Prediction before Training
with torch.no_grad():
    y_hat = net(x_train)
    plt.scatter(x_train, y_train)
    plt.plot(x_train, y_hat)
    plt.show()


for i in range(0, 500):
    y_hat = net(x_train)
    loss = criterion(y_hat, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if i % 10 == 9:
        print("Epoch: [%s/%s]; Loss: %s" % (i+1, 500, loss.item()))

# Prediction
with torch.no_grad():
    y_hat = net(x_train)
    plt.scatter(x_train, y_train)
    plt.plot(x_train, y_hat)
    plt.show()
