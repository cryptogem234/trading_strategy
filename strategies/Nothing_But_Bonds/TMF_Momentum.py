import pandas as pd

def tmf_momentum_string(df):

    if df['RSI_10'][df['ticker'] == 'TMF'].values[0] < 32:
        alloc_tkr = 'TMF'
    else:
        if df['SMA_21'][df['ticker'] == 'TLT'].values[0] > df['SMA_110'][df['ticker'] == 'TLT'].values[0]:
            alloc_tkr = 'TMF'
        else:
            if df['EMA_8'][df['ticker'] == 'TLT'].values[0] < df['EMA_20'][df['ticker'] == 'TLT'].values[0]:
                alloc_tkr = 'SHV'
            else:
                alloc_tkr = 'UBT'

    return alloc_tkr
