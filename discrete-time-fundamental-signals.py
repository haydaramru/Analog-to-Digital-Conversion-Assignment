import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import scipy
from scipy import signal

x = []
n = []                  # t = nT. Since we are performing uniform sampling, therefore, T=1.
for i in range(-5,6):
    n.append(i)
    if i==0:
        x.append(1)
    else:
        x.append(0)

print(x)
print(n)

plt.figure(figsize = (18,8)) # set the size of figure
#plt.suptitle('Constructing a Wave with different Sine Waves', fontsize = 40)
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.stem(n,x,'yo', label = 'Unit impulse function')
plt.ylim(-0.01,1.2)
plt.xlim(-5,5)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
n = []
for i in range(-5,6):
    n.append(i)
    if i== 2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.stem(n,x,'yo', label = 'Time Shifted Impulse (Time delay)')
plt.ylim(-0.01,1.2)
plt.xlim(-5,5)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
n = []
for i in range(-5,6):
    n.append(i)
    if i== -2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.stem(n,x,'yo', label = 'Time Shifted Impulse (Time advance)')
plt.ylim(-0.01,1.2)
plt.xlim(-5,5)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
n = []
for i in range(-5,10):
    n.append(i)
    if i >= 0:
        x.append(1)
    else:
        x.append(0)

print(x)
print(n)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.stem(n,x,'yo', label = 'Unit step function')
plt.ylim(0,1.5)
plt.xlim(-5,9)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
n = []
for i in range(-5,10):
    n.append(i)
    if i >= 2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.stem(n,x,'yo', label = 'Time Shifted Step (Time delay)')
plt.ylim(0,1.5)
plt.xlim(-5,9)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
n = []
for i in range(-5,5):
    n.append(i)
    if i >= -2:
        x.append(1)
    else:
        x.append(0)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.stem(n,x,'yo', label = 'Time Shifted Step (Time Advance)')
plt.ylim(0,1.5)
plt.xlim(-5,4)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

x = []
n = []
for i in range(0,10):
    n.append(i)
    x.append(i)

print(x)
print(n)

plt.figure(figsize = (18,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.stem(n,x,'yo', label = 'Ramp function')
plt.ylim(0,len(x))
plt.xlim(0,len(n)-1)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 20)
plt.show()

n = np.linspace(0,10,100)
amp = 5 # amplitude
f = 50  # frequency
x = amp * np.sin(2 * np.pi * f * n)

plt.figure(figsize = (18,12)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.stem(n,x,'yo', label = 'SineWave')
plt.ylim(-5,5)
plt.xlim(0,10)
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.legend(fontsize = 15)
plt.show()

n = np.linspace(0,10,100)
amp = 1
x = amp * np.exp(-n)

plt.figure(figsize = (15,8)) # set the size of figure
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.stem(n,x,'yo', label = 'Exponential Signal')
plt.xlabel('time.', fontsize = 15)
plt.ylabel('Amplitude', fontsize = 15)
plt.xlim(0,5)
plt.ylim(0,1)
plt.legend(fontsize = 20)
plt.show()

