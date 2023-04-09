import pandas as pd
import json

# 从CSV文件中加载Seeds数据集
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt'
url = './seeds_dataset.txt'  # Localized Dataset File
seeds_data = pd.read_csv(url, header=None, delim_whitespace=True)

# 获取特征和目标数据
description = '''The Seeds dataset is a well-known dataset used in machine learning and pattern recognition research. It contains measurements of different geometrical properties of three different types of wheat seeds: Kama, Rosa, and Canadian.
The dataset consists of seven different attributes or features of each seed, including area, perimeter, compactness, length of kernel, width of kernel, asymmetry coefficient, and length of kernel groove. These features were measured from digital images of the seeds taken with a high-resolution camera.
There are a total of 210 instances or samples in the dataset, with 70 samples for each of the three wheat seed types. The dataset is commonly used to test classification algorithms and to explore the relationship between the different features and the type of seed.
The Seeds dataset is a popular benchmark for comparing different machine learning models, and it has been used in numerous research papers and studies. It is freely available online and can be easily downloaded for use in various machine learning and data analysis projects.'''
data = seeds_data.iloc[:, :-1].values
target = seeds_data.iloc[:, -1].values
target = target - 1  # 1, 2, 3 to 0, 1, 2

dataset = {
    "description": description,
    "data": data.tolist(),
    "target": target.tolist()
}

json_str = json.dumps(dataset)
print(json_str)

with open("D04Seeds.json", "wb") as f:
    f.write(json_str.encode("utf-8"))
