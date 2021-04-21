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
# shoving it onto screen
LSBLabel.grid(row=29, column=91)
MSBLabel.grid(row=39, column=91)

ch_item = ['CH' + str(i) for i in range(7, -1, -1)]

lsb_ch_lb = {}
for i in range(len(ch_item)):
    lsb_ch_lb[ch_item[i]] = Label(root, text=ch_item[i] )
for i,lb in enumerate(lsb_ch_lb):
    lsb_ch_lb[lb].grid(row=i+31, column=92)

lsb_msb_item = ["eRxEn", "eRxEqu1", "eRxEqu0", "PAdisCH", "PAphase", "mask"]#, "EdgeRead"]

lsb_lb = {}
for i in range(len(lsb_msb_item)):
    lsb_lb[lsb_msb_item[i]] = Label(root, text=lsb_msb_item[i] )
for i,lb in enumerate(lsb_lb):
    lsb_lb[lb].grid(row=30, column=93+i)

lsb_entry = {}
for item in lsb_msb_item:
    lsb_entry[item] = []
for index, key in enumerate(lsb_entry):
    for i in range(len(ch_item)):
        lsb_entry[key].append( Entry(root, width=2) )
        lsb_entry[key][i].grid(row=i+31, column=index+93, padx=3, pady=3)
        lsb_entry[key][i].insert(END, str(0))


msb_ch_lb = {}
for i in range(len(ch_item)):
    msb_ch_lb[ch_item[i]] = Label(root, text=ch_item[i] )
for i,lb in enumerate(msb_ch_lb):
    msb_ch_lb[lb].grid(row=i+41, column=92)

msb_lb = {}
for i in range(len(lsb_msb_item)):
    msb_lb[lsb_msb_item[i]] = Label(root, text=lsb_msb_item[i] )
for i,lb in enumerate(msb_lb):
    msb_lb[lb].grid(row=40, column=93+i)

msb_entry = {}
for item in lsb_msb_item:
    msb_entry[item] = []
for index, key in enumerate(msb_entry):
    for i in range(len(ch_item)):
        msb_entry[key].append( Entry(root, width=2) )
        msb_entry[key][i].grid(row=i+41, column=index+93, padx=3, pady=3)
        msb_entry[key][i].insert(END, str(0))


FbDivLabel = Label(root, text="FbDiv", font='Helvetica 12 bold')
FbDiv_item = ['FbDiv_enTestClk1G28', 'FbDiv_enPAClk1G28', 'FbDiv_skip', 'FbDiv_enSer']
FbDiv_default = [1,0,0,1]
FbDiv_lb = {}
for i in range(len(FbDiv_item)):
    FbDiv_lb[FbDiv_item[i]] = Label(root, text=FbDiv_item[i] )

FbDivLabel.grid(row=30, column=2)
for i,lb in enumerate(FbDiv_lb):
    FbDiv_lb[lb].grid(row=i+31, column=2)

FbDiv_entry = []
for i in range(len(FbDiv_item)):
    FbDiv_entry.append( Entry(root, width=2) )
    FbDiv_entry[i].grid(row=i+31, column=3, padx=3, pady=3)
    FbDiv_entry[i].insert(END, str(FbDiv_default[i]))


AFCLabel = Label(root, text="AFC", font='Helvetica 12 bold')
AFC_item = ['AFC_Start', 'AFC_RST', 'AFC_overriseCtrl', 'AFC_OverrideCtrl_val1<5:0>']
AFC_default = [0,0,1,20]
AFC_lb = {}
for i in range(len(AFC_item)):
    AFC_lb[AFC_item[i]] = Label(root, text=AFC_item[i] )

AFCLabel.grid(row=30, column=4)
for i,lb in enumerate(AFC_lb):
    AFC_lb[lb].grid(row=i+31, column=4)

AFC_entry = []
for i in range(len(AFC_item)):
    AFC_entry.append( Entry(root, width=3) )
    AFC_entry[i].grid(row=i+31, column=5, padx=3, pady=3)
    AFC_entry[i].insert(END, str(AFC_default[i]))


PLLLabel = Label(root, text="PLL", font='Helvetica 12 bold')
PLL_item = ['PLL_ENABL EPLL', 'PLL_vcoDAC<3:0>', 'PLL_vcoRailMode', 'PLL_overrideVc', 'PLL_BIASGEN_CONFIG<3:0>', 'PLL_CONFIG_I_PLL<3:0>', 'PLL_CONFIG_P_PLL<3:0>', 'PLL_PLL_R_CONFIG<3:0>']
PLL_default = [1,8,1,0,8,10,10,8]
PLL_lb = {}
for i in range(len(PLL_item)):
    PLL_lb[PLL_item[i]] = Label(root, text=PLL_item[i] )

PLLLabel.grid(row=30, column=6)
for i,lb in enumerate(PLL_lb):
    PLL_lb[lb].grid(row=i+31, column=6)

