import pandas as pd
import os
import sys
import time
import winsound
from usb_iss import UsbIss, defs

from tkinter import *

'''
@author: Peilong Wang
@date: Apr. 7, 2021
'''

def df_form_reg(l_gui):
    # gui value -> resiger map
    l_txt = [0] * 13
    l_txt[10] = l_gui[0]  
    l_txt[11] = l_gui[1]  
    l_txt[4] = l_gui[2]  
    l_txt[6] = l_gui[3]  
    l_txt[1] = l_gui[4]  
    l_txt[0] = l_gui[5]  
    l_txt[2] = l_gui[6]  
    l_txt[7] = l_gui[7]  
    l_txt[12] = l_gui[8]  
    l_txt[3] = l_gui[9]  
    l_txt[5] = l_gui[10]  
    l_txt[9] = l_gui[11]  
    l_txt[8] = l_gui[12]  

    r0 = l_txt[0] << 4 | l_txt[1]
    r1 = l_txt[2] << 4 | l_txt[3]
    r2 = l_txt[4] << 7 | l_txt[5] << 4 | l_txt[6] << 3 | l_txt[7]
    r3 = l_txt[8] << 7 | l_txt[9] << 6 | l_txt[10] << 4 | l_txt[11] << 3 | l_txt[12]

    return [r0, r1, r2, r3]


def write_user_config(Reg_Val, out_filename):
    # write out to configuration file
    f = open(out_filename, 'w')
    for i in range(len(Reg_Val)):
        f.write('0x{0:0{1}X}'.format(i,2) + ' ' + '0x{0:0{1}X}'.format(Reg_Val[i],2) )
        f.write('\n')
    f.close()

    return
#-----------------------------------------------------------------------------------#
freqency = 1000
duration = 200
#-----------------------------------------------------------------------------------#

root = Tk()
root.title("QTIA")

# creating labels and shoving labels onto screen
lb_ch1 = Label(root, text="CH1")
lb_ch2 = Label(root, text="CH2")
lb_ch3 = Label(root, text="CH3")
lb_ch4 = Label(root, text="CH4")

lb_ch4.grid(row=2, column=0)
lb_ch3.grid(row=3, column=0)
lb_ch2.grid(row=4, column=0)
lb_ch1.grid(row=5, column=0)

# creating categories and shoving them onto screen
lb_cat1 = Label(root, text="Bias enabling", bg='grey')
lb_cat2 = Label(root, text="Bias selection", bg='grey')
lb_cat3 = Label(root, text="Bandwidth selection", bg='grey')
lb_cat4 = Label(root, text="Miscellaneous", bg='grey')

lb_cat1.grid(row=0, column=1, columnspan=4, padx=40, pady=10, sticky='ew')
lb_cat2.grid(row=0, column=5, columnspan=4, padx=40, pady=10, sticky='ew')
lb_cat3.grid(row=0, column=9, columnspan=3, padx=30, pady=10, sticky='ew')
lb_cat4.grid(row=0, column=12, columnspan=2, padx=20, pady=10, sticky='ew')

# creating register labels and them category onto screen
lb_name = ['PD_TIA<1:0>', 'LA_disBIAS', 'OD_disBIAS', 'LPF_disBIAS', 'IBSel_TIA<1:0>', 'IBSel_LA<2:0>', 'IBSel_OD0<2:0>', 'AmpSel_OD<2:0>', 'BWSel_TIA<2:0>', 'BWSel_LA<2:0>', 'PreEm_OD<2:0>', 'RSSION', 'CH1_CLKOn']

lb_reg1 = Label(root, text=lb_name[0])
lb_reg2 = Label(root, text=lb_name[1])
lb_reg3 = Label(root, text=lb_name[2])
lb_reg4 = Label(root, text=lb_name[3])
lb_reg5 = Label(root, text=lb_name[4])
lb_reg6 = Label(root, text=lb_name[5])
lb_reg7 = Label(root, text=lb_name[6])
lb_reg8 = Label(root, text=lb_name[7])
lb_reg9 = Label(root, text=lb_name[8])
lb_reg10 = Label(root, text=lb_name[9])
lb_reg11 = Label(root, text=lb_name[10])
lb_reg12 = Label(root, text=lb_name[11])
lb_reg13 = Label(root, text=lb_name[12])

