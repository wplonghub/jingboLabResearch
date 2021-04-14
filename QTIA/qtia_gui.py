import pandas as pd
import os
import sys
import time
# import winsound
# from usb_iss import UsbIss, defs

from tkinter import *

'''
@author: Peilong Wang
@date: Apr. 7, 2021
'''
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

# labels
lb_ch1 = Label(root, text="CH1")
lb_ch2 = Label(root, text="CH2")
lb_ch3 = Label(root, text="CH3")
lb_ch4 = Label(root, text="CH4")

lb_cat1 = Label(root, text="Bias enabling", bg='grey')
lb_cat2 = Label(root, text="Bias selection", bg='grey')
lb_cat3 = Label(root, text="Bandwidth selection", bg='grey')
lb_cat4 = Label(root, text="Miscellaneous", bg='grey')

lb_name = ['PD_TIA<1:0>', 'LA_disBIAS', 'OD_disBIAS', 'LPF_disBIAS', 'IBSel_TIA<1:0>', 'IBSel_LA<2:0>', 'IBSel_OD0<2:0>', 'AmpSel_OD<2:0>', 'BWSel_TIA<2:0>', 'BWSel_LA<2:0>', 'PreEm_OD<2:0>', 'RSSION', 'CH1_CLKOn']
print (len(lb_name))
print (lb_name)

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


# shoving labels onto screen
lb_ch4.grid(row=2, column=0)
lb_ch3.grid(row=3, column=0)
lb_ch2.grid(row=4, column=0)
lb_ch1.grid(row=5, column=0)

lb_cat1.grid(row=0, column=1, columnspan=4, padx=40, pady=10, sticky='ew')
lb_cat2.grid(row=0, column=5, columnspan=4, padx=40, pady=10, sticky='ew')
lb_cat3.grid(row=0, column=9, columnspan=3, padx=30, pady=10, sticky='ew')
lb_cat4.grid(row=0, column=12, columnspan=2, padx=20, pady=10, sticky='ew')

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
e4 = []
for j in range(13):
    e4.append( Entry(root, width=5) )
    e4[j].grid(row=2, column=j+1, padx=10, pady=10)
    e4[j].insert(END, '0')

e3 = []
for j in range(13):
    e3.append( Entry(root, width=5) )
    e3[j].grid(row=3, column=j+1, padx=10, pady=10)
    e3[j].insert(END, '0')

e2 = []
for j in range(13):
    e2.append( Entry(root, width=5) )
    e2[j].grid(row=4, column=j+1, padx=10, pady=10)
    e2[j].insert(END, '0')

e1 = []
for j in range(13):
    e1.append( Entry(root, width=5) )
    e1[j].grid(row=5, column=j+1, padx=10, pady=10)
    e1[j].insert(END, '0')


e_com = Entry(root, width=8, fg='red')
e_com.grid(row=2, column=15, padx=10, pady=12)
e_com.insert(END, 'COM3')

i2cAddr = Entry(root, width=8, fg='red')
i2cAddr.grid(row=3, column=15, padx=10, pady=12)
i2cAddr.insert(END, '0x20')



def df_form_reg(el):
    # assembly to resiger map
    l = []
    l.append( el[10] )
    l.append( el[11] )
    l.append( el[4] )
    l.append( el[6] )
    l.append( el[1] )
    l.append( el[0] )
    l.append( el[2] )
    l.append( el[7] )
    l.append( el[12] )
    l.append( el[3] )
    l.append( el[5] )
    l.append( el[9] )
    l.append( el[8] )

    r0 = l[0] << 4 | l[1]
    r1 = l[2] << 4 | l[3]
    r2 = l[4] << 7 | l[5] << 4 | l[6] << 3 | l[7]
    r3 = l[8] << 7 | l[9] << 6 | l[10] << 4 | l[11] << 3 | l[12]

    return [r0, r1, r2, r3]

