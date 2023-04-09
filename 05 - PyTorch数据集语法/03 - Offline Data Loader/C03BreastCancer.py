import json

cancer_data = None
with open("D03BreastCancer.json", "rb") as f:
    cancer_data = f.read().decode("utf-8")
    cancer_data = json.loads(cancer_data)

description = cancer_data["description"]
data = cancer_data["data"]
target = cancer_data["target"]

print(description)
print(data)
print(target)
