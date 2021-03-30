#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import copy
import time
import math
import serial
import struct
import socket
import schedule
import winsound
import datetime
import heartrate
import numpy as np
import pyvisa as visa
from scipy.stats import norm
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

from scipy.optimize import curve_fit
#========================================================================================#
## plot parameters
lw_grid = 0.5                   # grid linewidth
fig_dpi = 800                   # save figure's resolution
#========================================================================================#
freqency = 1000
duration = 1000
'''
@author: Wei Zhang
@date: 2021-03-24
@updated by Peilong Wang on 2021-03-30
This script is used to control optical switch and optical spectrum analyzer (Model: ANDO AQ6317)
'''
#========================================================================================#
## dBm to mW conversion
def dBm_to_mW(x):
    return 1 * (10**(x/10.0))
#========================================================================================#
## square function
def square(x):
    return x**2
#========================================================================================#
def gauss(x, H, A, x0, sigma):
    return H + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

def gauss_fit(x, y):
    mean = sum(x * y) / sum(y)
    sigma = np.sqrt(sum(y * (x - mean) ** 2) / sum(y))
    popt, pcov = curve_fit(gauss, x, y, p0=[min(y), max(y), mean, sigma])
    return popt
#========================================================================================#

def main():
    timeslot = 0
    chan_sel = [b'<OSW01_OUT_01>', b'<OSW01_OUT_02>', b'<OSW01_OUT_03>', b'<OSW01_OUT_04>',\
                b'<OSW01_OUT_05>', b'<OSW01_OUT_06>', b'<OSW01_OUT_07>', b'<OSW01_OUT_08>']
    ser = serial.Serial('COM4')
    print("Serial port: %s"%ser.name)

    rm = visa.ResourceManager()
    print(rm.list_resources())
    inst1 = rm.open_resource('GPIB0::5::INSTR')     # GPIB address
    time.sleep(1)
    print(inst1.query("*IDN?"))                     # query Instrument ID
    lasttime = datetime.datetime.now()
    while True:
        if(datetime.datetime.now() - lasttime > datetime.timedelta(minutes=timeslot)):
            lasttime = datetime.datetime.now()
            for j in range(8):
                ser.write(chan_sel[j])
                s = ser.read(14)
                time.sleep(2)
                    
                inst1.write('INIT')                             
                time.sleep(3)
                inst1.write('STAWL835.00')                      # set start waveform length = 840 nm
                inst1.write('HD0')
                inst1.write('LSCL10.0')                         # y-axis scale 10 dB/D
                inst1.write('STPWL865.00')                      # set stop waveform length = 870 nm
                inst1.write('RESLN0.2')                         # set x-axis resolution 0.05 nm
                inst1.write('SMPL2000')                         # set sample point
            
                inst1.write('SGL')                              # start a single sweep
                time.sleep(6)

                xdata = []
                ydata = []
                inst1.write('WDATAR1-R2000')                    # acquire x-axis data
                xdata = inst1.query('')[:-2].split(",")[1:]

                inst1.write('LDATAR1-R2000')                    # acquire y-axis data
                ydata = inst1.query('')[:-2].split(",")[1:]

                wavelength = []                             
                yydata = []
                timestamp = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
                print(timestamp)
                with open("./Waveform_data/waveform_data_channel%s_%s.txt"%(j+1, timestamp), 'w') as infile:
                    for i in range(len(xdata)):
                        wavelength += [float(xdata[i])]
                        yydata += [float(ydata[i])] 
                        infile.write('%f %f\n'%(float(xdata[i]), float(ydata[i]))) 


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


                # # (mean, sigma) = norm.fit(Power_Density)
                # # print(mean, sigma)
                # Power_RMS = sigma
                # Power_mean = mean



                # # added on 20210330
                # partowrite = "%s, "%timestamp + "%f uW, "%(Total_Power) + "%f mW, "%(Peak_Power) + "%f nm, "%(Peak_wavelength_location) + "%f nm, "%(Power_mean) + "%f nm\n"%(Power_RMS)
                
                # print (str(j+1) + ", " + partowrite)
                
                # with open("./Channel_data/Channel_%s_Parameters_Calculation.txt"%(j+1), 'a') as infile1:
                #     infile1.write(partowrite)
            
    print("ok")


#========================================================================================#
if __name__ == "__main__":
    main()
    
