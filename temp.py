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

x_train = torch.randn(10, 5)
y_train = torch.randn(10, 4)

criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)


# Iteration
for i in range(0, 1000):
    y_hat = net(x_train)
    loss = criterion(y_hat, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if i % 100 == 99:
        print("Epoch: [%s/%s]; Loss: %s" % (i+1, 1000, loss.item()))


# Prediction
x_test = torch.randn(3, 5)
with torch.no_grad():
    y_hat = net(x_test)
    print(y_hat)
