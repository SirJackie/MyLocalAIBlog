import json

iris_data = None
with open("D01Iris.json", "rb") as f:
    iris_data = f.read().decode("utf-8")
    iris_data = json.loads(iris_data)

description = iris_data["description"]
data = iris_data["data"]
target = iris_data["target"]

print(description)
print(data)
print(target)
