import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, lfilter
import mat73

def run():
    fs = 1000.0
    T = 30
    notch_freq = 60.0
    quality_factor = 240.0
    harmonics = [notch_freq * i for i in range(2, 8)]  # First 5 harmonics of 60 Hz

    x = mat73.loadmat('../../../scratch/midway3/kaienh/MILFP.mat', use_attrdict=True)
    loaded = x['MILFP']
    data = loaded['Data'][30][0:30000]

    # Plot original PSD
    plt.figure(figsize=(10, 6))
    # psd_original, freqs = plt.psd(data, Fs=fs, visible=False)
    # psd_original_log = 20 * np.log10(psd_original)
    # plt.plot(freqs, psd_original_log, label='Original Welch PSD', linestyle='solid', color='orange')

    filterloop = data
    for harmonic_freq in harmonics:
        b_notch, a_notch = iirnotch(harmonic_freq, quality_factor * harmonic_freq/60, fs)
        curr = lfilter(b_notch, a_notch, filterloop)
        filterloop = curr
    psd, freqs = plt.psd(filterloop, Fs=fs, visible=False)
    filtered = 20 * np.log10(psd)

    plt.plot(freqs, filtered, linestyle='solid', color='blue', label="Welch PSD")

    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')
    plt.show()

run()