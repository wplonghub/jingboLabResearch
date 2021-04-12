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


def df_form_reg(df):
    l1 = df['V1'][:7].astype('int32')
    r0 = l1[0] << 4 | l1[1] << 1 | l1[2]
    r1 = l1[3] << 4 | l1[4]
    r2 = l1[5] << 4 | l1[6]

    l2 = df['V2'][:7].astype('int32')
    r3 = l2[0] << 6 | l2[1] << 5 | l2[2] << 4 | l2[3] << 3 | l2[4] << 2 | l2[5] << 1 | l2[6]

    l3 = df['V3'][:8].astype('int32')
    r4 = l3[0] << 7 | l3[1] << 6 | l3[2] << 5 | l3[3] << 4 | l3[4] << 3 | l3[5] << 2 | l3[6] << 1 | l3[7]

    l4 = df['V4'][:6].astype('int32')
    r5 = l4[0] << 4 | l4[1]
    r6 = l4[2] << 4 | l4[3]
    r7 = l4[4] << 4 | l4[5]

    l5 = df['V5'][:8].astype('int32')
    r8 = l5[0] << 7 | l5[1] << 6 | l5[2] << 5 | l5[3]
    r9 = l5[4] << 4 | l5[5] << 3 | l5[6] << 2 | l5[7]
    
    l6 = df['V1'][9:].astype('int32').tolist()
    rA = l6[0] << 7 | l6[1] << 6 | l6[2] << 5 | l6[3] << 4 | l6[4] << 3 | l6[5] << 2 | l6[6] << 1 | l6[7]

    l7 = df['V2'][9:16].astype('int32').tolist()
    rB = l7[0] << 6 | l7[1] << 5 | l7[2] << 4 | l7[3] << 3 | l7[4] << 2 | l7[5] << 1 | l7[6]

    l8 = df['V3'][9:16].astype('int32').tolist()
    rC = l8[0] << 6 | l8[1] << 5 | l8[2] << 4 | l8[3] << 3 | l8[4] << 2 | l8[5] << 1 | l8[6]

    l9 = df['V4'][9:16].astype('int32').tolist()
    rD = l9[0] << 7 | l9[1] << 5 | l9[2] << 4 | l9[3] << 3 | l9[4] << 2 | l9[5] << 1 | l9[6]

    l10 = df['V5'][9:15].astype('int32').tolist()
    rE = l10[0] << 5 | l10[1] << 4 | l10[2] << 3 | l10[3] << 1 | l10[4]
    rF = l10[5]

    return [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, rA, rB, rC, rD, rE, rF]
    

def read_and_write_user_config(user_config_filename, out_filename):

    df = pd.read_csv(user_config_filename, delim_whitespace=True, names= ['C1', 'V1', 'C2', 'V2', 'C3', 'V3', 'C4', 'V4', 'C5', 'V5']) 
    Reg_Val = []

    Reg_Val.extend( df_form_reg(df) )

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
    user_config_filename = "GBS20_user_config.txt"    # need to change by users
    register_filename = "GBS20_register_config.txt"   # need to change by users

    COM_Port = "COM3"                           # need to change according com port
    I2C_Addr = 0x20                             # need to change according I2C Addr

    Reg_Addr = []
    Reg_Val = []

    read_and_write_user_config(user_config_filename, register_filename)    # comment out this line if you want to use register_filename directly

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
