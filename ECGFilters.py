import scipy.io as sio
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt


"""
Author: Wilson.Zhang
Date: 2018/11/18
Usage: Load ECG Signals mat file and NC signals using digital filters.
Reference: 
The ULg Multimodality Drowsiness Database (called DROZY) and Examples of Use.
"""

# Load ECG signals
ECG = sio.loadmat("ECG1_1.mat")["ECG1_1"]
# print(ECG, ECG.shape)


# Set Baseline Correction Filter...
# Reference: https://stackoverflow.com/questions/29156532/python-baseline-correction-library
def baseline_als(y, lam, p, niter=10):
    L = len(y)
    D = sparse.diags([1, -2, 1], [0, -1, -2], shape=(L, L-2))
    w = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
    return z


tmp = ECG[0]
res = baseline_als(tmp, 0.1, 0.1)
print(res, res.shape)

# Try to plot res out...
time = range(len(res))
plt.figure()
plt.plot(time, -res)
plt.show()
