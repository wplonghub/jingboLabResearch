import pandas as pd
import os
import sys
import time
# import winsound
# from usb_iss import UsbIss, defs

from tkinter import *

'''
@author: Peilong Wang
@date: Apr. 19, 2021
'''
root = Tk()
root.title("GBS20V1 GUI")

# creating a label widget
LSBLabel = Label(root, text="LSB channel", font='Helvetica 12 bold')
MSBLabel = Label(root, text="MSB channel", font='Helvetica 12 bold')

lsb_ch0_lb = Label(root, text="CH0")
lsb_ch1_lb = Label(root, text="CH1")
lsb_ch2_lb = Label(root, text="CH2")
lsb_ch3_lb = Label(root, text="CH3")
lsb_ch4_lb = Label(root, text="CH4")
lsb_ch5_lb = Label(root, text="CH5")
lsb_ch6_lb = Label(root, text="CH6")
lsb_ch7_lb = Label(root, text="CH7")

lsb_msb_item = ["eRxEn", "eRxEqu1", "eRxEqu0", "PAdisCH", "PAphase", "mask", "EdgeRead"]

lsb_eRxEn_lb = Label(root, text=lsb_msb_item[0])
lsb_eRxEqu1_lb = Label(root, text=lsb_msb_item[1])
lsb_eRxEqu0_lb = Label(root, text=lsb_msb_item[2])
lsb_PAdisCH_lb = Label(root, text=lsb_msb_item[3])
lsb_PAphase_lb = Label(root, text=lsb_msb_item[4])
lsb_mask_lb = Label(root, text=lsb_msb_item[5])
lsb_EdgeRead_lb = Label(root, text=lsb_msb_item[6])


msb_ch0_lb = Label(root, text="CH0")
msb_ch1_lb = Label(root, text="CH1")
msb_ch2_lb = Label(root, text="CH2")
msb_ch3_lb = Label(root, text="CH3")
msb_ch4_lb = Label(root, text="CH4")
msb_ch5_lb = Label(root, text="CH5")
msb_ch6_lb = Label(root, text="CH6")
msb_ch7_lb = Label(root, text="CH7")


msb_eRxEn_lb = Label(root, text=lsb_msb_item[0])
msb_eRxEqu1_lb = Label(root, text=lsb_msb_item[1])
msb_eRxEqu0_lb = Label(root, text=lsb_msb_item[2])
msb_PAdisCH_lb = Label(root, text=lsb_msb_item[3])
msb_PAphase_lb = Label(root, text=lsb_msb_item[4])
msb_mask_lb = Label(root, text=lsb_msb_item[5])
msb_EdgeRead_lb = Label(root, text=lsb_msb_item[6])


FbDivLabel = Label(root, text="FbDiv", font='Helvetica 12 bold')
FbDiv_item = ['FbDiv_enTestClk1G28', 'FbDiv_enPAClk1G28', 'FbDiv_skip', 'FbDiv_enSer']
FbDiv_lb = {}
for i in range(len(FbDiv_item)):
    FbDiv_lb[FbDiv_item[i]] = Label(root, text=FbDiv_item[i] )

AFCLabel = Label(root, text="AFC", font='Helvetica 12 bold')
AFC_item = ['AFC_Start', 'AFC_RST', 'AFC_overriseCtrl', 'AFC_OverrideCtrl_val1<5:0>']
AFC_lb = {}
for i in range(len(AFC_item)):
    AFC_lb[AFC_item[i]] = Label(root, text=AFC_item[i] )

PLLLabel = Label(root, text="PLL", font='Helvetica 12 bold')
PLL_item = ['PLL_ENABL EPLL', 'PLL_vcoDAC<3:0>', 'PLL_vcoR ailMode', 'PLL_overri deVc', 'PLL_BIASGEN_CONFIG<3:0>', 'PLL_CONFIG_I_PLL<3:0>', 'PLL_CONFIG_P_PLL<3:0>', 'PLL_PLL_R_CONFIG<3:0>']
PLL_lb = {}
for i in range(len(PLL_item)):
    PLL_lb[PLL_item[i]] = Label(root, text=PLL_item[i] )

GNCLabel = Label(root, text="GNC", font='Helvetica 12 bold')
GNC_item = ['ENC_seedLSB<6:0>', 'Enc_Rst', 'ENC_seedMSB<6:0>', 'Enc_Enable']
GNC_lb = {}
for i in range(len(GNC_item)):
    GNC_lb[GNC_item[i]] = Label(root, text=GNC_item[i] )

