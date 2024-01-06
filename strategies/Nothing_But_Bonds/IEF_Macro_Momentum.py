import pandas as pd

def ief_momentum_string(df):

    if df['SMA_200'][df['ticker'] == 'IEF'].values[0] > df['SMA_450'][df['ticker'] == 'IEF'].values[0]:
        alloc_tkr = 'IEF'
    else:
        alloc_tkr = 'SHV'

    return alloc_tkr