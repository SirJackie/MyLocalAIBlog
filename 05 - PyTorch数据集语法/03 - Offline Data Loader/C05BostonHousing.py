import json

boston_data = None
with open("D05BostonHousing.json", "rb") as f:
    boston_data = f.read().decode("utf-8")
    boston_data = json.loads(boston_data)

description = boston_data["description"]
data = boston_data["data"]
target = boston_data["target"]

print(description)
print(data)
print(target)