PLL_entry = []
for i in range(len(PLL_item)):
    PLL_entry.append( Entry(root, width=3) )
    PLL_entry[i].grid(row=i+31, column=7, padx=3, pady=3)
    PLL_entry[i].insert(END, str(PLL_default[i]))


ENCLabel = Label(root, text="ENC", font='Helvetica 12 bold')
ENC_item = ['ENC_seedLSB<6:0>', 'Enc_Rst', 'ENC_seedMSB<6:0>', 'Enc_Enable']
ENC_default = [67,1,22,1]
ENC_lb = {}
for i in range(len(ENC_item)):
    ENC_lb[ENC_item[i]] = Label(root, text=ENC_item[i] )

ENCLabel.grid(row=30, column=8)
for i,lb in enumerate(ENC_lb):
    ENC_lb[lb].grid(row=i+31, column=8)

ENC_entry = []
for i in range(len(ENC_item)):
    ENC_entry.append( Entry(root, width=3) )
    ENC_entry[i].grid(row=i+31, column=9, padx=3, pady=3)
    ENC_entry[i].insert(END, str(ENC_default[i]))


PALabel = Label(root, text="PA", font='Helvetica 12 bold')
PA_item = ['PA_cpcurrent<3:0>', 'PA_dllstartVoltage<1:0>', 'PA0_clkInvert', 'PA1_clkInvert', 'PA0_edgeResetN', 'PA0_enEdgeDetect', 'PA0_dllFD', 'PA0_dllcapReset', 'PA0_dllEn', 'PA1_edgeResetN', 'PA1_enEdgeDetect', 'PA1_dllFD', 'PA1_dllcapReset', 'PA1_dllEn']
PA_default = [4,1,0,0,0,1,0,0,0,0,1,0,0,0]
PA_lb = {}
for i in range(len(PA_item)):
    PA_lb[PA_item[i]] = Label(root, text=PA_item[i] )

PALabel.grid(row=30, column=10)
for i,lb in enumerate(PA_lb):
    PA_lb[lb].grid(row=i+31, column=10)

PA_entry = []
for i in range(len(PA_item)):
    PA_entry.append( Entry(root, width=3) )
    PA_entry[i].grid(row=i+31, column=11, padx=3, pady=3)
    PA_entry[i].insert(END, str(PA_default[i]))


CoreLabel = Label(root, text="Core", font='Helvetica 12 bold')
Core_item = ['Core_Sel2V5', 'Core_disLA', 'Core_disCombine', 'Core_CTLE<2:0>', 'Core_capLoad<4:0>', 'Core_iLSBSel<4:0>', 'Core_iMSBSel<4:0>', 'IBIAS_BIAS<4:0>']
Core_default = [1,0,0,0,0,16,16,0]
Core_lb = {}
for i in range(len(Core_item)):
    Core_lb[Core_item[i]] = Label(root, text=Core_item[i] )

CoreLabel.grid(row=30, column=12)
for i,lb in enumerate(Core_lb):
    Core_lb[lb].grid(row=i+31, column=12)

Core_entry = []
for i in range(len(Core_item)):
    Core_entry.append( Entry(root, width=3) )
    Core_entry[i].grid(row=i+31, column=13, padx=3, pady=3)
    Core_entry[i].insert(END, str(Core_default[i]))


StartupLabel = Label(root, text="Startup", font='Helvetica 12 bold')
Startup_item = ['RefClk_enRx', 'Ser_txDataRate']
Startup_default = [1,1]
Startup_lb = {}
for i in range(len(Startup_item)):
    Startup_lb[Startup_item[i]] = Label(root, text=Startup_item[i] )

StartupLabel.grid(row=24, column=2)
for i,lb in enumerate(Startup_lb):
    Startup_lb[lb].grid(row=i+25, column=2)

Startup_entry = []
for i in range(len(Startup_item)):
    Startup_entry.append( Entry(root, width=2) )
    Startup_entry[i].grid(row=i+25, column=3, padx=3, pady=3)
    Startup_entry[i].insert(END, str(Startup_default[i]))


Run_item = ['Port', 'I2C']
Run_lb = {}
for i in range(len(Run_item)):
    Run_lb[Run_item[i]] = Label(root, text=Run_item[i], fg='red' )

for i,lb in enumerate(Run_lb):
    Run_lb[lb].grid(row=i+25, column=98)

Run_entry = []
for i in range(len(Run_item)):
    Run_entry.append( Entry(root, width=5) )
    Run_entry[i].grid(row=i+25, column=99, padx=5, pady=5)
    Run_entry[i].insert(END, str(0))


# ReadonlyLabel = Label(root, text="Readonly", font='Helvetica 12 bold')
# Readonly_item = ['AFCcalCap<5:0>', 'AFCbusy', 'INSTLOCK_PLL', 'PA0_edge<7:0>', 'PA1_edge<7:0>', 'PA0_testEdge<0>', 'PA1_testEdge<0>']
# Readonly_lb = {}
# for i in range(len(Readonly_item)):
#     Readonly_lb[Readonly_item[i]] = Label(root, text=Readonly_item[i] )

