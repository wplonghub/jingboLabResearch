import pandas as pd
import os
import sys
import time
import winsound
from usb_iss import UsbIss, defs

'''
@author: Peilong Wang
@date: Apr. 7, 2021
This script as a generic I2C cofniguration software to configure I2C slave. The I2C reg configuration data is read into a xxx.dat file.
The UsbIss as I2C master deivce is used to write and read I2C slave register.
'''

def df_form_reg(l):
    r0 = l[0] << 4 | l[1]
    r1 = l[2] << 4 | l[3]
    r2 = l[4] << 7 | l[5] << 4 | l[6] << 3 | l[7]
    r3 = l[8] << 7 | l[9] << 6 | l[10] << 4 | l[11] << 3 | l[12]

    return [r0, r1, r2, r3]
    

def write_user_config(user_config_filename, out_filename):
    df = pd.read_table(user_config_filename, delim_whitespace=True) 
    Reg_Val = []
    for column in df.columns[::-1][:-1]:
        Reg_Val.extend( df_form_reg(df[column]) )


    print ([hex(i) for i in Reg_Val])
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
def main():
    user_config_filename = "QTIA_user_config.txt"    # need to change by users
    register_filename = "QTIA_register_config.txt"   # need to change by users

    COM_Port = "COM3"                           # need to change according com port
    I2C_Addr = 0x20                             # need to change according I2C Addr

    Reg_Addr = []
    Reg_Val = []

    write_user_config(user_config_filename, register_filename)    # comment out this line if you want to use register_filename directly

    with open(register_filename, 'r') as infile:                  # read configuration file
        for line in infile.readlines():
            Reg_Addr += [int(line.split()[0], 16)]              # read register address and value
            Reg_Val += [int(line.split()[1], 16)]

    print (Reg_Addr)
    print (Reg_Val)

    # set usb-iss iic master device
    iss = UsbIss()
    iss.open(COM_Port)
    iss.setup_i2c(clock_khz=100)

    regWritelen = len(Reg_Addr)
    print (type(I2C_Addr))
    print (regWritelen)

    # write data into i2c slave
    iss.i2c.write(I2C_Addr, 0, Reg_Val)       
    time.sleep(0.02)

    # for i in range(regWritelen):                              # write data into i2c slave
    #     print (I2C_Addr, hex(Reg_Addr[i]), hex(Reg_Val[i]))
    #     iss.i2c.write(I2C_Addr, Reg_Addr[i], Reg_Val[i])
    #     time.sleep(0.02)

    read_data = []
    for i in range(regWritelen):                              # read data from i2c slave
        read_data += iss.i2c.read(I2C_Addr, Reg_Addr[i], 1)
        time.sleep(0.02)

    # compare write in data with read back data
    print('Check write-in registers:')
    for i in range(regWritelen):
        if Reg_Val[i] != read_data[i]:
            print("Read-back didn't match with write-in: {} {} {}".format(hex(Reg_Addr[i]), hex(Reg_Val[i]), hex(read_data[i])) )
    print('Write-in data check finished')

    for i in range(3):                                      # if read back data matched with write in data, speaker will make a sound three times
        winsound.Beep(freqency, duration)
        time.sleep(0.01)

    print("Ok!")
#-----------------------------------------------------------------------------------#
if __name__ == '__main__':
    main()
