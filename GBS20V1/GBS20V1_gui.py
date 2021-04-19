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

FbDiv_item = ['FbDiv_enTestClk1G28', 'FbDiv_enPAClk1G28', 'FbDiv_skip', 'FbDiv_enSer']
FbDiv_lb = {}
for i in range(len(FbDiv_item)):
    FbDiv_lb[FbDiv_item[i]] = Label(root, text=FbDiv_item[i] )

AFC_item = ['AFC_Start', 'AFC_RST', 'AFC_overriseCtrl', 'AFC_OverrideCtrl_val1<5:0>']
AFC_lb = {}
for i in range(len(AFC_item)):
    AFC_lb[AFC_item[i]] = Label(root, text=AFC_item[i] )



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

for i,lb in enumerate(FbDiv_lb):
    FbDiv_lb[lb].grid(row=i+31, column=2)

for i,lb in enumerate(AFC_lb):
    AFC_lb[lb].grid(row=i+31, column=4)

   
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
    
# FbDiv_lb[lb].grid(row=i+31, column=2)


# FbDivider


    # e4.append( Entry(root, width=5) )
    # e4[j].grid(row=2, column=j+1, padx=10, pady=10)
    # e4[j].insert(END, str(entry_default_value[j]))










root.mainloop()
