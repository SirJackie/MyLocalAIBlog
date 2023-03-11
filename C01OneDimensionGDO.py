def myFunction(x):
    return 2*x**2 + x + 3


def getGradient(myFunction, x, dx=0.001):
    dy = myFunction(x + dx) - myFunction(x)
    return dy / dx


currentX = 9.8
learningRate = 0.0001
resultX = []
resultG = []

for i in range(500000):
    resultX.append(currentX)
    gradient = getGradient(myFunction, currentX)
    resultG.append(gradient)
    currentX -= gradient * learningRate

finalX = resultX.pop()
finalY = myFunction(finalX)
error = finalY - myFunction(-0.25)
print(finalX, finalY, error)
