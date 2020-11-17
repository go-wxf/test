import torch
from torch.backends import cudnn  # 如正常则静默
a = torch.tensor([23])
print(torch.tensor([1, 2]))
x = 'fdsjkl'.replace('fds', 'wxf')
a = torch.Tensor([1.])  # 如正常则静默
print(a.cuda())  # 如正常则返回"tensor([ 1.], device='cuda:0')"
print(cudnn.is_acceptable(a.cuda()))  # 如正常则返回 "True"
