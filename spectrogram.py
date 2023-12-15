from scipy import signal
from scipy.io import wavfile, whosmat, loadmat
import mat73
import ghostipy

def run():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 1000.0
    # Filter a noisy signal.
    T = 900
    
    x = loadmat('../Neuro/e196/kin\ analysis/ChewCerebus.mat')
    loaded = x['e196t03']
    data = loaded[:,1]
    plt.figure(1)
    plt.clf()
    psd, freqs = ghostipy.mtm_spectrogram(data, )
    plt.plot(freqs, psd)
    # plt.psd(data, Fs=fs)
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')
    plt.show()


run()