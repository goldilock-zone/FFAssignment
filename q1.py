import numpy as np
import pandas as pd
import time

def slicer(n): #slicer gives viable cominations of indexes in the array to test for
    sliced = []

    for i in range(n):
        for j in range(i):
            sliced.append((j,i))
    
    return sliced 

def stockBuySell(A: np.array):
    n = len(A)
    sliced_array = slicer(n)
    profit_tuple = []

    for start, end in sliced_array: #populating the profit_tuple in list in the format: (start,end), diff)
        int_arr = A[start:end]
        if len(int_arr) > 0:
            diff = int_arr[-1] - int_arr[0]
            profit_tuple.append(((start,end), diff))
    
    df = pd.DataFrame(columns = ['Diff', 'Periods'])
    for dates, diff in profit_tuple:
        if diff >= 0:
            df2 = { #creating a new row
            'Diff': diff, 
            'Periods': dates 
            }
            df = df.append(df2, ignore_index = True)

    final_df = df.sort_values(by=['Diff'], ascending=False).copy()
    final_df.reindex([i for i in range(df.shape[0])])
    
    covered_array = [final_df.iloc[0]['Periods']] #This array has the possible trade periods
    for i in range(1, final_df.shape[0]):
        add_flag = True
        cur_start, cur_end = final_df.iloc[i]['Periods']
        for start, end in covered_array:
            if cur_end <= end and cur_end >= start: #checking for overlaps between time periods
                add_flag = False
        if add_flag:
            covered_array.append(final_df.iloc[i]['Periods'])

    return list(reversed(covered_array))
          
print(stockBuySell([100,180,260,310,40,535,695]))