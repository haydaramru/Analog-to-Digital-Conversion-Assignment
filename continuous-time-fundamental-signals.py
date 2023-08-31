import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import scipy
from scipy import signal

x = []    # inisialisasi variabel x
t = []    # inisialisasi variabel t
for i in range(-5,6):
    t.append(i)
    if i==0:
        x.append(1)
    else:
        x.append(0)

print(x)
print(t)

plt.figure(figsize = (18,8)) # set the size of figure
#plt.suptitle('Constructing a Wave with different Sine Waves', fontsize = 40)
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(t,x,linewidth = 3, label = 'Unit impulse function')
plt.ylim(-0.01,1)
plt.xlim(-5,5)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

Impulse = signal.unit_impulse(10,'mid')

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(np.arange(-5, 5), Impulse, linewidth = 3, label = 'Unit impulse function')
plt.ylim(-0.01,1)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

shifted_impulse = signal.unit_impulse(7, 2)
shifted_impulse

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(shifted_impulse, linewidth = 3, label = 'Shifted impulse function (Time delay)')
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
t = []
for i in range(-5,6):
    t.append(i)
    if i== -2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(t,x,linewidth = 3, label = 'Time Shifted Impulse (Time advance)')
plt.ylim(-0.01,1)
plt.xlim(-5,5)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
t = []
for i in range(-5,10):
    t.append(i)
    if i >= 0:
        x.append(1)
    else:
        x.append(0)

print(x)
print(t)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(t,x,linewidth = 3, label = 'Unit step function')
plt.ylim(0,1.5)
plt.xlim(-5,9)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
t = []
for i in range(-5,10):
    t.append(i)
    if i >= 2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(t,x,linewidth = 3, label = 'Time Shifted Step (Time delay)')
plt.ylim(0,1.5)
plt.xlim(-5,9)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
t = []
for i in range(-5,5):
    t.append(i)
    if i >= -2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(t,x,linewidth = 3, label = 'Time Shifted Step (Time Advance)')
plt.ylim(0,1.5)
plt.xlim(-5,4)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
t = []
for i in range(0,10):
    t.append(i)
    x.append(i)

print(x)
print(t)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(t,x, linewidth = 3, label = 'Ramp function')
plt.ylim(0,len(x))
plt.xlim(0,len(t)-1)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

t = np.linspace(0,10,100)
amp = 5 # amplitude
f = 50  # frequency
x = amp * np.sin(2 * np.pi * f * t)

plt.figure(figsize = (15,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(t,x,linewidth = 3, label = 'SineWave')
plt.xlim(0,10)
plt.ylim(-5,5)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

t = np.linspace(0,10,100)
amp = 1
x = amp * np.exp(-t)

plt.figure(figsize = (15,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(t,x,linewidth = 3, label = 'Exponential Signal')
plt.xlim(0,5)
plt.ylim(0,1)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

