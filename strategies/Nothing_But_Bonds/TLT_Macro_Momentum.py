import pandas as pd

def tlt_macro_momentum_string(df):

    if df['SMA_350'][df['ticker'] == 'TLT'].values[0] > df['SMA_550'][df['ticker'] == 'TLT'].values[0]:
        if df['RSI_60'][df['ticker'] == 'TLT'].values[0] > 62:
            alloc_tkr = 'SHY'

        else:
            alloc_tkr = 'TLT'

    else:
        if df['RSI_60'][df['ticker'] == 'TLT'].values[0] > 53:
            alloc_tkr = 'TLT'

        else:
            alloc_tkr = 'SHV'

    return alloc_tkr