PALabel = Label(root, text="PA", font='Helvetica 12 bold')
PA_item = ['PA_cpcurrent<3:0>', 'PA_dllstartVoltage<1:0>', 'PA0_clkInvert', 'PA1_clkInvert', 'PA0_edgeResetN', 'PA0_enEdgeDetect', 'PA0_dllFD', 'PA0_dllcapReset', 'PA0_dllEn', 'PA1_edgeResetN', 'PA1_enEdgeDetect', 'PA1_dllFD', 'PA1_dllcapReset', 'PA1_dllEn']
PA_lb = {}
for i in range(len(PA_item)):
    PA_lb[PA_item[i]] = Label(root, text=PA_item[i] )

CoreLabel = Label(root, text="Core", font='Helvetica 12 bold')
Core_item = ['Core_Sel2V5', 'Core_disLA', 'Core_disCombine', 'Core_CTLE<2:0>', 'Core_capLoad<4:0>', 'Core_iLSBSel<4:0>', 'Core_iMSBSel<4:0>', 'IBIAS_BIAS<4:0>']
Core_lb = {}
for i in range(len(Core_item)):
    Core_lb[Core_item[i]] = Label(root, text=Core_item[i] )

StartupLabel = Label(root, text="Startup", font='Helvetica 12 bold')
Startup_item = ['RefClk_enRx', 'Ser_txDataRate']
Startup_lb = {}
for i in range(len(Startup_item)):
    Startup_lb[Startup_item[i]] = Label(root, text=Startup_item[i] )

Run_item = ['Port', 'I2C']
Run_lb = {}
for i in range(len(Run_item)):
    Run_lb[Run_item[i]] = Label(root, text=Run_item[i], fg='red' )

ReadonlyLabel = Label(root, text="Readonly", font='Helvetica 12 bold')
Readonly_item = ['AFCcalCap<5:0>', 'AFCbusy', 'INSTLOCK_PLL', 'PA0_edge<7:0>', 'PA1_edge<7:0>', 'PA0_testEdge<0>', 'PA1_testEdge<0>']
Readonly_lb = {}
for i in range(len(Readonly_item)):
    Readonly_lb[Readonly_item[i]] = Label(root, text=Readonly_item[i] )

# readonly register
Readonly_var = []
for i in range(len(Readonly_item)):
    Readonly_var.append( StringVar() )
    Readonly_var[i].set('0')
Readonly_var_lb = {}
for i in range(len(Readonly_item)):
    Readonly_var_lb[Readonly_item[i]] = Label(root, textvariable = Readonly_var[i], borderwidth=5 )


# shoving it onto screen
LSBLabel.grid(row=29, column=91)
MSBLabel.grid(row=39, column=91)

lsb_ch7_lb.grid(row=31, column=92)
lsb_ch6_lb.grid(row=32, column=92)
lsb_ch5_lb.grid(row=33, column=92)
lsb_ch4_lb.grid(row=34, column=92)
lsb_ch3_lb.grid(row=35, column=92)
lsb_ch2_lb.grid(row=36, column=92)
lsb_ch1_lb.grid(row=37, column=92)
lsb_ch0_lb.grid(row=38, column=92)

lsb_eRxEn_lb.grid(row=30, column=93)
lsb_eRxEqu1_lb.grid(row=30, column=94)
lsb_eRxEqu0_lb.grid(row=30, column=95)
lsb_PAdisCH_lb.grid(row=30, column=96)
lsb_PAphase_lb.grid(row=30, column=97)
lsb_mask_lb.grid(row=30, column=98)
lsb_EdgeRead_lb.grid(row=30, column=99)


msb_ch7_lb.grid(row=41, column=92)
msb_ch6_lb.grid(row=42, column=92)
msb_ch5_lb.grid(row=43, column=92)
msb_ch4_lb.grid(row=44, column=92)
msb_ch3_lb.grid(row=45, column=92)
msb_ch2_lb.grid(row=46, column=92)
msb_ch1_lb.grid(row=47, column=92)
msb_ch0_lb.grid(row=48, column=92)

msb_eRxEn_lb.grid(row=40, column=93)
msb_eRxEqu1_lb.grid(row=40, column=94)
msb_eRxEqu0_lb.grid(row=40, column=95)
msb_PAdisCH_lb.grid(row=40, column=96)
msb_PAphase_lb.grid(row=40, column=97)
msb_mask_lb.grid(row=40, column=98)
msb_EdgeRead_lb.grid(row=40, column=99)