def button_run():
    Reg_Val = []

    el4 = []
    for i in range(13):
         el4.append( e4[i].get() )
    el4 = [int(i) for i in el4]
    print (el4)
    Reg_Val.extend( df_form_reg(el4) )

    el3 = []
    for i in range(13):
         el3.append( e4[i].get() )
    el3 = [int(i) for i in el3]
    print (el3)
    Reg_Val.extend( df_form_reg(el3) )

    el2 = []
    for i in range(13):
         el2.append( e4[i].get() )
    el2 = [int(i) for i in el2]
    print (el2)
    Reg_Val.extend( df_form_reg(el2) )

    el1 = []
    for i in range(13):
         el1.append( e4[i].get() )
    el1 = [int(i) for i in el1]
    print (el1)
    Reg_Val.extend( df_form_reg(el1) )

    print (Reg_Val)


    register_filename = "QTIA_gui_register_config.txt"   # need to change by users

    COM_Port = e_com.get()
    I2C_Addr = int(i2cAddr.get(), 0)                             # need to change according I2C Addr
    print (I2C_Addr)

    write_user_config(Reg_Val, register_filename)    # comment out this line if you want to use register_filename directly


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

    # # for i in range(regWritelen):                              # write data into i2c slave
    # #     print (I2C_Addr, hex(Reg_Addr[i]), hex(Reg_Val[i]))
    # #     iss.i2c.write(I2C_Addr, Reg_Addr[i], Reg_Val[i])
    # #     time.sleep(0.02)

    # read_data = []
    # for i in range(regWritelen):                              # read data from i2c slave
    #     read_data += iss.i2c.read(I2C_Addr, Reg_Addr[i], 1)
    #     time.sleep(0.02)

    # # compare write in data with read back data
    # print('Check write-in registers:')
    # for i in range(regWritelen):
    #     if Reg_Val[i] != read_data[i]:
    #         print("Read-back didn't match with write-in: {} {} {}".format(hex(Reg_Addr[i]), hex(Reg_Val[i]), hex(read_data[i])) )
    # print('Write-in data check finished')

    # for i in range(3):                                      # if read back data matched with write in data, speaker will make a sound three times
    #     winsound.Beep(freqency, duration)
    #     time.sleep(0.01)

    # print("Ok!")




bt_run = Button(root, text='Run', padx=40, pady=10, command=button_run)
bt_run.grid(row=1, column=15)







root.mainloop()



# e4_1 = Entry(root, width=5)
# e4_1.grid(row=2, column=1, padx=10, pady=10)
# e4_2 = Entry(root, width=5)
# e4_2.grid(row=2, column=2, padx=10, pady=10)
# e4_3 = Entry(root, width=5)
# e4_3.grid(row=2, column=3, padx=10, pady=10)
# e4_4 = Entry(root, width=5)
# e4_4.grid(row=2, column=4, padx=10, pady=10)
# e4_5 = Entry(root, width=5)
# e4_5.grid(row=2, column=5, padx=10, pady=10)
# e4_6 = Entry(root, width=5)
# e4_6.grid(row=2, column=6, padx=10, pady=10)
# e4_7 = Entry(root, width=5)
# e4_7.grid(row=2, column=7, padx=10, pady=10)
# e4_8 = Entry(root, width=5)
# e4_8.grid(row=2, column=8, padx=10, pady=10)
# e4_9 = Entry(root, width=5)
# e4_9.grid(row=2, column=9, padx=10, pady=10)
# e4_10 = Entry(root, width=5)
# e4_10.grid(row=2, column=10, padx=10, pady=10)
# e4_11 = Entry(root, width=5)
# e4_11.grid(row=2, column=11, padx=10, pady=10)
# e4_12 = Entry(root, width=5)
# e4_12.grid(row=2, column=12, padx=10, pady=10)
# e4_13 = Entry(root, width=5)
# e4_13.grid(row=2, column=13, padx=10, pady=10)



