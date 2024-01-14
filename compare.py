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
    print("test")
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 1000.0
    # Filter a noisy signal.
    T = 120
    notch_freq = 120.0  # Frequency to be removed from signal (Hz)
    quality_factor = 20.0  # Quality factor 
    x = mat73.loadmat('../../../scratch/midway3/kaienh/MILFP.mat', use_attrdict=True)
    loaded = x['MILFP']
    data = loaded['Data'][40][0:120000] #2 mins of data. Choose 5 mins from start
    plt.figure(1)
    plt.clf()
    # psd, freqs = ghostipy.mtm_spectrum(data, 15, fs=fs) # use 25 ish for bandwidth
    psd, freqs = plt.psd(data, Fs=fs)
    psd_log = np.log10(psd) * 20
    b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, fs)  
    notched = signal.filtfilt(b_notch, a_notch, psd_log)
    plt.plot(freqs, notched)

    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')
    plt.show()


run()