import json

seeds_data = None
with open("D04Seeds.json", "rb") as f:
    seeds_data = f.read().decode("utf-8")
    seeds_data = json.loads(seeds_data)

description = seeds_data["description"]
data = seeds_data["data"]
target = seeds_data["target"]

print(description)
print(data)
print(target)
