import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

f = 20;  # Hz
t = np.linspace(0,0.5,200);
x1 = np.sin(2 * np.pi * f * t)

srate = 35  # Hz. Here the sampling frequency is less than the requirement of sampling theorem
T = 1/srate;
n = np.arange(0, 0.5/T);
nT = n*T
x2 = np.sin(2 * np.pi * f * nT)  # Since for sampling t = nT.

# Plotting

plt.figure(figsize = (24,18)) # set the size of figure
plt.suptitle('Sampling a Sine wave of Fmax = 20Hz with fs = 35 Hz', fontsize = 40)
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15


plt.subplot(2,2,1) 
plt.plot(t,x1,linewidth = 3) 
plt.title('SineWave of frequency 20 Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,2)
plt.plot(nT,x2,'ro',linewidth = 3)
plt.title('Sample marks after resampling at fs = 35Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,3)
plt.stem(nT,x2,'m')
plt.title('Sample after resampling at fs = 35Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,4)
plt.plot(nT,x2,'g-',linewidth = 3)
plt.title('Reconstruted Sine wave', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.show()

f = 20;  # Hz
t = np.linspace(0,0.5,200);
x1 = np.sin(2 * np.pi * f * t)

srate = 50  # Hz. or fs = 50 Hz

T = 1/srate;

n = np.arange(0, 0.5/T);

nT = n*T

x2 = np.sin(2 * np.pi * f * nT)  # Since for sampling t = nT.

# Plotting

plt.figure(figsize = (24,18)) # set the size of figure
plt.suptitle('Sampling a Sine wave of Fmax = 20Hz with fs = 50 Hz', fontsize = 40)
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15


plt.subplot(2,2,1) 
plt.plot(t,x1,linewidth = 3) 
plt.title('SineWave of frequency 20 Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,2)
plt.plot(nT,x2,'ro',linewidth = 3)
plt.title('Sample marks after resampling at fs = 50Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,3)
plt.stem(nT,x2,'m')
plt.title('Sample after resampling at fs = 50Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,4)
plt.plot(nT,x2,'g-',linewidth = 3)
plt.title('Reconstruted Sine wave', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.show()

f = 20;  # Hz
t = np.linspace(0,0.5,200);
x1 = np.sin(2 * np.pi * f * t)

srate = 100  # Hz. 

T = 1/srate;

n = np.arange(0, 0.5/T);

nT = n*T

x2 = np.sin(2 * np.pi * f * nT)  # Since for sampling t = nT.

# Plotting

plt.figure(figsize = (24,18)) # set the size of figure
plt.suptitle('Sampling a Sine wave of Fmax = 20Hz with fs = 100 Hz', fontsize = 40)
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15


plt.subplot(2,2,1) 
plt.plot(t,x1,linewidth = 3) 
plt.title('SineWave of frequency 20 Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,2)
plt.plot(nT,x2,'ro',linewidth = 3)
plt.title('Sample marks after resampling at fs = 100Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,3)
plt.stem(nT,x2,'m')
plt.title('Sample after resampling at fs = 100Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,4)
plt.plot(nT,x2,'g-',linewidth = 3)
plt.title('Reconstruted Sine wave', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.show()

t = np.linspace(0,0.5,200);
x1 = 2 * np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 20 * t)

srate = 100  # Hz. 

T = 1/srate;

n = np.arange(0, 0.5/T);

nT = n*T

x2 = 2 * np.sin(2 * np.pi * 10 * nT) + np.sin(2 * np.pi * 20 * nT)          # Since for sampling t = nT.

# Plotting

plt.figure(figsize = (24,18)) # set the size of figure
plt.suptitle('Sampling a wave of Fmax = 20Hz with fs = 100 Hz', fontsize = 40)
style.use('dark_background')
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15


plt.subplot(2,2,1) 
plt.plot(t,x1,linewidth = 3) 
plt.title('Sine wave of Fmax = 20Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,2)
plt.plot(nT,x2,'ro',linewidth = 3)
plt.title('Sample marks after resampling at fs = 100Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,3)
plt.stem(nT,x2,'m')
plt.title('Sample after resampling at fs = 100Hz', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.subplot(2,2,4)
plt.plot(nT,x2,'g-',linewidth = 3)
plt.title('Reconstruted wave', fontsize = 25)
plt.xlabel('time', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)

plt.show()