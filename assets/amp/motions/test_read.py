import numpy as np

data = dict(np.load("amp_humanoid_walk.npy", allow_pickle=True).item())

# print(data["global_velocity"]["arr"])
# exit()
new_data = {}
new_data["rotation"] = data["rotation"]
new_data["__name__"] = data["__name__"]
new_data["root_translation"] = data["root_translation"]
new_data["global_velocity"] = data["global_velocity"]
new_data["global_angular_velocity"] = data["global_angular_velocity"]
new_data["skeleton_tree"] = data["skeleton_tree"]
np.save("TEST_amp_humanoid_walk.npy", new_data, allow_pickle=True)
# rot = data["rotation"]["arr"]
# # print(len(rot))
# for r in rot:
#     print(r)
