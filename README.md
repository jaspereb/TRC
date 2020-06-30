# TRC
Supporting code and hardware designs for the paper on monocular depth prediction in the agricontrol conference https://doi.org/10.1016/j.ifacol.2019.12.565. The repository name comes from Time-of-flight + Rgb + Cnn (TRC). Network predictions for the NYUv2 dataset are shown in the 'Sample Outputs' directory.

# Paper Information
All of the results in the paper were generated using this code which is an adaptation of [Sparse to Dense](https://github.com/fangchangma/sparse-to-dense.pytorch) by Ma and Karaman (2018).

The 'Experiment Results' spreadsheet tracks all of the experiments which were run, the actual commands used to generate these results can be found in 'trainCMD by Exp Num'. If the training parameter is not set (or noted) in that text file, then the default value from 'utils.py' was used.

# Software
To get started, have a look through [Sparse to Dense](https://github.com/fangchangma/sparse-to-dense.pytorch) because it is a fork of this. Several features are added to the original code, mostly the additional sampling methods but also functionality for fine tuning a network with new train parameters. 

You should be able to activate the virtual environment with `source stodEnv/bin/activate` then install pyTorch, download NYUv2 or Kitti using the commands in Sparse to Dense, and run the experiment command
`python3 main.py -a resnet50 -d upproj -m rgbd -b 16 --sparsifier statsam --variable-focal --variable-scale --data nyudepthv2`
which will sample a single depth point at [114,192] with simulated variable focal length and variable object scale. 

# Hardware
All of the hardware used in the test rig was modelled in Solidworks and 3D printed. Files for this are provided along with code to read a VL53L0X sensor, as both a matlab ROS node and arduino code. The two cameras are read via an RPi3 and a Pi Zero both of which run ROS nodes with OpenCV. The realsense is read using the standard ROS wrapper for that. 

Open the 'TRC Assem.SLDASM' file
