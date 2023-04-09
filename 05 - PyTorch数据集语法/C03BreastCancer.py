from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer()

description = cancer_data.DESCR
data = cancer_data.data
target = cancer_data.target

print(description)
print(data)
print(target)
