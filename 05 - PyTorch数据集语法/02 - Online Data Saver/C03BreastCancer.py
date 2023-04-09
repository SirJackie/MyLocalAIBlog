from sklearn.datasets import load_breast_cancer
import json

cancer_data = load_breast_cancer()

description = cancer_data.DESCR
data = cancer_data.data
target = cancer_data.target

dataset = {
    "description": description,
    "data": data.tolist(),
    "target": target.tolist()
}

json_str = json.dumps(dataset)
print(json_str)

with open("D03BreastCancer.json", "wb") as f:
    f.write(json_str.encode("utf-8"))
