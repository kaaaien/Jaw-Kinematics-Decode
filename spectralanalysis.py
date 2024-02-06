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
    print("new")
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 1000.0
    # Filter a noisy signal.
    T = 30
    notch_freq = 60.0
    quality_factor = 60.0
    harmonics = [notch_freq * i for i in range(2, 6)]  # First 5 harmonics of 60 Hz
    x = mat73.loadmat('../../../scratch/midway3/kaienh/MILFP.mat', use_attrdict=True)
    loaded = x['MILFP']
    data = loaded['Data'][30][0:30000] #2 mins of data. Choose 5 mins from start
    plt.figure(figsize=(10, 6))
    plt.clf()
    filterloop = data
    for harmonic_freq in harmonics:
        b_notch, a_notch = signal.iirnotch(harmonic_freq, quality_factor * harmonic_freq/60, fs)
        curr = signal.lfilter(b_notch, a_notch, filterloop)
        filterloop = curr
    psd, freqs = ghostipy.mtm_spectrum(filterloop, 15, fs=fs)
    filtered = 20 * np.log10(psd)
    plt.plot(freqs, filtered, linestyle='solid', color='blue', label='Multitaper PSD')
    # plt.psd(data, Fs=fs)
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')
    plt.show()


run()