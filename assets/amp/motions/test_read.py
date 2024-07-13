import numpy as np

data = np.load("amp_humanoid_walk.npy", allow_pickle=True)
rot = dict(data.item())["rotation"]["arr"]
# print(len(rot))
for r in rot:
    print(r)
