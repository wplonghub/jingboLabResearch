import os
import sys
import time
import winsound
from usb_iss import UsbIss, defs
'''
@author: Lily Zhang
@date: March 28, 2021
This script as a generic I2C cofniguration software to configure I2C slave. The I2C reg configuration data is read into a xxx.dat file.
The UsbIss as I2C master deivce is used to write and read I2C slave register.
'''
#-----------------------------------------------------------------------------------#
freqency = 1000
duration = 200
#-----------------------------------------------------------------------------------#
def main():
    config_filename = "GBS20V1_I2C_Config.txt"                    # need to change by users
    COM_Port = "COM3"                                             # need to change according com port

    I2C_Addr = 0x20
    Reg_Addr = []
    Reg_Val = []
    with open(config_filename, 'r') as infile:                  # read configuration file
        for line in infile.readlines():
            if len(line.split()) == 1:                          # read I2C address
                I2C_Addr = hex(int(line.split()[0], 16))
            else:                                               # read register address and value
                Reg_Addr += [int(line.split()[0], 16)]
                Reg_Val += [int(line.split()[1], 16)]

    print (Reg_Addr)
    print (Reg_Val)

    # set usb-iss iic master device
    iss = UsbIss()
    iss.open(COM_Port)
    iss.setup_i2c()

    regWritelen = 16

    for i in range(regWritelen):                              # write data into i2c slave
        print (I2C_Addr, hex(Reg_Addr[i]), hex(Reg_Val[i]))
        iss.i2c.write(I2C_Addr, Reg_Addr[i], Reg_Val[i])
        time.sleep(0.02)

    regReadlen = 17
    read_data = []
    read_data = Reg_Val
    for i in range(regReadlen):                              # read data from i2c slave
        read_data += [iss.i2c.read(I2C_Addr, Reg_Addr[i], 1)]
        time.sleep(0.02)

    # compare write in data with read back data
    print('Check write-in registers:')
    for i in range(regWritelen):
        if Reg_Val[i] != read_data[i]:
            print("Read-back didn't match with write-in: {} {} {}".format(hex(Reg_Addr[i]), hex(Reg_Val[i]), hex(read_data[i])) )
    print('Write-in data check finisehd')

    # check read-only register data
    print('Read read-only registers:')
    for i in range(regWritelen, regReadlen):
        print(hex(Reg_Addr[i]), hex(read_data[i]))

    for i in range(3):                                      # if read back data matched with write in data, speaker will make a sound three times
        winsound.Beep(freqency, duration)
        time.sleep(0.01)

    print("Ok!")
#-----------------------------------------------------------------------------------#
if __name__ == '__main__':
    main()
