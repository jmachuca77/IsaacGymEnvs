# Training notes

- In branch `amp_no_root`, trying to get the model to work without having the root orientation and position. 
  - For now, hard
  - Probably need linear and angular velocity to learn properly ? Should be ok, we just want the model to be invariant to the position and orientation
  - Can't seem to learn the walk without the absolute orientation. Will try to at least keep only roll and pitch, discarding yaw.
- examples directly from placo seem harder to learn than when recording through mujoco. 
- Maybe I'm too aggressive with the randomization? kept vanilla ones, but maybe I should try to reduce them.
- At some point I want to re introduce random pushes

## Plan
1) Get a simple walking in place policy working in isaac -> mujoco -> real robot []
2) Introduce commands
   - Train (from checkpoint?) with velocity tracking []
   - Or, train with different animations. Find a way to select the correct reference animation depending on the commands []

## TODO

Check (again) velocity tracking reward. Scales of the commands etc

### Stiffness and damping 
- No idea what parameters to use here. 
- With 20 stiffness and 1 damping, seem to be able to learn a good walking policy. But what are the units ? how to convert to mujoco and real robot ???
- Training with 0.5 0.5 amp + task seem not to work. 
  
### Current training
Trying to establish a working baseline with the current parameters:
- 20 stiffness, 1 damping
- 1.0 amp 0.0 task
- No randomization
- (No root orientation and position) EDIT need orientation finally
- walk in place animation EDIT does not seem to work. Trying with forward