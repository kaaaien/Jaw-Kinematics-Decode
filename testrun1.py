from scipy import signal
from scipy.io import loadmat
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

Fs = 48000 #Sample rate
Fc = 300   #Cut off frequency
t = np.linspace(0, 0.125, Fs , False)  # 1/8 second
sig = loadmat('../Neuro/e196/Neural data/MILFP.mat')

sos = signal.butter (2, Fc, 'lp', fs=Fs, output='sos')
w, h = signal.sosfreqz(sos, worN=3000)
filtsig = signal.sosfilt(sos, sig)
plt.plot(t, filtsig)

plt.title('Test run on LFP data')
plt.xlabel('Frequency [Normalized, 1=Fs/2]') #half of sampling rate
plt.ylabel('Magnitude [dB]')

plt.tight_layout()
plt.legend()
plt.show()