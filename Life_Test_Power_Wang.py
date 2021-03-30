import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


# col = [Date, time, P1(dBm), P2(dBm), P3(dBm), P4(dBm)       , P5(dBm)       , P6(dBm)       , P7(dBm)       , P8(dBm)       , P9(dBm)       , P10(dBm)       , P11(dBm)       , P12(dBm)       , P13(dBm)       , P14(dBm)       , P15(dBm)       , P16(dBm)       , P17(dBm)       , P18(dBm)       , P19(dBm)       , P20(dBm)       , P21(dBm)       , P22(dBm)       , P23(dBm)       , P24(dBm)       , V1(dBm)       , V2(dBm)       , V3(dBm)       , V4(dBm)       , V5(dBm)       , V6(dBm)       , V7(dBm)       , V8(dBm)       , V9(dBm)       , V10(dBm)       , V11(dBm)       , V12(dBm)       , P13(dBm)       .1, V14(dBm)       , V15(dBm)       , V16(dBm)       , V17(dBm)       , V18(dBm)       , V19(dBm)       , V20(dBm)       , V21(dBm)       , V22(dBm)       , V23(dBm)       , V24(dBm)]
colname = ['Date']

for i in range(1, 25):
    colname.append('P' + str(i) + '(dBm)')

# voltage in dBm?
for i in range(1, 25):
    colname.append('V' + str(i) + '(dBm)')

colname.append('End')

# print (colname)
# print (len(colname))





colname2 = ['P1(dBm)', 'P2(dBm)', 'P3(dBm)', 'P4(dBm)', 'P5(dBm)', 'P6(dBm)', 'P7(dBm)', 'P8(dBm)', 'P9(dBm)', 'P10(dBm)', 'P11(dBm)', 'P12(dBm)', 'P13(dBm)', 'P14(dBm)', 'P15(dBm)', 'P16(dBm)', 'P17(dBm)', 'P18(dBm)', 'P19(dBm)', 'P20(dBm)', 'P21(dBm)', 'P22(dBm)', 'P23(dBm)', 'P24(dBm)', 'V1(dBm)', 'V2(dBm)', 'V3(dBm)', 'V4(dBm)', 'V5(dBm)', 'V6(dBm)', 'V7(dBm)', 'V8(dBm)', 'V9(dBm)', 'V10(dBm)', 'V11(dBm)', 'V12(dBm)', 'V13(dBm)', 'V14(dBm)', 'V15(dBm)', 'V16(dBm)', 'V17(dBm)', 'V18(dBm)', 'V19(dBm)', 'V20(dBm)', 'V21(dBm)', 'V22(dBm)', 'V23(dBm)', 'V24(dBm)', 'End']


# LifeTest_Opowers_20200105.TXT
df1 = pd.read_table("LifeTest_Opowers_20200105.TXT", index_col=0, parse_dates=True)#, names=colname)
df1 = df1.loc[df1.index > '2019-07-27 00:00:00']
df1.columns = colname2
df1 = df1.drop(columns=['End'])
print (df1.dtypes)
# print (df1)

# LifeTest_Opowers_20201205.TXT
df2 = pd.read_table("LifeTest_Opowers_20201205.TXT", index_col=0, parse_dates=True, names=colname2 )
df2 = df2.loc[df2.index < '2020-10-05 00:00:00']
df2 = df2.drop(columns=['End'])
print (df2.dtypes)
# print (df2)


# LifeTest_Opowers_20210324.TXT
df3 = pd.read_table("LifeTest_Opowers_20210324.TXT", index_col=0, parse_dates=True, names=colname2 )
df3 = df3.loc[df3.index < '2021-02-22 00:00:00']
df3 = df3.drop(columns=['End'])
print (df3.dtypes)
# print (df3)

dfapp = df1.append(df2).append(df3)
dfapp = dfapp.groupby(dfapp.index.date).mean()
dffig = dfapp.plot(marker = ".")
plt.legend(prop={'size': 3.5}, loc='center left', bbox_to_anchor=(1, 0.5))
# plt.show()
plt.savefig('foo.png', dpi=300)
dffig.figure.savefig('testAll.png', dpi=300)



# print (df1.iloc[1:])
# print (df1['P1(dBm)'])
# print (len(df1.columns) )
