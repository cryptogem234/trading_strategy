import pandas as pd

def moderated_wmdyn_ftlt(df):

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
                            if df['RSI_14'][df['ticker'] == 'QQQ'].values[0] < 30:
                                alloc_df1 = df[df['ticker'].isin(['TECL'])]
                                alloc_df2 = df[df['ticker'].isin(['SVXY','FNGU','TECL','TLT'])].sort_values(by='RSI_5',ascending=False).head(1)
                                alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                            else:
                                if df['RSI_14'][df['ticker'] == 'SOXX'].values[0] < 30:
                                    alloc_df1 = df[df['ticker'].isin(['SOXL'])]
                                    alloc_df2 = df[df['ticker'].isin(['SVXY', 'SOXL', 'TECL', 'TLT'])].sort_values(by='RSI_5', ascending=False).head(1)
                                    alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                                else:
                                    if df['RSI_10'][df['ticker'] == 'BIL'].values[0] < df['RSI_10'][df['ticker'] == 'TLT'].values[0]:
                                        alloc_df = df[df['ticker'].isin(['TECL','SOXL'])]
                                    else:
                                        if df['RSI_5'][df['ticker'] == 'SPY'].values[0] < 25:
                                            if df['RSI_5'][df['ticker'] == 'BSV'].values[0] < df['RSI_5'][df['ticker'] == 'VTV'].values[0]:
                                                alloc_df1 = df[df['ticker'].isin(['SOXS'])]
                                                alloc_df2 = df[df['ticker'].isin(['UVXY', 'SOXS','TLT'])].sort_values(by='RSI_5', ascending=False).head(1)
                                                alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                                            else:
                                                alloc_df1 = df[df['ticker'].isin(['SOXL'])]
                                                alloc_df2 = df[df['ticker'].isin(['SVXY', 'SOXL', 'FNGU', 'TLT'])].sort_values(by='RSI_5', ascending=False).head(1)
                                                alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                                        else:
                                            if df['STDR_10'][df['ticker'] == 'SPY'].values[0] > 0.03:
                                                alloc_df = df[df['ticker'].isin(['VIXY', 'TMF', 'SPXU', 'SOXS'])].sort_values(by='RSI_5', ascending=False).head(2)
                                            else:
                                                if df['SMR_100'][df['ticker'] == 'BIL'].values[0] < df['SMR_100'][df['ticker'] == 'TLT'].values[0]:
                                                    if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.08:
                                                        if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.04:
                                                            alloc_df = df[df['ticker'].isin(['UVXY'])]
                                                        else:
                                                            if df['RSI_200'][df['ticker'] == 'TLT'].values[0] > df['RSI_200'][df['ticker'] == 'IEF'].values[0]:
                                                                alloc_df = df[df['ticker'].isin(['TLT'])]
                                                            else:
                                                                alloc_df1 = df[df['ticker'].isin(['TECL'])]
                                                                alloc_df2 = df[df['ticker'].isin(['TECL', 'SOXL', 'FNGU', 'TLT'])].sort_values(by='RSI_5', ascending=False).head(1)
                                                                alloc_df = pd.concat([alloc_df1, alloc_df2],ignore_index=True, sort=False)
                                                    else:
                                                        if df['RSI_200'][df['ticker'] == 'TLT'].values[0] > df['RSI_200'][df['ticker'] == 'IEF'].values[0]:
                                                            alloc_df = df[df['ticker'].isin(['TLT'])]
                                                        else:
                                                            alloc_df1 = df[df['ticker'].isin(['TECL'])]
                                                            alloc_df2 = df[df['ticker'].isin(['TECL', 'SOXL', 'FNGU', 'TLT'])].sort_values(by='RSI_5',ascending=False).head(1)
                                                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True,sort=False)
                                                else:
                                                    if df['RSI_10'][df['ticker'] == 'IEF'].values[0] > df['RSI_20'][df['ticker'] == 'PSQ'].values[0]:
                                                        alloc_df1 = df[df['ticker'].isin(['FNGU'])]
                                                        alloc_df2 = df[df['ticker'].isin(['FNGU', 'TECL', 'SVXY', 'TLT'])].sort_values(by='RSI_5', ascending=False).head(1)
                                                        alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True,sort=False)
                                                    else:
                                                        if df['close'][df['ticker'] == 'SPY'].values[0] > df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                                                            alloc_df = df[df['ticker'].isin(['SPLV', 'BTAL', 'PDBC', 'UGL'])].sort_values(by='RSI_5',ascending=False).head(2)
                                                        else:
                                                            if df['RSI_60'][df['ticker'] == 'SPY'].values[0] > 50:
                                                                alloc_df1 = df[df['ticker'].isin(['FNGD'])]
                                                                alloc_df2 = df[df['ticker'].isin(['FNGD','TECS','TLT'])].sort_values(by='RSI_5', ascending=False).head(1)
                                                                alloc_df = pd.concat([alloc_df1, alloc_df2],ignore_index=True, sort=False)
                                                            else:
                                                                if df['RSI_200'][df['ticker'] == 'IEF'].values[0] < df['RSI_200'][df['ticker'] == 'TLT'].values[0]:
                                                                    alloc_df1 = df[df['ticker'].isin(['TECS'])]
                                                                    alloc_df2 = df[df['ticker'].isin(['TECS','TMV','SQQQ'])].sort_values(by='RSI_5', ascending=False).head(1)
                                                                    alloc_df = pd.concat([alloc_df1, alloc_df2],ignore_index=True, sort=False)
                                                                else:
                                                                    alloc_df1 = df[df['ticker'].isin(['TECL'])]
                                                                    alloc_df2 = df[df['ticker'].isin(['TECL', 'SVXY', 'FNGU', 'TLT'])].sort_values(by='RSI_5', ascending=False).head(1)
                                                                    alloc_df = pd.concat([alloc_df1, alloc_df2],ignore_index=True, sort=False)

    return alloc_df


















