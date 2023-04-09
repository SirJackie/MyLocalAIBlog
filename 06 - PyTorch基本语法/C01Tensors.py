import torch


alist = [1, 2, 3, 4, 5]
tensor = torch.tensor(alist, dtype=torch.float)
print(tensor)

zeros_tensor = torch.zeros(5)
ones_tensor = torch.ones(5)
random_tensor = torch.rand(5)
normal_tensor = torch.randn(5)  # normal distribution

print(zeros_tensor)
print(ones_tensor)
print(random_tensor)
print(normal_tensor)

sliced_tensor = normal_tensor[:3]
print(sliced_tensor)

random_list = random_tensor.tolist()
print(random_list)
