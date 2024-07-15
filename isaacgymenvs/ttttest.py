import torch

policy = torch.jit.load("TEST.pt")
num_obs = 54
input = torch.zeros(1, num_obs).to(device="cuda:0")
print(policy(input)[0].cpu().detach().numpy()[0])
