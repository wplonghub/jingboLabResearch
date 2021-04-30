import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table("test_data/waveform_data_channel8_2021-04-20_23-20-24.txt", delim_whitespace=True, index_col=0, names=['Wavelength', 'OpticalPower']) 
print (df)

# plt.figure()
testpl = df.plot()
plt.ylabel('Optical Power (dBm)')
testpl.figure.savefig('test.png', dpi=300)
# input('pase')

peak_wavelength = df['OpticalPower'].idxmax(axis=0)
print (peak_wavelength)
# print (df.loc[847.096])

peak_power = df['OpticalPower'].max()
print (peak_power)

# print (df['OpticalPower'].sum())
total_power = df['OpticalPower'].sum() * 1500
print (total_power)