# e3_1 = Entry(root, width=5)
# e3_1.grid(row=3, column=1, padx=10, pady=10)
# e3_2 = Entry(root, width=5)
# e3_2.grid(row=3, column=2, padx=10, pady=10)
# e3_3 = Entry(root, width=5)
# e3_3.grid(row=3, column=3, padx=10, pady=10)
# e3_4 = Entry(root, width=5)
# e3_4.grid(row=3, column=4, padx=10, pady=10)
# e3_5 = Entry(root, width=5)
# e3_5.grid(row=3, column=5, padx=10, pady=10)
# e3_6 = Entry(root, width=5)
# e3_6.grid(row=3, column=6, padx=10, pady=10)
# e3_7 = Entry(root, width=5)
# e3_7.grid(row=3, column=7, padx=10, pady=10)
# e3_8 = Entry(root, width=5)
# e3_8.grid(row=3, column=8, padx=10, pady=10)
# e3_9 = Entry(root, width=5)
# e3_9.grid(row=3, column=9, padx=10, pady=10)
# e3_10 = Entry(root, width=5)
# e3_10.grid(row=3, column=10, padx=10, pady=10)
# e3_11 = Entry(root, width=5)
# e3_11.grid(row=3, column=11, padx=10, pady=10)
# e3_12 = Entry(root, width=5)
# e3_12.grid(row=3, column=12, padx=10, pady=10)
# e3_13 = Entry(root, width=5)
# e3_13.grid(row=3, column=13, padx=10, pady=10)


# e2_1 = Entry(root, width=5)
# e2_1.grid(row=4, column=1, padx=10, pady=10)
# e2_2 = Entry(root, width=5)
# e2_2.grid(row=4, column=2, padx=10, pady=10)
# e2_3 = Entry(root, width=5)
# e2_3.grid(row=4, column=3, padx=10, pady=10)
# e2_4 = Entry(root, width=5)
# e2_4.grid(row=4, column=4, padx=10, pady=10)
# e2_5 = Entry(root, width=5)
# e2_5.grid(row=4, column=5, padx=10, pady=10)
# e2_6 = Entry(root, width=5)
# e2_6.grid(row=4, column=6, padx=10, pady=10)
# e2_7 = Entry(root, width=5)
# e2_7.grid(row=4, column=7, padx=10, pady=10)
# e2_8 = Entry(root, width=5)
# e2_8.grid(row=4, column=8, padx=10, pady=10)
# e2_9 = Entry(root, width=5)
# e2_9.grid(row=4, column=9, padx=10, pady=10)
# e2_10 = Entry(root, width=5)
# e2_10.grid(row=4, column=10, padx=10, pady=10)
# e2_11 = Entry(root, width=5)
# e2_11.grid(row=4, column=11, padx=10, pady=10)
# e2_12 = Entry(root, width=5)
# e2_12.grid(row=4, column=12, padx=10, pady=10)
# e2_13 = Entry(root, width=5)
# e2_13.grid(row=4, column=13, padx=10, pady=10)



# e1_1 = Entry(root, width=5)
# e1_1.grid(row=5, column=1, padx=10, pady=10)
# e1_2 = Entry(root, width=5)
# e1_2.grid(row=5, column=2, padx=10, pady=10)
# e1_3 = Entry(root, width=5)
# e1_3.grid(row=5, column=3, padx=10, pady=10)
# e1_4 = Entry(root, width=5)
# e1_4.grid(row=5, column=4, padx=10, pady=10)
# e1_5 = Entry(root, width=5)
# e1_5.grid(row=5, column=5, padx=10, pady=10)
# e1_6 = Entry(root, width=5)
# e1_6.grid(row=5, column=6, padx=10, pady=10)
# e1_7 = Entry(root, width=5)
# e1_7.grid(row=5, column=7, padx=10, pady=10)
# e1_8 = Entry(root, width=5)
# e1_8.grid(row=5, column=8, padx=10, pady=10)
# e1_9 = Entry(root, width=5)
# e1_9.grid(row=5, column=9, padx=10, pady=10)
# e1_10 = Entry(root, width=5)
# e1_10.grid(row=5, column=10, padx=10, pady=10)
# e1_11 = Entry(root, width=5)
# e1_11.grid(row=5, column=11, padx=10, pady=10)
# e1_12 = Entry(root, width=5)
# e1_12.grid(row=5, column=12, padx=10, pady=10)
# e1_13 = Entry(root, width=5)
# e1_13.grid(row=5, column=13, padx=10, pady=10)



    # l[0] = el[10]
    # l[1] = el[11]
    # l[2] = el[4]
    # l[3] = el[6]
    # l[4] = el[1]
    # l[5] = el[0]
    # l[6] = el[2]
    # l[7] = el[7]
    # l[8] = el[12]
    # l[9] = el[3]
    # l[10] = el[5]
    # l[11] = el[9]
    # l[12] = el[8]
