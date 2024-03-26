import matplotlib.pyplot as plt
import numpy as np
import os

os.system('clear')

fs = 1e6
Ts = 1/fs

n = np.array(range(int(1e6)))

fft_size = len(n)
freq = np.arange(-fs/2, fs/2, fs/fft_size)

f_sig = .1e6

i = np.real(np.exp(1j*2*np.pi*f_sig/fs*n))
q = np.real(np.exp(1j*2*np.pi*f_sig/fs*n))*np.exp(np.pi/2)

complex = i + q

i_fft = np.fft.fftshift(np.fft.fft(i, n=fft_size))/fft_size
q_fft = np.fft.fftshift(np.fft.fft(q, n=fft_size))/fft_size

plt.subplot(2,1,1)
plt.stem(Ts*n[1:100], i[1:100], 'r', label='In-Phase')
plt.stem(Ts*n[1:100], q[1:100], 'g', label='Quadrature-Phase')
plt.legend()

plt.subplot(2,2,3)
plt.plot(freq, np.real(i_fft), label='In-Phase')
plt.plot(freq, np.real(q_fft), label='Quadrature-Phase')
plt.legend()

plt.subplot(2,2,4)
plt.plot(freq, np.imag(i_fft), label='In-Phase')
plt.plot(freq, np.imag(q_fft), label='Quadrature-Phase')
plt.legend()

plt.show()