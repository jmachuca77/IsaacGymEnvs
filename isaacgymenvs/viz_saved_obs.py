import argparse
import pickle
import time

import FramesViewer.utils as fv_utils
import numpy as np
from FramesViewer.viewer import Viewer
from scipy.spatial.transform import Rotation as R

parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str, default="saved_obs.pkl")
args = parser.parse_args()

fv = Viewer()
fv.start()

base_pose = fv_utils.make_pose([0.1, 0.1, 0.1], [0, 0, 0])
ang_vel_pose = fv_utils.make_pose([0.1, 0.2, 0.1], [0, 0, 0])
ang_vel_euler = [0, 0, 0]
ang_vel_mat = np.eye(3)

saved_obs = pickle.loads(open(args.path, "rb").read())
i = 0
while True:
    obs = saved_obs[i]
    base_quat = obs[:4]
    ang_vel = obs[4:7]

    base_mat = R.from_quat(base_quat).as_matrix()
    base_pose[:3, :3] = base_mat
    fv.pushFrame(base_pose, "base", color=(255, 0, 0))

    ang_vel_euler += np.deg2rad(ang_vel * 4)
    ang_vel_mat = np.eye(3)
    ang_vel_mat[:3, :3] = R.from_euler("xyz", ang_vel_euler).as_matrix()

    ang_vel_pose[:3, :3] = ang_vel_mat
    fv.pushFrame(ang_vel_pose, "ang_vel", color=(0, 255, 0))

    time.sleep(1 / 60)
    i += 1
