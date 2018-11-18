import scipy.io as sio

"""
Author: Wilson.Zhang
Date: 2018/11/18
Usage: Load ECG Signals mat file and NC signals using digital filters.
Reference: 
The ULg Multimodality Drowsiness Database (called DROZY) and Examples of Use.
"""

# Load ECG signals
ECG = sio.loadmat("ECG1_1.mat")["ECG1_1"]
print(ECG, ECG.shape)

# Set filters

