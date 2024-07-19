from FramesViewer.viewer import Viewer
import numpy as np
from scipy.spatial.transform import Rotation as R
import FramesViewer.utils as fv_utils
import pickle
import time

fv = Viewer()
fv.start()

base_pose = fv_utils.make_pose([0.1, 0.1, 0.1], [0, 0, 0])
saved_obs = pickle.loads(open("saved_obs.pkl", "rb").read())
i = 0
while True:
    obs = saved_obs[i]
    base_quat = obs[:4]
    base_mat = R.from_quat(base_quat).as_matrix()

    base_pose[:3, :3] = base_mat
    fv.pushFrame(base_pose, "base", color=(255, 0, 0))
    time.sleep(1 / 30)
    i += 1
