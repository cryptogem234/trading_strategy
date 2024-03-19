import pandas as pd

def frontrunner_200d_inverse(df):

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
                    if df['close'][df['ticker'] == 'SPY'].values[0] > df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                        if df['SMA_3'][df['ticker'] == 'SPY'].values[0] < df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                            alloc_df1 = df[df['ticker'].isin(['TQQQ','TMF'])].sort_values(by='RSI_10',ascending=False).head(1)
                            alloc_df2 = df[df['ticker'].isin(['UPRO', 'UGL', 'TECL'])].sort_values(by='RSI_10',ascending=False).head(1)
                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                        else:
                            if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 80:
                                alloc_df = df[df['ticker'].isin(['VIXY'])]
                            else:
                                if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
                                    alloc_df = df[df['ticker'].isin(['VIXY'])]
                                else:
                                    if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
                                        alloc_df = df[df['ticker'].isin(['TQQQ'])]
                                    else:
                                        if df['STDR_10'][df['ticker'] == 'UVXY'].values[0] > 0.10:
                                            alloc_df = df[df['ticker'].isin(['BIL'])]
                                        else:
                                            if df['RSI_5'][df['ticker'] == 'SPXU'].values[0] > df['RSI_5'][df['ticker'] == 'SVXY'].values[0]:
                                                alloc_df = df[df['ticker'].isin(['SVXY'])]
                                            else:
                                                alloc_df = df[df['ticker'].isin(['SPXU'])]
                    else:
                        if df['SMA_3'][df['ticker'] == 'SPY'].values[0] > df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                            alloc_df1 = df[df['ticker'].isin(['SQQQ', 'UGL'])].sort_values(by='RSI_10',ascending=True).head(1)
                            alloc_df2 = df[df['ticker'].isin(['SPXU', 'TYO'])].sort_values(by='RSI_10',ascending=False).head(1)
                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                        else:
                            if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 80:
                                alloc_df = df[df['ticker'].isin(['VIXM'])]
                            else:
                                if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
                                    alloc_df = df[df['ticker'].isin(['VIXM'])]
                                else:
                                    if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 31:
                                        alloc_df = df[df['ticker'].isin(['TECL'])]
                                    else:
                                        if df['RSI_10'][df['ticker'] == 'IEF'].values[0] > df['RSI_20'][df['ticker'] == 'PSQ'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['TECL'])]
                                        else:
                                            if df['close'][df['ticker'] == 'SPY'].values[0] > df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                                                alloc_df = df[df['ticker'].isin(['BTAL','XLP','UGL'])].sort_values(by='RSI_5',ascending=False).head(2)
                                            else:
                                                alloc_df1 = df[df['ticker'].isin(['SQQQ'])]
                                                alloc_df2 = df[df['ticker'].isin(['TLT','SQQQ','TECS'])].sort_values(by='RSI_5',ascending=False).head(1)
                                                alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)

    return alloc_df




