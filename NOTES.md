# Notes

- "Long" motion example seem to work best (130 seconds)
  - bdx_walk.txt : 130 seconds of walking forwards with placo walk engine
- disc_grad_penalty : 10

There is a phase during training when the robot does not move and stands still. The learning process amazingly overcomes this state and the robot starts walking afterwards

## Exporting
- onnx are torch.jit.save are the same.
