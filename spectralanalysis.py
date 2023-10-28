from scipy import signal
from scipy.io import wavfile, whosmat
import mat73
import ghostipy

#TODO: compute power spectrum - plot power spectrum for all channels
# are there any bad channels?
#TODO: Compute power spectrum from 0 - 200Hz and look for peaks
#TODO: Play with selection of data channels and data length time frame


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y

def run():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 1000.0
    lowcut = 15.0
    highcut = 35.0
    # Filter a noisy signal.
    T = 120
    nsamples = int(T * fs)
    
    t = np.linspace(0, T, nsamples, endpoint=False)
    x = mat73.loadmat('../Neuro/e196/Neural data/MILFP.mat', use_attrdict=True)
    loaded = x['MILFP']
    data = loaded['Data'][32][0:120000] #5-10 mins of data. Choose 5 mins from start
    plt.figure(2)
    plt.clf()
    plt.plot(t, data, label='Noisy signal')

    y = butter_bandpass_filter(data, lowcut, highcut, fs, order=6) #play around with order 
    final = ghostipy.mtm_spectrum(y, highcut-lowcut, fs)
    plt.plot(t, final, label='Filtered signal (test Hz)')
    plt.xlabel('time (seconds)')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')

    plt.show()


run()