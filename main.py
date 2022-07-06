def myFunction(x):
    return 2*x**2 + x + 3


def getGradient(myFunction, x, dx=0.02):
    dy = myFunction(x + dx) - myFunction(x)
    return dy / dx


currentX = 9.8
learningRate = 0.01
resultX = []
resultG = []

for i in range(5000):
    resultX.append(currentX)
    gradient = getGradient(myFunction, currentX)
    resultG.append(gradient)
    currentX -= gradient * learningRate

print(resultX.pop())
print(resultG.pop())
