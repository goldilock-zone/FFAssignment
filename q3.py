# from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
from stockstats import StockDataFrame

import pandas as pd
import numpy as np

data = pd.read_csv('CL Data.csv')

def manipulate(df : pd.DataFrame, n: int): #n is the lookback period
    #adding moving standard deviation
    df['Close Standard Deviation'] = df['Close'].std()
    df['Rolling Close Standard Deviation'] = df['Close'].rolling(n).std()


    # True Range ops
    high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())

    tr = np.array(np.maximum(low_close, np.maximum(high_low, high_close)))

    df['True Range'] = tr
    
    df['ATR'] = df['True Range'].rolling(n).mean()

    return df

df = manipulate(data, 10)

fig = go.Figure(data=[go.Candlestick(x=df['Timestamp'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                line = dict(width=1)
                )])

df_ti = StockDataFrame.retype(df)
print(df_ti)
fig.add_trace(go.Line(x=df['timestamp'],y=df_ti["atr"],))
fig.add_trace(go.Line(x=df['timestamp'],y=df_ti["rolling close standard deviation"],))

fig.show()
