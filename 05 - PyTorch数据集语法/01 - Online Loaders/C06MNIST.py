import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms

# 定义数据预处理操作，将图像数据转换为张量并进行标准化
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 加载 MNIST 数据集
train_dataset = datasets.MNIST(root='./PyTorchDataset', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./PyTorchDataset', train=False, download=True, transform=transform)

# 创建数据加载器
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)

# 显示数据集

# 遍历训练集数据加载器，获取一个批次的数据
for data, target in train_loader:
    # Data's Shape: (batch_size, num_channels, height, width)
    # Target's Shape: (batch_size,)
    print("Train: ", data.shape, target.shape)

# 遍历测试集数据加载器，获取一个批次的数据
for data, target in test_loader:
    # Data's Shape: (batch_size, num_channels, height, width)
    # Target's Shape: (batch_size,)
    print("Test: ", data.shape, target.shape)
