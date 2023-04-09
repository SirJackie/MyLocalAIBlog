from sklearn.datasets import load_iris

iris_data = load_iris()

description = iris_data.DESCR
data = iris_data.data
target = iris_data.target

print(description)
print(data)
print(target)
