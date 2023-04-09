from sklearn.datasets import load_wine
import json

wine_data = load_wine()

description = wine_data.DESCR
data = wine_data.data
target = wine_data.target

dataset = {
    "description": description,
    "data": data.tolist(),
    "target": target.tolist()
}

json_str = json.dumps(dataset)
print(json_str)

with open("D02Wine.json", "wb") as f:
    f.write(json_str.encode("utf-8"))
