import pandas as pd

def tmv_momentum_string(df):

    if df['RSI_10'][df['ticker'] == 'TMF'].values[0] < 32:
        alloc_tkr = 'TMF'

    else:
        if df['SMA_15'][df['ticker'] == 'TMV'].values[0] > df['SMA_50'][df['ticker'] == 'TMV'].values[0]:
            if df['close'][df['ticker'] == 'TMV'].values[0] > df['SMA_135'][df['ticker'] == 'TMV'].values[0]:
                if df['RSI_10'][df['ticker'] == 'TMV'].values[0] > 71:
                    alloc_tkr = 'SHV'

                else:
                    if  df['RSI_60'][df['ticker'] == 'TMV'].values[0] > 59:
                        alloc_tkr = 'TLT'

                    else:
                        alloc_tkr = 'TMV'
            else:
                alloc_tkr = 'BND'
        else:
            alloc_tkr = 'BND'

    return alloc_tkr
