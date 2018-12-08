import scipy.signal as signal
import scipy.io as sio
import matplotlib.pyplot as plt

import numpy as np

import math
from scipy.signal import butter, lfilter


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):    
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)    
    y = lfilter(b, a, data)    
    return y


def butter_bandpass(lowcut, highcut, fs, order=5):    
    nyq = 0.5 * fs    
    low = lowcut / nyq    
    high = highcut / nyq   
    b, a = butter(order, [low, high], btype='band')
    return b, a


sampRat = 512
dt = 1/sampRat
T = 30

t = np.linspace(0, T, T*sampRat, endpoint=False)
y = sio.loadmat("ECG2_1.mat")["ECG2_1"][5]

filterY = butter_bandpass_filter(y, 5, 12, sampRat, 3)
time = range(len(filterY))
plt.figure(1)
plt.plot(time, y)
plt.show()

plt.figure(2)
plt.plot(time, filterY)
plt.show()

# f = np.linspace(0, sampRat, T*sampRat, endpoint=False)
#
# ff = np.fft.fft(y)
# ff = np.abs(ff)*2/T/sampRat
#
# plt.figure(2)
# plt.plot(f, ff)
# plt.title('滤波前的频谱')
# plt.show()
#
# ff = np.fft.fft(filterY)
# ff = np.abs(ff)*2/T/sampRat
#
# plt.figure(3)
# plt.plot(f, ff)
# plt.title('滤波后的频谱')
# plt.show()
