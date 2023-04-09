from sklearn.datasets import load_iris
import json

iris_data = load_iris()

description = iris_data.DESCR
data = iris_data.data
target = iris_data.target

dataset = {
    "description": description,
    "data": data.tolist(),
    "target": target.tolist()
}

json_str = json.dumps(dataset)
print(json_str)

with open("D01Iris.json", "wb") as f:
    f.write(json_str.encode("utf-8"))
