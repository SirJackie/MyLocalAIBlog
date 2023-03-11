from math import sqrt, fabs


# z = 100 - sqrt(abs( 10000 - (x-2)^2 - (y-4)^2 ))
def MyFunction(x, y):
    return 100 - sqrt(
        fabs(
            10000 - (x-2)**2 - (y-4)**2
        )
    )


def GetXDirectionDerivative(function, fixedY, x, dx=0.001):
    dz = function(x + dx, fixedY) - function(x, fixedY)
    return dz / dx


def GetYDirectionDerivative(function, fixedX, y, dy=0.001):
    dz = function(fixedX, y + dy) - function(fixedX, y)
    return dz / dy


def GetGradient(function, x, y):
    xDerivative = GetXDirectionDerivative(MyFunction, x, y)
    yDerivative = GetYDirectionDerivative(MyFunction, x, y)
    return xDerivative, yDerivative  # returns a tuple, format is (dx, dy)


def TestGradientCalculators():
    print(MyFunction(2, 4))
    print(MyFunction(-10, -10))

    print(GetXDirectionDerivative(MyFunction, -10, -10))
    print(GetYDirectionDerivative(MyFunction, -10, -10))

    print(GetGradient(MyFunction, -10, -10))


if __name__ == "__main_":
    print(GetGradient(MyFunction, -10, -10))


if __name__ == "__main__":
    expectedX = 2
    expectedY = 4
    expectedZ = MyFunction(expectedX, expectedY)  # 0.0

    currentX = -10
    currentY = -10
    learningRate = 1

    for i in range(0, 5000):
        gradient = GetGradient(MyFunction, currentX, currentY)
        print(currentX, currentY, gradient)
        currentX += -gradient[0] * learningRate
        currentY += -gradient[1] * learningRate

    finalX = currentX
    finalY = currentY
    finalZ = MyFunction(finalX, finalY)
    print("finalX: %.5f; expectedX: %.5f; errorX: %.5f" % (finalX, expectedX, abs(finalX - expectedX)))
    print("finalY: %.5f; expectedY: %.5f; errorY: %.5f" % (finalY, expectedY, abs(finalY - expectedY)))
    print("finalZ: %.5f; expectedZ: %.5f; errorZ: %.5f" % (finalZ, expectedZ, abs(finalZ - expectedZ)))
