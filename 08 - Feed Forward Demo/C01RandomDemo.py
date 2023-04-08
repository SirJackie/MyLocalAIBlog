import torch
import torch.nn as nn
import torch.optim as optim

# 定义神经网络模型
class Net(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 定义模型参数
input_size = 10
hidden_size = 20
output_size = 2

# 初始化模型
model = Net(input_size, hidden_size, output_size)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 构造训练数据
X_train = torch.randn(100, input_size)
y_train = torch.randint(0, output_size, (100,))

# 训练模型
for epoch in range(100):
    # 前向传播
    outputs = model(X_train)

    # 计算损失
    loss = criterion(outputs, y_train)

    # 反向传播
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 打印损失
    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, 100, loss.item()))
