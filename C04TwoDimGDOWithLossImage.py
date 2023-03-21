from math import sqrt
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# z = x*x + y*y
def MyFunction(x, y):
    return x*x + y*y


def GetXDirectionDerivative(function, fixedY, x, dx=0.001):
    dz = function(x + dx, fixedY) - function(x - dx, fixedY)
    return dz / (2 * dx)


def GetYDirectionDerivative(function, fixedX, y, dy=0.001):
    dz = function(fixedX, y + dy) - function(fixedX, y - dy)
    return dz / (2 * dy)


def GetGradient(function, x, y):
    xDerivative = GetXDirectionDerivative(MyFunction, x, y)
    yDerivative = GetYDirectionDerivative(MyFunction, x, y)
    return xDerivative, yDerivative  # returns a tuple, format is (dx, dy)


def TestGradientCalculators():
    print(MyFunction(0, 0))
    print(MyFunction(-10, -10))
    print(GetGradient(MyFunction, 0, 0))
    print(GetGradient(MyFunction, -10, -10))


if __name__ == "__main_":
    TestGradientCalculators()


if __name__ == "__main__":
    # Store X and Y History
    xHis = []
    yHis = []

    # Set Parameters
    expectedX = 0
    expectedY = 0
    expectedZ = MyFunction(expectedX, expectedY)  # 0.0

    currentX = -10
    currentY = -10
    learningRate = 0.1

    # Iterate
    for i in range(0, 500):
        xHis.append(currentX)
        yHis.append(currentY)

        gradient = GetGradient(MyFunction, currentX, currentY)
        currentX += -gradient[0] * learningRate
        currentY += -gradient[1] * learningRate

    # Final Result
    xHis.append(currentX)
    yHis.append(currentY)
    finalX = currentX
    finalY = currentY
    finalZ = MyFunction(finalX, finalY)

    # Output
    print("finalX: %.5f; expectedX: %.5f; errorX: %.5f" % (finalX, expectedX, abs(finalX - expectedX)))
    print("finalY: %.5f; expectedY: %.5f; errorY: %.5f" % (finalY, expectedY, abs(finalY - expectedY)))
    print("finalZ: %.5f; expectedZ: %.5f; errorZ: %.5f" % (finalZ, expectedZ, abs(finalZ - expectedZ)))

    print(xHis)
    print(yHis)

    # 新建一个画布
    figure = plt.figure()
    # 新建一个3d绘图对象
    ax = Axes3D(figure, auto_add_to_figure=False)
    figure.add_axes(ax)

    # 生成x, y 的坐标集 (-2,2) 区间，间隔为 0.1
    x = np.arange(-10, 10.1, 0.5)
    y = np.arange(-10, 10.1, 0.5)

    # 生成网格矩阵
    X, Y = np.meshgrid(x, y)

    # Z 轴 函数
    # z = x*x + y*y
    Z = X * X + Y * Y

    # 定义x,y 轴名称
    plt.xlabel("x")
    plt.ylabel("y")

    # 绘制梯度散点
    zHis = []
    for i in range(0, len(xHis)):
        zHis.append(MyFunction(xHis[i], yHis[i]))

    ax.plot(xs=xHis, ys=yHis, zs=zHis, c="g", marker="X")

    # 绘制曲面
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="rainbow", alpha=0.5)

    # 展示
    plt.show()
