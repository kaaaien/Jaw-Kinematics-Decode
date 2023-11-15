from scipy import signal
from scipy.io import wavfile, whosmat, loadmat
import mat73
import ghostipy

#TODO: compute power spectrum - plot power spectrum for all channels
# are there any bad channels?
#TODO: Compute power spectrum from 0 - 200Hz and look for peaks
#TODO: Play with selection of data channels and data length time frame


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
    data = loaded[:,1] #15 mins of data. Choose 5 mins from start
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