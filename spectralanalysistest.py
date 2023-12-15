from scipy import signal
from scipy.io import wavfile, whosmat
import mat73
import ghostipy

#TODO: compute power spectrum - plot power spectrum for all channels
# are there any bad channels?
#TODO: Compute power spectrum from 0 - 200Hz and look for peaks
#TODO: Play with selection of data channels and data length time frame
#TODO: IMPORTANT - move MILFP.mat to scratch and use it from there

def run():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 1000.0
    # Filter a noisy signal.
    T = 120
    x = mat73.loadmat('MILFP.mat', use_attrdict=True)
    loaded = x['MILFP']
    data_prelog = loaded['Data'][40][0:120000] #15 mins of data. Choose 5 mins from start
    data = np.log10(data_prelog) * 20
    plt.figure(1)
    plt.clf()
    psd, freqs = ghostipy.mtm_spectrum(data_prelog, 15, fs=fs) # use 25 ish for bandwidth 

    plt.plot(freqs, psd)
    # plt.psd(data, Fs=fs)
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')
    plt.show()


run()