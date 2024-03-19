import pandas as pd
from strategies.anansi.volmageddon import volmageddon

def indecent_vixation(df):

    if df['RSI_14'][df['ticker'] == 'SPY'].values[0] < 30:
        alloc_df = df[df['ticker'].isin(['SVXY'])]
    else:
        if df['RSI_14'][df['ticker'] == 'QQQ'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['SVXY'])]
        else:
            if df['CUMR_5'][df['ticker'] == 'SPY'].values[0] < -0.10:
                alloc_df = df[df['ticker'].isin(['SVXY'])]
            else:
                if df['RSI_14'][df['ticker'] == 'SPY'].values[0] > 80:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    if df['close'][df['ticker'] == 'SPY'].values[0] > df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                        if df['SMA_3'][df['ticker'] == 'SPY'].values[0] < df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                            alloc_df1 = df[df['ticker'].isin(['TQQQ'])]
                            alloc_df2 = df[df['ticker'].isin(['SVXY', 'TQQQ', 'TECL'])].sort_values(by='RSI_5',ascending=False).head(1)
                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                        else:
                            ### volmageddon 2.0 ###
                            alloc_df = volmageddon(df)

                    else:
                        if df['SMA_3'][df['ticker'] == 'SPY'].values[0] > df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                            alloc_df1 = df[df['ticker'].isin(['SQQQ'])]
                            alloc_df2 = df[df['ticker'].isin(['VIXY', 'SQQQ', 'TECS'])].sort_values(by='RSI_5',ascending=False).head(1)
                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                        else:
                            ### volmageddon 2.0 ###
                            alloc_df = volmageddon(df)

    return alloc_df











