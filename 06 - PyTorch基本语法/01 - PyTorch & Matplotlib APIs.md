# PyTorch APIs

```python
import torch
```

```python
# 创建张量
torch.tensor(alist, dtype=torch.float)  # 转换Python列表为张量
alist = tensor.tolist()                 # 转换张量为Python列表
torch.rand(N)   # 随机数
torch.randn(N)  # 正态分布随机数，可用于噪声生成
torch.zeros(N)  # 填充0
torch.ones(N)   # 填充1
tensor[i:j]     # 切片操作
torch.linspace(0, 1, 100)  # 0到1，切成100份
```

```python
# 张量的属性和方法
w  # 参与表达式计算（带梯度）
w.requires_grad = True  # 请求计算梯度
w.data      # 获取数据（不带梯度）
w.detach()  # 获取数据（不带梯度），同w.data
w.grad      # 获取梯度数据
w.mean()    # 计算张量分量的平均数
```

```python
# 表达式的属性和方法
exp.backward()  # 反向触发所有梯度计算（autograd机制）
```

独热编码：

```python
import torch
import torch.nn.functional as nn_func

alist = [0, 0, 0, 1, 1, 2]
tensor = torch.tensor(alist)
tensor_long = tensor.long()  # 将标签张量转换为长整型
tensor_one_hot = nn_func.one_hot(tensor_long, num_classes=3)
print(tensor_one_hot)
```

反独热编码：

```
one_hot = torch.tensor([0, 0, 1], dtype=torch.long)
de_one_hot = torch.argmax(one_hot).item()
```

四舍五入：

```
x = torch.tensor([0.1, 0.9, 0.1])
rounded = torch.round(x)
```

转换维度：

```python
y_train = torch.unsqueeze(target, 1)  # target: (506, ); y_train: (506, 1)
target = torch.squeeze(y_train)       # y_train: (506, 1); target: (506, )
```

# Matplotlib APIs

```python
import matplotlib as plt
```

```python
# 绘图方法
plt.plot(test_x, test_y)
plt.scatter(X, Y)
```

