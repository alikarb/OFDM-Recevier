import random
import matplotlib.pyplot as plt
import numpy as np
from math import ceil
import komm
from scipy import special

number_error = 100
step = 0.5
stop = 10
ebn0 = np.arange(0, stop+step, step)
packet_size = int(1e4)
fs = 1
ber_bpsk = []

qpsk = komm.PSKModulation(order=4, phase_offset=np.pi/4)
bpsk = komm.PSKModulation(order=2)

for snr in ebn0:
    ebn0_bpsk = 10**(snr/10)

    n0_bpsk = 1/ebn0_bpsk
    var_bpsk = n0_bpsk*fs/2

    error_count_bpsk = 0
    packet_count = 0
    while error_count_bpsk < number_error:
        packet_count +=1
        bits = (np.sign(np.random.randn(packet_size)) + 1)/2
        symbols_bpsk = bpsk.modulate(bits)

        noise_bpsk = np.sqrt(var_bpsk)*np.random.randn(len(symbols_bpsk))

        signal_bpsk = symbols_bpsk + noise_bpsk

        received_bits_bpsk = bpsk.demodulate(signal_bpsk)

        for a,b in zip(bits, received_bits_bpsk):
            if a != b:
                error_count_bpsk += 1
        
        print(f'SNR: {snr}dB\nPacket Count: {packet_count}\nError Count (BPSK): {error_count_bpsk}\n')
    ber_bpsk.append(error_count_bpsk/(packet_count*packet_size))

ideal_ber = 0.5*special.erfc(np.sqrt(10**(ebn0/10)))

plt.semilogy(ebn0, ber_bpsk, label='Simulated BPSK', linestyle='none', marker='.')
plt.semilogy(ebn0, ideal_ber, label='Ideal BER', linestyle='none', marker='.')
plt.legend()
plt.show()