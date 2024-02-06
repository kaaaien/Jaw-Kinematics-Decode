import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, lfilter
import mat73
import ghostipy

def run():
    fs = 1000.0
    T = 30
    notch_freq = 60.0
    quality_factor = 60.0
    wharmonics = [notch_freq * i for i in range(2, 8)]  # First 2-7 harmonics of 60 Hz
    mtmharmonics = [notch_freq * i for i in range(2, 6)]  # First 2-5 harmonics of 60 Hz

    x = mat73.loadmat('../../../scratch/midway3/kaienh/MILFP.mat', use_attrdict=True)
    loaded = x['MILFP']
    data = loaded['Data'][30][0:30000] #Import data


    wfilterloop = data #create loop that repeatedly applies notch filter to make it harmonic, this is for welch method
    for harmonic_freq in wharmonics:
        b_notch, a_notch = iirnotch(harmonic_freq, 4*quality_factor * harmonic_freq/60, fs) #using different quality factor
        curr = lfilter(b_notch, a_notch, wfilterloop)
        wfilterloop = curr
    wpsd, wfreqs = plt.psd(wfilterloop, Fs=fs, visible=False) #compute the welch psd
    wfiltered = 20 * np.log10(wpsd) #apply log

    mtmfilterloop = data #same thing for multitaper method
    for harmonic_freq in mtmharmonics:
        b_notch, a_notch = iirnotch(harmonic_freq, quality_factor * harmonic_freq/60, fs)
        curr = lfilter(b_notch, a_notch, mtmfilterloop)
        mtmfilterloop = curr
    mtmpsd, mtmfreqs = ghostipy.mtm_spectrum(mtmfilterloop, 15, fs=fs) #compute the multitaper psd
    mtmfiltered = 20 * np.log10(mtmpsd) #apply log

    plt.plot(wfreqs, wfiltered, linestyle='solid', color='blue', label="Filtered PSD") #plot welch psd
    plt.plot(mtmfreqs, mtmfiltered, linestyle='solid', color='orange', label="Multitaper PSD") #plot multitaper psd
    # mse = np.square(np.subtract(mtmpsd, wpsd)).mean()
    #this MSE code doesn't work

    plt.grid(True)
    plt.axis('tight')
    # plt.legend([mse],loc='upper left')
    plt.legend(loc='upper left')
    plt.show()

run()