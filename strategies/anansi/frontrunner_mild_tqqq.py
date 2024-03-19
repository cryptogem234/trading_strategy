import pandas as pd

def frontrunner_mild_tqqq(df):

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
                    if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.12:
                        if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                            alloc_df = df[df['ticker'].isin(['UVXY'])]
                        else:
                            if df['close'][df['ticker'] == 'TLT'].values[0] < df['SMA_126'][df['ticker'] == 'TLT'].values[0]:
                                alloc_df1 = df[df['ticker'].isin(['TQQQ'])]
                                alloc_df2 = df[df['ticker'].isin(['SVXY', 'TQQQ', 'TECL'])].sort_values(by='RSI_5',ascending=False).head(1)
                                alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                            else:
                                alloc_df = df[df['ticker'].isin(['TMF', 'IEF', 'BND'])].sort_values(by='RSI_20',ascending=True).head(1)
                    else:
                        if df['RSI_126'][df['ticker'] == 'SPY'].values[0] > df['RSI_126'][df['ticker'] == 'XLU'].values[0]:
                            alloc_df1 = df[df['ticker'].isin(['TQQQ'])]
                            alloc_df2 = df[df['ticker'].isin(['SVXY', 'TQQQ', 'TECL'])].sort_values(by='RSI_5',ascending=False).head(1)
                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                        else:
                            if df['close'][df['ticker'] == 'TLT'].values[0] < df['SMA_126'][df['ticker'] == 'TLT'].values[0]:
                                if df['RSI_21'][df['ticker'] == 'AGG'].values[0] > df['RSI_21'][df['ticker'] == 'TQQQ'].values[0]:
                                    alloc_df1 = df[df['ticker'].isin(['TQQQ'])]
                                else:
                                    alloc_df1 = df[df['ticker'].isin(['SVXY', 'VIXM', 'BTAL'])].sort_values(by='STDR_20',ascending=False).head(2)

                                if df['RSI_21'][df['ticker'] == 'AGG'].values[0] > df['RSI_21'][df['ticker'] == 'UPRO'].values[0]:
                                    alloc_df2 = df[df['ticker'].isin(['UPRO'])]
                                else:
                                    alloc_df2 = df[df['ticker'].isin(['SVXY', 'VIXM', 'BTAL'])].sort_values(by='STDR_20',ascending=False).head(2)

                                if df['RSI_21'][df['ticker'] == 'AGG'].values[0] > df['RSI_21'][df['ticker'] == 'SOXL'].values[0]:
                                    alloc_df3 = df[df['ticker'].isin(['SOXL'])]
                                else:
                                    alloc_df3 = df[df['ticker'].isin(['SVXY', 'VIXM', 'BTAL'])].sort_values(by='STDR_20',ascending=False).head(2)

                                alloc_df = pd.concat([alloc_df1, alloc_df2, alloc_df3], ignore_index=True, sort=False)

                            else:
                                alloc_df = df[df['ticker'].isin(['TMF', 'IEF', 'BND'])].sort_values(by='RSI_20',ascending=True).head(1)

    return alloc_df