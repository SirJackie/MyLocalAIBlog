import json

wine_data = None
with open("D02Wine.json", "rb") as f:
    wine_data = f.read().decode("utf-8")
    wine_data = json.loads(wine_data)

description = wine_data["description"]
data = wine_data["data"]
target = wine_data["target"]

print(description)
print(data)
print(target)