lb_reg1.grid(row=1, column=1)
lb_reg2.grid(row=1, column=2)
lb_reg3.grid(row=1, column=3)
lb_reg4.grid(row=1, column=4)
lb_reg5.grid(row=1, column=5)
lb_reg6.grid(row=1, column=6)
lb_reg7.grid(row=1, column=7)
lb_reg8.grid(row=1, column=8)
lb_reg9.grid(row=1, column=9)
lb_reg10.grid(row=1, column=10)
lb_reg11.grid(row=1, column=11)
lb_reg12.grid(row=1, column=12)
lb_reg13.grid(row=1, column=13)


# add entry to screen
entry_default_value = [1, 0, 0, 0, 1, 2, 3, 3, 5, 1, 7, 0, 0]

e4 = []
for j in range(13):
    e4.append( Entry(root, width=5) )
    e4[j].grid(row=2, column=j+1, padx=10, pady=10)
    e4[j].insert(END, str(entry_default_value[j]))

e3 = []
for j in range(13):
    e3.append( Entry(root, width=5) )
    e3[j].grid(row=3, column=j+1, padx=10, pady=10)
    e3[j].insert(END, str(entry_default_value[j]))

e2 = []
for j in range(13):
    e2.append( Entry(root, width=5) )
    e2[j].grid(row=4, column=j+1, padx=10, pady=10)
    e2[j].insert(END, str(entry_default_value[j]))

e1 = []
for j in range(13):
    e1.append( Entry(root, width=5) )
    e1[j].grid(row=5, column=j+1, padx=10, pady=10)
    e1[j].insert(END, str(entry_default_value[j]))


e_com = Entry(root, width=8, fg='red')
e_com.grid(row=2, column=15, padx=10, pady=12)
e_com.insert(END, 'COM3')

i2cAddr = Entry(root, width=8, fg='red')
i2cAddr.grid(row=3, column=15, padx=10, pady=12)
i2cAddr.insert(END, '0x21')


def button_run():

    # get entry values from GUI
    Reg_Val = []

    e4_value = []
    for i in range(13):
         e4_value.append( e4[i].get() )
    e4_value = [int(i) for i in e4_value]
    Reg_Val.extend( df_form_reg(e4_value) )

    e3_value = []
    for i in range(13):
         e3_value.append( e3[i].get() )
    e3_value = [int(i) for i in e3_value]
    Reg_Val.extend( df_form_reg(e3_value) )

    e2_value = []
    for i in range(13):
         e2_value.append( e2[i].get() )
    e2_value = [int(i) for i in e2_value]
    Reg_Val.extend( df_form_reg(e2_value) )

    e1_value = []
    for i in range(13):
         e1_value.append( e1[i].get() )
    e1_value = [int(i) for i in e1_value]
    Reg_Val.extend( df_form_reg(e1_value) )

    register_filename = "QTIA_gui_register_config.txt"   # need to change by users

    COM_Port = e_com.get()
    I2C_Addr = int(i2cAddr.get(), 0)                             # need to change according I2C Addr

    # Write GUI value to txt
    write_user_config(Reg_Val, register_filename)    

    Reg_Addr = []
    Reg_Val = []

    with open(register_filename, 'r') as infile:                  # read configuration file
        for line in infile.readlines():
            Reg_Addr += [int(line.split()[0], 16)]              # read register address and value
            Reg_Val += [int(line.split()[1], 16)]

    print (Reg_Addr)
    print (Reg_Val)

    # # set usb-iss iic master device
    # iss = UsbIss()
    # iss.open(COM_Port)
    # iss.setup_i2c(clock_khz=100)

    # regWritelen = len(Reg_Addr)
    # print (type(I2C_Addr))
    # print (regWritelen)

    # # write data into i2c slave
    # iss.i2c.write(I2C_Addr, 0, Reg_Val)       
    # time.sleep(0.02)

    # read_data = []
    # for i in range(regWritelen):                              # read data from i2c slave
    #     read_data += iss.i2c.read(I2C_Addr, Reg_Addr[i], 1)
    #     time.sleep(0.02)

#     # compare write in data with read back data
#     print('Check write-in registers:')
#     for i in range(regWritelen):
#         if Reg_Val[i] != read_data[i]:
#             print("Read-back didn't match with write-in: {} {} {}".format(hex(Reg_Addr[i]), hex(Reg_Val[i]), hex(read_data[i])) )
#     print('Write-in data check finished')

#     for i in range(3):                                      # if read back data matched with write in data, speaker will make a sound three times
#         winsound.Beep(freqency, duration)
#         time.sleep(0.01)

#     print("Ok!")




bt_run = Button(root, text='Run', padx=40, pady=10, command=button_run)
bt_run.grid(row=1, column=15)

root.mainloop()

