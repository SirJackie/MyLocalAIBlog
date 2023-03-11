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


if __name__ == "__main__":
    TestGradientCalculators()