# ReadonlyLabel.grid(row=29, column=100)
# for i,lb in enumerate(Readonly_lb):
#     Readonly_lb[lb].grid(row=i+31, column=101)

# Readonly_var = [] # readonly register
# for i in range(len(Readonly_item)):
#     Readonly_var.append( StringVar() )
#     Readonly_var[i].set('0')
# Readonly_var_lb = {}
# for i in range(len(Readonly_item)):
#     Readonly_var_lb[Readonly_item[i]] = Label(root, textvariable = Readonly_var[i], borderwidth=5 )
# for i,lb in enumerate(Readonly_var_lb):
#     Readonly_var_lb[lb].grid(row=i+31, column=102)



def gui_form_reg():
    rN = []

    # REG_00 to 05
    l = []
    for e in lsb_entry["eRxEn"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    l = []
    for e in msb_entry["eRxEn"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    l = []
    for e in lsb_entry["eRxEqu1"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    l = []
    for e in msb_entry["eRxEqu1"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    l = []
    for e in lsb_entry["eRxEqu0"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    l = []
    for e in msb_entry["eRxEqu0"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    # REG_06 to 07
    l = []
    for e in FbDiv_entry:
        l.append( e.get() )
    l = [int(i) for i in l]
    rFbDiv = l[0] << 3 | l[1] << 2 | l[2] << 1 | l[3]

    rRefClk = int( Startup_entry[0].get() )

    l = []
    for e in AFC_entry:
        l.append( e.get() )
    l = [int(i) for i in l]
    rAFC = l[0] << 2 | l[1] << 1 | l[2]
    rAFC_Overide = l[3]

    rN.append( rFbDiv << 4 | rRefClk << 3 | rAFC )
    rN.append( rAFC_Overide )

    # REG_08 to 0A
    rSer_tx = int( Startup_entry[1].get() )

    l = []
    for e in PLL_entry:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( rSer_tx << 7 | l[0] << 6 | l[1] << 2 | l[2] << 1 | l[3] )
    rN.append( l[4] << 4 | l[5] )
    rN.append( l[6] << 4 | l[7] )

    # REG_0B to 0C
    l = []
    for e in lsb_entry["mask"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    l = []
    for e in msb_entry["mask"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    # REG_0D to 0E
    l = []
    for e in ENC_entry:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 1 | l[1] )
    rN.append( l[2] << 1 | l[3] )

    # REG_0F to 10
    l = []
    for e in lsb_entry["PAdisCH"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    l = []
    for e in msb_entry["PAdisCH"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[0] << 7 | l[1] << 6 | l[2] << 5 | l[3] << 4 | l[4] << 3 | l[5] << 2 | l[6] << 1 | l[7] )

    # REG_11 to 14
    l = []
    for e in lsb_entry["PAphase"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[6] << 4 | l[7] )
    rN.append( l[4] << 4 | l[5] )
    rN.append( l[2] << 4 | l[3] )
    rN.append( l[0] << 4 | l[1] )

    # REG_15 to 18
    l = []
    for e in msb_entry["PAphase"]:
        l.append( e.get() )
    l = [int(i) for i in l]
    rN.append( l[6] << 4 | l[7] )
    rN.append( l[4] << 4 | l[5] )
    rN.append( l[2] << 4 | l[3] )
    rN.append( l[0] << 4 | l[1] )

    # REG_19 to 1B
    l_PA = []
    for e in PA_entry:
        l_PA.append( e.get() )
    l_PA = [int(i) for i in l_PA]

    l_Core = []
    for e in Core_entry:
        l_Core.append( e.get() )
    l_Core = [int(i) for i in l_Core]

    rN.append( l_PA[0] << 4 | l_PA[1] << 2 | l_PA[2] << 1 | l_PA[3] )
    rN.append( l_Core[0] << 5 | l_PA[4] << 4 | l_PA[5] << 3 | l_PA[6] << 2 | l_PA[7] << 1 | l_PA[8] )
    rN.append( l_Core[1] << 6 | l_Core[2] << 5 | l_PA[9] << 4 | l_PA[10] << 3 | l_PA[11] << 2 | l_PA[12] << 1 | l_PA[13] )
    rN.append( l_Core[3] << 5 | l_Core[4] )
    rN.append( l_Core[5] )
    rN.append( l_Core[6] )
    rN.append( l_Core[7] )

    # print (rN)
    for i in range(len(rN)):
        print('0x{0:0{1}X}'.format(i,2) + ' ' + '0x{0:0{1}X}'.format(rN[i],2) )

    print ('End')
    return

def button_run():
    gui_form_reg

    return 
bt_run = Button(root, text='Run', fg='red', command=gui_form_reg, pady=15)
bt_run.grid(row=25, column=100, rowspan=2)

root.mainloop()


# entry section











    
# FbDiv_lb[lb].grid(row=i+31, column=2)


# FbDivider


    # e4.append( Entry(root, width=5) )
    # e4[j].grid(row=2, column=j+1, padx=10, pady=10)
    # e4[j].insert(END, str(entry_default_value[j]))

