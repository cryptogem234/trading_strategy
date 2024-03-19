import pandas as pd

def volmageddon(df):
    ### Volmageddon 2.0 ###
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
                            alloc_df = df[df['ticker'].isin(['TECL', 'SVXY'])]
                    else:
                        if df['STDR_10'][df['ticker'] == 'UVXY'].values[0] > 0.10:
                            if df['RSI_10'][df['ticker'] == 'UVXY'].values[0] > 70:
                                alloc_df = df[df['ticker'].isin(['UVXY', 'VIXY'])].sort_values(by='SMR_5',
                                                                                               ascending=False).head(1)
                            else:
                                alloc_df = df[df['ticker'].isin(['VTI', 'BIL'])].sort_values(by='SMR_14',
                                                                                             ascending=False).head(1)
                        else:
                            alloc_df = df[df['ticker'].isin(['SPXU', 'SVXY'])]

    return alloc_df