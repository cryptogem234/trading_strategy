import pandas as pd

df = pd.DataFrame()

if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] > 79:
    alloc_df = df[df['ticker'].isin(['UVXY'])]
else:
    if df['RSI_10'][df['ticker'] == 'XLK'].values[0] > 79:
        alloc_df = df[df['ticker'].isin(['UVXY'])]
    else:
        if df['RSI_10'][df['ticker'] == 'VOX'].values[0] > 79:
            alloc_df = df[df['ticker'].isin(['UVXY'])]
        else:
            if df['RSI_10'][df['ticker'] == 'VTV'].values[0] > 79:
                alloc_df = df[df['ticker'].isin(['UVXY'])]
            else:
                if df['RSI_10'][df['ticker'] == 'SOXX'].values[0] > 79:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 79:
                        alloc_df = df[df['ticker'].isin(['UVXY'])]
                    else:
                        if df['RSI_10'][df['ticker'] == 'VTV'].values[0] > 79:
                            alloc_df = df[df['ticker'].isin(['UVXY'])]
                        else:
                            if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 30:
                                alloc_df = df[df['ticker'].isin(['TQQQ'])]
                            else:
                                if df['close'][df['ticker'] == 'SVXY'].values[0] > df['SMA_24'][df['ticker'] == 'SVXY'].values[0]:
                                    alloc_df = df[df['ticker'].isin(['SVXY', 'VTI'])]
                                else:
                                    alloc_df = df[df['ticker'].isin(['BTAL'])]
