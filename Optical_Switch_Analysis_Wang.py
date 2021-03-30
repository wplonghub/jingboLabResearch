import pandas as pd
import numpy as np

from scipy.optimize import curve_fit

import pylab as plb
import matplotlib.pyplot as plt
from scipy import asarray as ar,exp

def gauss(x, H, A, x0, sigma):
    return H + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

def gauss_fit(x, y):
    mean = sum(x * y) / sum(y)
    sigma = np.sqrt(sum(y * (x - mean) ** 2) / sum(y))
    popt, pcov = curve_fit(gauss, x, y, p0=[min(y), max(y), mean, sigma])
    return popt



df = pd.read_table("./Waveform_data/waveform_data_channel5_2021-03-26_17-22-45.txt", names=['wave', 'dBm'], delim_whitespace=True)

print (df)

x = df['wave'].to_numpy()
y = df['dBm'].to_numpy()
ymindex = np.argmax(y)
print (ymindex, x[ymindex])
imin = ymindex - 150
imax = ymindex + 150
x = x[612:863]
y = y[612:863]
# print (x)
# print (y) 635, 863 [762]

n = len(x)                          #the number of data
mean = sum(x*y)/n                   #note this correction
sigma = sum(y*(x-mean)**2)/n        #note this correction

def gaus(x,a,x0,sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))

popt,pcov = curve_fit(gaus,x,y,p0=[1,mean,sigma])

plt.plot(x,y,'b+:',label='data')
plt.plot(x,gaus(x,*popt),'ro:',label='fit')
plt.legend()
plt.title('Fig. 3 - Fit for Time Constant')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()








# H, A, x0, sigma = gauss_fit(x, y)
# FWHM = 2.35482 * sigma

# print (x0, sigma)

# print (type(df['wave'].tolist()) )
# print (df['wave'])



# with open("./Waveform_data/waveform_data_channel%s_%s.txt"%(j+1, timestamp), 'w') as infile:
#     for i in range(len(xdata)):
#         wavelength += [float(xdata[i])]
#         yydata += [float(ydata[i])] 
#         infile.write('%f %f\n'%(float(xdata[i]), float(ydata[i]))) 
# # print(xxdata)
# # print(yydata)  

# Power_Density = list(map(dBm_to_mW, yydata))
# # print(Power_Density)
# Power = []
# for k in range(len(wavelength)-1):
#     Power += [(Power_Density[k+1] + Power_Density[k]) * (wavelength[k+1] - wavelength[k]) / 2.0] 
# print(Power)

# Total_Power = sum(Power) * 1000.0
# Peak_Power = max(Power)
# Peak_wavelength_location = wavelength[Power.index(max(Power))]

