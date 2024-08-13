import pickle
import numpy as np
import matplotlib.pyplot as plt

isaac_torques = pickle.load(open("isaac_torques.pkl", "rb"))
custom_torques = pickle.load(open("custom_torques.pkl", "rb"))

nb_dofs = 15

isaac_dofs_torques = np.zeros((nb_dofs, len(isaac_torques)))
custom_dofs_torques = np.zeros((nb_dofs, len(custom_torques)))

for i in range(len(isaac_torques)):
    isaac_dofs_torques[:, i] = isaac_torques[i]

for i in range(len(custom_torques)):
    custom_dofs_torques[:, i] = custom_torques[i]


# one plot per dof in one figure
# compare torques

nb_rows = int(np.sqrt(nb_dofs))
nb_cols = int(np.ceil(nb_dofs / nb_rows))

fig, axs = plt.subplots(nb_rows, nb_cols, sharex=True, sharey=True)

for i in range(nb_rows):
    for j in range(nb_cols):
        if i * nb_cols + j >= nb_dofs:
            break

        axs[i, j].plot(isaac_dofs_torques[i * nb_cols + j], label="isaac")
        axs[i, j].plot(custom_dofs_torques[i * nb_cols + j], label="custom")
        axs[i, j].set_title(f"dof {i * nb_cols + j}")
        axs[i, j].legend()

plt.show()
