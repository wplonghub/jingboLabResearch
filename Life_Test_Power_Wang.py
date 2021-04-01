import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


colname2 = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'End']


# LifeTest_Opowers_20200105.TXT
df1 = pd.read_table("LifeTest_Opowers_20200105.TXT", index_col=0, parse_dates=True)#, names=colname)
df1 = df1.loc[df1.index > '2019-07-27 00:00:00']
df1.columns = colname2
df1 = df1.drop(columns=['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'End'])
print (df1.dtypes)
# print (df1)

# LifeTest_Opowers_20201205.TXT
df2 = pd.read_table("LifeTest_Opowers_20201205.TXT", index_col=0, parse_dates=True, names=colname2 )
df2 = df2.loc[df2.index < '2020-10-05 00:00:00']
df2 = df2.loc[(df2.index < '2020-04-10 00:00:00') | (df2.index > '2020-04-17 00:00:00')]
df2 = df2.drop(columns=['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'End'])
print (df2.dtypes)
# print (df2)


# # LifeTest_Opowers_20210324.TXT
# df3 = pd.read_table("LifeTest_Opowers_20210324.TXT", index_col=0, parse_dates=True, names=colname2 )
# df3 = df3.loc[df3.index < '2021-02-22 00:00:00']
# df3 = df3.drop(columns=['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'End'])
# print (df3.dtypes)
# # print (df3)

dfapp = df1.append(df2) #.append(df3)
dfapp = dfapp.groupby(dfapp.index.date).mean()
maxValues = dfapp.max()
minValues = dfapp.min()
deltaValues = maxValues - minValues
print (maxValues)
print (minValues)
print (deltaValues)
print (type(deltaValues) )
deltaValues.to_csv('power_differences.csv')
# plt.figure(figsize=(3, 3))
dffig = dfapp.plot(marker = ".", linestyle = 'None', figsize = (9, 6) )
# plt.figure(figsize=(1.2,1))
plt.legend(prop={'size': 8}, loc='center left', bbox_to_anchor=(1, 0.5))
# plt.show()
plt.xlabel('Date', fontsize=18)
plt.ylabel('Optical Power (dBm)', fontsize=16)
plt.savefig('foo.png', dpi=300)
dffig.figure.savefig('testAll.png', dpi=300)



# print (df1.iloc[1:])
# print (df1['P1'])
# print (len(df1.columns) )
