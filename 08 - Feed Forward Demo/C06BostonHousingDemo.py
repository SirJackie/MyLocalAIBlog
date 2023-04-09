from sklearn.datasets import load_boston

boston_data = load_boston()

description = boston_data.DESCR
data = boston_data.data
target = boston_data.target

print(description)
print(data)
print(target)
