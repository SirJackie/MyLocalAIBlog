# f(x) = 2x^2 + x + 3
# Minimum: x = -0.25
# f(-0.25) = 2.875


def MyFunction(x):
    return 2*x**2 + x + 3


def GetGradient(MyFunction, x, dx=0.001):
    dy = MyFunction(x + dx) - MyFunction(x)
    return dy / dx


if __name__ == "__main__":
    expectedX = -0.25
    expectedY = MyFunction(expectedX)  # 2.875
    currentX = 10000
    learningRate = 0.1

    for i in range(0, 500):
        gradient = GetGradient(MyFunction, currentX)
        currentX += -gradient * learningRate

    finalX = currentX
    finalY = MyFunction(finalX)
    print("finalX: %.5f; expectedX: %.5f; errorX: %.5f" % (finalX, expectedX, abs(finalX - expectedX)))
    print("finalY: %.5f; expectedY: %.5f; errorY: %.5f" % (finalY, expectedY, abs(finalY - expectedY)))
