import numpy as np

# === rotation ===
# === root_translation ===
# === global_velocity ===
# === global_angular_velocity ===
# === skeleton_tree ===
# === is_local ===
# === fps ===
# === __name__ ===

data = dict(np.load("amp_humanoid_run.npy", allow_pickle=True).item())

# rotation: dof_pos : [quat] * nb_dofs
# root_translation : root_pos
# global_velocity: root_vel
# global_angular_velociry : dof_vel
# skeleton_tree : ???
# is_local : true
# fps : 60
# __name__ : azeazeze
print(data["skeleton_tree"]["node_names"])
exit()
# for key in data.keys():
#     print("===", key, "===")
#     # print(data[key])
# exit()
# print(data["global_velocity"]["arr"])
# exit()
new_data = {}
new_data["rotation"] = data["rotation"]
new_data["__name__"] = data["__name__"]
new_data["root_translation"] = data["root_translation"]
new_data["global_velocity"] = data["global_velocity"]
new_data["global_angular_velocity"] = data["global_angular_velocity"]
new_data["skeleton_tree"] = {}
np.save("TEST_amp_humanoid_walk.npy", new_data, allow_pickle=True)
# rot = data["rotation"]["arr"]
# # print(len(rot))
# for r in rot:
#     print(r)
