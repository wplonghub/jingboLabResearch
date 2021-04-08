import pandas as pd

def main():
    user_config_filename = "user_config_GBS20.txt"    # need to change by users
    register_filename = "register_config.txt"   # need to change by users

    df = pd.read_csv(user_config_filename, delim_whitespace=True, names= ['C1', 'V1', 'C2', 'V2', 'C3', 'V3', 'C4', 'V4', 'C5', 'V5']) 
    print (df)
    # df = df.astype('int32')

    reg_val = []


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

    reg_val.extend([r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, rA, rB, rC, rD, rE, rF])

    for i in reg_val:
        print (hex(i))
    
        



#-----------------------------------------------------------------------------------#
if __name__ == '__main__':
    main()
