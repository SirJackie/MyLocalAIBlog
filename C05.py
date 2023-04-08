import torch
import torch.nn as nn
import torch.optim as optim

# 3 fc layers with training process

# 定义数据集
x_train = torch.randn(10, 5)
y_train = torch.randn(10, 4)
# 第一维的大小10表示批大小（batch size），即每次训练使用的样本数量。


# 定义神经网络模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
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

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)
# net.parameters()返回权重矩阵的迭代器


# 训练模型
for epoch in range(1000):
    # 前向传播
    output = net(x_train)
    loss = criterion(output, y_train)

    # 反向传播
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, 1000, loss.item()))
        # loss.item()是用来获取张量loss中的单个数值的函数。

# 使用模型进行预测
x_test = torch.randn(5, 5)
with torch.no_grad():
    output = net(x_test)
    print(output)
