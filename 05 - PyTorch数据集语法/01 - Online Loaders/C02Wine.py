from sklearn.datasets import load_wine

wine_data = load_wine()

description = wine_data.DESCR
data = wine_data.data
target = wine_data.target

print(description)
print(data)
print(target)
