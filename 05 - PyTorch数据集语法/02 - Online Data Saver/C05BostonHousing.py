from sklearn.datasets import load_boston
import json

boston_data = load_boston()

description = boston_data.DESCR
data = boston_data.data
target = boston_data.target

dataset = {
    "description": description,
    "data": data.tolist(),
    "target": target.tolist()
}

json_str = json.dumps(dataset)
print(json_str)

with open("D05BostonHousing.json", "wb") as f:
    f.write(json_str.encode("utf-8"))
