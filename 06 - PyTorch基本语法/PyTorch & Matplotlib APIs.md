# PyTorch APIs

```python
import torch
```

```python
# 创建张量
torch.rand(N)   # 随机数
torch.randn(N)  # 正态分布随机数，可用于噪声生成
torch.zeros(N)  # 填充0
torch.ones(N)   # 填充1
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

# Matplotlib APIs

```python
import matplotlib as plt
```

```python
# 绘图方法
plt.plot(test_x, test_y)
plt.scatter(X, Y)
```

