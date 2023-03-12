import pandas as pd
import numpy as np

df = pd.read_excel('Test Question 2.xlsx') # reading the excel file
group_vals = set(df['Group']) #getting the number of groups in the data

out_df = pd.DataFrame(columns = df.columns.values.tolist())
print(out_df)

for group_num in range(1, max(group_vals) + 1):
    temp_df =  df[df['Group'] == group_num] # segmenting teh dataframe by the group value, and then rassigning into a temporrary dataframe
    
    df2 = { #creating a new row
        'Group': group_num, 
        'First': np.array(temp_df['First'])[0], 
        'Max': np.max(np.array(temp_df['Max'])),
        'Min': np.min(np.array(temp_df['Min'])),
        'Last': np.array(temp_df['Last'])[-1],
        'Sum': np.sum(np.array(temp_df['Sum']))
        }
    out_df = out_df.append(df2, ignore_index = True) #appending the row to the dataframe

print(out_df)