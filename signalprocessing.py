from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

Fs = 48000 #Sample rate
Fc = 300   #Cut off frequency
        
sos = signal.butter (1, Fc, 'lp', fs=Fs, output='sos')
w, h = signal.sosfreqz(sos, worN=3000)
db = 20*np.log10(np.maximum(np.abs(h), 1e-5))
plt.plot(w/np.pi, db, label='1st Order Response')

sos = signal.butter (4, Fc, 'lp', fs=Fs, output='sos')
w, h = signal.sosfreqz(sos, worN=3000)
db = 20*np.log10(np.maximum(np.abs(h), 1e-5))
plt.plot(w/np.pi, db, 'magenta', label='4th Order Response')

sos = signal.butter (7, Fc, 'lp', fs=Fs, output='sos')
w, h = signal.sosfreqz(sos, worN=3000)
db = 20*np.log10(np.maximum(np.abs(h), 1e-5))
plt.plot(w/np.pi, db, 'cyan', label='7th Order Response')

sos = signal.butter (10, Fc, 'lp', fs=Fs, output='sos')
w, h = signal.sosfreqz(sos, worN=3000)
db = 20*np.log10(np.maximum(np.abs(h), 1e-5))
plt.plot(w/np.pi, db, 'red', label='10th Order Response')

sos = signal.butter (15, Fc, 'lp', fs=Fs, output='sos')
w, h = signal.sosfreqz(sos, worN=3000)
db = 20*np.log10(np.maximum(np.abs(h), 1e-5))
plt.plot(w/np.pi, db, 'orange', label='15th Order Response')

plt.axvline(Fc/24000, color='green', label='Cut Off Frequency') # cutoff frequency

plt.title('Filter frequency response')
plt.xlabel('Frequency [Normalized, 1=Fs/2]')
plt.ylabel('Magnitude [dB]')

plt.tight_layout()
plt.legend()
plt.show()