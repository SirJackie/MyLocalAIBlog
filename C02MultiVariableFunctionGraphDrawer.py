# pyplot  是命令式函数的集合
from matplotlib import pyplot as plt
# Axes3D 包含的是实现3d绘图的各种方法
from mpl_toolkits.mplot3d import Axes3D
# numpy 是常用的科学计算库
import numpy as np

# 新建一个画布
figure = plt.figure()
# 新建一个3d绘图对象
ax = Axes3D(figure, auto_add_to_figure=False)
figure.add_axes(ax)

# 生成x, y 的坐标集 (-2,2) 区间，间隔为 0.1
x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)

# 生成网格举证
X, Y = np.meshgrid(x, y)

# Z 轴 函数
Z = np.power(1 - X, 2) + 100 * np.power((Y - np.power(x, 2)), 2)

# 定义x,y 轴名称
plt.xlabel("x")
plt.ylabel("y")

# 设置间隔和颜色
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="rainbow")
# 展示
plt.show()