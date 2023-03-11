from math import sqrt, fabs


# z = 100 - sqrt(abs( 10000 + ( 1 - (x-2)^2 - (y-4)^2 ) ))
def MyFunction(x, y):
    return 100 - sqrt(
        fabs(
            10000 + (1 - (x-2)**2 - (y-4)**2)
        )
    )


print(MyFunction(2, 4))
print(MyFunction(-10, -10))
