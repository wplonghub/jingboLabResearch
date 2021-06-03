import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
from math import sqrt, log10


def get_parameter(filename):

    df = pd.read_table(filename, delim_whitespace=True, index_col=0, names=['Wavelength', 'OpticalPower']) 
    print (df)

    # plt.figure()

    # testpl = df.plot()
    # plt.ylabel('Optical Power (dBm)')
    # testpl.figure.savefig('test.png', dpi=300)


    x = df.index.to_list()
    y = df['OpticalPower'].to_list()
    y_new = [10**(i/10 - 3) for i in y]

    print (type(x))
    # print (x)
    print (type(y_new))
    # print (y)


    mu = sum([a*b for a,b in zip(x,y_new)]) / sum(y_new)
    x0 = [i - mu for i in x]
    x0_2 = [i**2 for i in x0]
    sigma_2 = sum( [a*b for a,b in zip(x0_2,y_new)] ) / sum(y_new)
    sigma = sqrt(sigma_2)

    print (mu,sigma)


    peak_wavelength = df['OpticalPower'].idxmax(axis=0)
    print (peak_wavelength)
    # print (df.loc[847.096])

    peak_power = df['OpticalPower'].max()
    print (peak_power)

    # print (df['OpticalPower'].sum())
    total_power = sum(y_new) * 0.015
    print ('total power', total_power)

    total_dBm = 10 * log10(total_power * 1000)
    print ('total dBm', total_dBm)

    # sum_temp = 0
    # for i in y_new:
    #     if i > 1e-5:
    #         sum_temp += i
    # power_temp = sum_temp * 0.015
    # print ('power_temp', power_temp)
    # print ('test dBm', 10 * log10(power_temp * 1000) )


    # plt.plot(x,y_new,'b+:',label='data')
    # plt.plot(x,gaus(x,*popt),'ro:',label='fit')
    # plt.legend()
    # plt.title('Fig. 3 - Fit for Time Constant')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Voltage (V)')
    # plt.show()

    return [mu, sigma, peak_wavelength, peak_power, total_power, total_dBm]


def get_date_time(filename):
    filename_list = filename.replace("waveform_data_channel", "").replace(".txt", "").split('_')
    print (filename_list[1:])

    # date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
    return filename_list[1:]

def main():
    filename = "waveform_data_channel8_2021-04-20_23-20-24.txt"
    full_filename = 'test_data/' + filename
    out_filename = 'out_parameter.txt'
    par_list = get_parameter(full_filename)
    print (par_list)

    date_time_list = get_date_time(filename)


    f = open(out_filename, 'w')
    f.write('date time mu sigma peak_wavelength peak_power total_power total_dBm')
    f.write('\n')
    for item in date_time_list:
        f.write('%s ' % item)
    for listitem in par_list:
        f.write('%s ' % listitem)
    f.write('\n')
    f.close()


if __name__ == '__main__':
    main()