FbDivLabel.grid(row=30, column=2)
for i,lb in enumerate(FbDiv_lb):
    FbDiv_lb[lb].grid(row=i+31, column=2)

AFCLabel.grid(row=30, column=4)
for i,lb in enumerate(AFC_lb):
    AFC_lb[lb].grid(row=i+31, column=4)

PLLLabel.grid(row=30, column=6)
for i,lb in enumerate(PLL_lb):
    PLL_lb[lb].grid(row=i+31, column=6)

GNCLabel.grid(row=30, column=8)
for i,lb in enumerate(GNC_lb):
    GNC_lb[lb].grid(row=i+31, column=8)

PALabel.grid(row=30, column=10)
for i,lb in enumerate(PA_lb):
    PA_lb[lb].grid(row=i+31, column=10)

CoreLabel.grid(row=30, column=12)
for i,lb in enumerate(Core_lb):
    Core_lb[lb].grid(row=i+31, column=12)

StartupLabel.grid(row=24, column=2)
for i,lb in enumerate(Startup_lb):
    Startup_lb[lb].grid(row=i+25, column=2)

for i,lb in enumerate(Run_lb):
    Run_lb[lb].grid(row=i+24, column=96)

ReadonlyLabel.grid(row=29, column=100)
for i,lb in enumerate(Readonly_lb):
    Readonly_lb[lb].grid(row=i+31, column=101)

for i,lb in enumerate(Readonly_var_lb):
    Readonly_var_lb[lb].grid(row=i+31, column=102)
   
# entry section
lsb_entry = {}
for item in lsb_msb_item:
    lsb_entry[item] = []
for index, key in enumerate(lsb_entry):
    for i in range(8):
        lsb_entry[key].append( Entry(root, width=2) )
        lsb_entry[key][i].grid(row=i+31, column=index+93, padx=3, pady=3)
        lsb_entry[key][i].insert(END, str(0))

msb_entry = {}
for item in lsb_msb_item:
    msb_entry[item] = []
for index, key in enumerate(msb_entry):
    for i in range(8):
        msb_entry[key].append( Entry(root, width=2) )
        msb_entry[key][i].grid(row=i+41, column=index+93, padx=3, pady=3)
        msb_entry[key][i].insert(END, str(0))

FbDiv_entry = []
for i in range(len(FbDiv_item)):
    FbDiv_entry.append( Entry(root, width=2) )
    FbDiv_entry[i].grid(row=i+31, column=3, padx=3, pady=3)
    FbDiv_entry[i].insert(END, str(0))

AFC_entry = []
for i in range(len(AFC_item)):
    AFC_entry.append( Entry(root, width=3) )
    AFC_entry[i].grid(row=i+31, column=5, padx=3, pady=3)
    AFC_entry[i].insert(END, str(0))

PLL_entry = []
for i in range(len(PLL_item)):
    PLL_entry.append( Entry(root, width=3) )
    PLL_entry[i].grid(row=i+31, column=7, padx=3, pady=3)
    PLL_entry[i].insert(END, str(0))

GNC_entry = []
for i in range(len(GNC_item)):
    GNC_entry.append( Entry(root, width=3) )
    GNC_entry[i].grid(row=i+31, column=9, padx=3, pady=3)
    GNC_entry[i].insert(END, str(0))

PA_entry = []
for i in range(len(PA_item)):
    PA_entry.append( Entry(root, width=3) )
    PA_entry[i].grid(row=i+31, column=11, padx=3, pady=3)
    PA_entry[i].insert(END, str(0))

Core_entry = []
for i in range(len(Core_item)):
    Core_entry.append( Entry(root, width=3) )
    Core_entry[i].grid(row=i+31, column=13, padx=3, pady=3)
    Core_entry[i].insert(END, str(0))

Startup_entry = []
for i in range(len(Startup_item)):
    Startup_entry.append( Entry(root, width=2) )
    Startup_entry[i].grid(row=i+25, column=3, padx=3, pady=3)
    Startup_entry[i].insert(END, str(0))

Run_entry = []
for i in range(len(Run_item)):
    Run_entry.append( Entry(root, width=5) )
    Run_entry[i].grid(row=i+24, column=97, padx=5, pady=5)
    Run_entry[i].insert(END, str(0))


    
# FbDiv_lb[lb].grid(row=i+31, column=2)


# FbDivider


    # e4.append( Entry(root, width=5) )
    # e4[j].grid(row=2, column=j+1, padx=10, pady=10)
    # e4[j].insert(END, str(entry_default_value[j]))










root.mainloop()
