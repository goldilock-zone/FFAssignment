import pandas as pd
import numpy as np

df = pd.read_csv('CL Data.csv')

def manipulate(df : pd.DataFrame, n: int): #n is the lookback period
    #adding moving standard deviation
    df['Close Standard Deviation'] = df['Close'].std()
    df['Rolling Close Standard Deviation'] = df['Close'].rolling(n).std()


    # True Range ops
    high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())

    df['True Range'] = (df['High'] - df['Low']), abs(df['High'] - df['Close']), abs(df['Low'] - df['Close']))
    
    df['ATR'] = df['True Range'].rolling(n).mean()

    return df

df = manipulate(df, 10)
print(df)