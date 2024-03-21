import pandas as pd

df = pd.DataFrame()

def beta_baller_cleaned_up(df):

    if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 79:
        alloc_df = df[df['ticker'].isin(['UVXY'])]

    else:
        if df['RSI_6'][df['ticker'] == 'SPY'].values[0] < 27:
            if df['RSI_7'][df['ticker'] == 'BSV'].values[0] < df['RSI_7'][df['ticker'] == 'SPHB'].values[0]:
                alloc_df = df[df['ticker'].isin(['BTAL'])]
            else:
                alloc_df = df[df['ticker'].isin(['SOXL', 'TQQQ', 'FNGU'])].sort_values(by='RSI_10', ascending=True).head(1)
        else:
            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
                alloc_df = df[df['ticker'].isin(['SOXL','TQQQ','UPRO'])].sort_values(by='RSI_10', ascending=True).head(1)
            else:
                if df['SMR_100'][df['ticker'] == 'TLT'].values[0] > df['SMR_100'][df['ticker'] == 'BIL'].values[0]:
                    if df['SMR_20'][df['ticker'] == 'SPTL'].values[0] < 0:
                        ## A.B.B.A: Risk Off, Rising Rates ##
                        if df['EMA_210'][df['ticker'] == 'SPY'].values[0] < df['SMA_360'][df['ticker'] == 'SPY'].values[0]:
                            if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 30:
                                alloc_df = df[df['ticker'].isin(['SOXL','FNGU','TQQQ'])].sort_values(by='RSI_10', ascending=True).head(1)
                            else:
                                if df['SMR_5'][df['ticker'] == 'SH'].values[0] < df['SMR_5'][df['ticker'] == 'TLH'].values[0]:
                                    alloc_df = df[df['ticker'].isin(['BTAL'])]
                                else:
                                    alloc_df = df[df['ticker'].isin(['TMV', 'TQQQ', 'SOXL'])].sort_values(by='SMR_10', ascending=True).head(1)
                        else:
                            alloc_df1 = df[df['ticker'].isin(['TMV', 'TQQQ', 'SOXL'])].sort_values(by='SMR_5',ascending=True).head(1)
                            alloc_df2 = df[df['ticker'].isin(['UUP'])]
                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                    ## A.B.B.B: Risk Off, Falling Rates##
                    else:
                        if df['EMA_210'][df['ticker'] == 'SPY'].values[0] < df['SMA_360'][df['ticker'] == 'SPY'].values[0]:
                            if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 30:
                                alloc_df = df[df['ticker'].isin(['SOXL','FNGU','TQQQ'])].sort_values(by='CUMR_10',ascending=True).head(1)
                            else:
                                if df['CUMR_1'][df['ticker'] == 'SPY'].values[0] > 0.01:
                                    alloc_df = df[df['ticker'].isin(['BTAL'])]
                                else:
                                    alloc_df = df[df['ticker'].isin(['TQQQ','SOXL','EEM','TMF'])].sort_values(by='CUMR_5',ascending=False).head(1)
                        else:
                            if df['SMR_210'][df['ticker'] == 'SPY'].values[0] > \
                                    df['SMR_360'][df['ticker'] == 'DBC'].values[0]:
                                if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.10:
                                    if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                                        alloc_df = df[df['ticker'].isin(['VIXY'])]
                                    else:
                                        if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < \
                                                df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['SOXL'])]
                                        else:
                                            alloc_df = df[df['ticker'].isin(['TQQQ','SOXL','EEM','TMF'])].sort_values(
                                                by='SMR_5', ascending=False).head(1)
                                else:
                                    if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < \
                                            df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                        alloc_df = df[
                                            df['ticker'].isin(['TQQQ','SOXL','EEM','TMF'])].sort_values(
                                            by='SMR_5', ascending=True).head(1)
                                    else:
                                        alloc_df = df[df['ticker'].isin(['USDU', 'EEM', 'TMF'])].sort_values(by='CUMR_10',ascending=False).head(1)
                            else:
                                if df['STDR_20'][df['ticker'] == 'DBC'].values[0] > \
                                        df['STDR_20'][df['ticker'] == 'SPY'].values[0]:
                                    alloc_df = df[
                                        df['ticker'].isin(['BTAL'])]
                                else:
                                    if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < \
                                            df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                        alloc_df = df[df['ticker'].isin(['SOXL', 'TQQQ', 'TMF'])].sort_values(by='SMR_5',ascending=True).head(1)
                                    else:
                                        alloc_df = df[df['ticker'].isin(['BTAL'])]
                else:
                    if df['SMR_20'][df['ticker'] == 'SPTL'].values[0] < 0:
                        ### B.A.A: Risk Off, Rising Rates ###
                        if df['EMA_210'][df['ticker'] == 'SPY'].values[0] < df['SMA_360'][df['ticker'] == 'SPY'].values[0]:
                            if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 30:
                                alloc_df = df[df['ticker'].isin(['SOXL', 'TQQQ', 'FNGU'])].sort_values(by='SMR_5',ascending=False).head(1)
                            else:
                                if df['CUMR_2'][df['ticker'] == 'UUP'].values[0] > 0.01:
                                    alloc_df = df[df['ticker'].isin(['BTAL'])]
                                else:
                                    if df['SMR_5'][df['ticker'] == 'SH'].values[0] > \
                                            df['SMR_5'][df['ticker'] == 'STIP'].values[0]:
                                        alloc_df = df[df['ticker'].isin(['BTAL'])]
                                    else:
                                        alloc_df = df[df['ticker'].isin(['FNGU', 'SOXL', 'TMV', 'TQQQ'])].sort_values(by='CUMR_5', ascending=True).head(1)
                        else:
                            if df['SMR_210'][df['ticker'] == 'SPY'].values[0] > \
                                    df['SMR_360'][df['ticker'] == 'DBC'].values[0]:
                                if df['RSI_11'][df['ticker'] == 'TQQQ'].values[0] > 77:
                                    alloc_df = df[df['ticker'].isin(['BTAL'])]
                                else:
                                    if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.10:
                                        if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                                            alloc_df = df[df['ticker'].isin(['VIXY'])]
                                        else:
                                            alloc_df = df[df['ticker'].isin(['FNGU','SOXL','TMV','TQQQ'])].sort_values(by='CUMR_5',ascending=True).head(1)
                                    else:
                                        if df['SMR_5'][df['ticker'] == 'SH'].values[0] < \
                                                df['SMR_5'][df['ticker'] == 'STIP'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['TQQQ', 'SOXL', 'FNGU'])].sort_values(by='CUMR_5', ascending=False).head(1)
                                        else:
                                            alloc_df = df[df['ticker'].isin(['BTAL'])].sort_values(by='SMR_21', ascending=True).head(1)
                            else:
                                if df['STDR_20'][df['ticker'] == 'DBC'].values[0] > \
                                        df['STDR_20'][df['ticker'] == 'SPY'].values[0]:
                                    if df['STDR_10'][df['ticker'] == 'DBC'].values[0] > 0.03:
                                        if df['STDR_5'][df['ticker'] == 'TMV'].values[0] < \
                                                df['STDR_5'][df['ticker'] == 'DBC'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['TMV'])]
                                        else:
                                            alloc_df = df[df['ticker'].isin(['BTAL'])]
                                    else:
                                        if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < \
                                                df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['BTAL','TMV'])].sort_values(by='CUMR_5', ascending=False).head(1)
                                        else:
                                            alloc_df = df[df['ticker'].isin(['BTAL'])]
                                else:
                                    if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < \
                                            df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                        alloc_df = df[df['ticker'].isin(['TQQQ','SOXL','FNGU','EEM'])].sort_values(by='CUMR_5', ascending=True).head(1)
                                    else:
                                        alloc_df = df[df['ticker'].isin(['BTAL'])]
                    ### B.A.B: Risk Off, Falling Rates ###
                    else:
                        if df['EMA_210'][df['ticker'] == 'SPY'].values[0] < df['SMA_360'][df['ticker'] == 'SPY'].values[0]:
                            if df['CUMR_1'][df['ticker'] == 'SPY'].values[0] < -0.02:
                                alloc_df = df[df['ticker'].isin(['SPXS', 'TECS', 'SOXS', 'SQQQ'])].sort_values(by='CUMR_5', ascending=False).head(1)
                            else:
                                if df['SMR_10'][df['ticker'] == 'IEF'].values[0] < \
                                        df['SMR_10'][df['ticker'] == 'SH'].values[0]:
                                    alloc_df = df[df['ticker'].isin(['TMF','IEF','BTAL'])].sort_values(by='CUMR_10', ascending=False).head(1)
                                else:
                                    alloc_df = df[
                                        df['ticker'].isin(['TECL', 'TQQQ', 'SOXL', 'EEM', 'TMF'])].sort_values(by='CUMR_5', ascending=True).head(1)
                        else:
                            if df['SMR_210'][df['ticker'] == 'SPY'].values[0] > df['SMR_360'][df['ticker'] == 'DBC'].values[0]:
                                if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.10:
                                    if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                                        alloc_df = df[df['ticker'].isin(['VIXY'])]
                                    else:
                                        alloc_df = df[df['ticker'].isin(['TQQQ','FNGU','EEM','SOXL','TMF'])].sort_values(by='CUMR_5', ascending=True).head(1)
                                else:
                                    if df['SMR_10'][df['ticker'] == 'IEF'].values[0] > df['SMR_10'][df['ticker'] == 'SH'].values[0]:
                                        alloc_df1 = df[df['ticker'].isin(['TQQQ','FNGU','EEM','SOXL','TMF'])].sort_values(by='SMR_5', ascending=True).head(1)
                                        alloc_df2 = df[df['ticker'].isin(['TMF'])]
                                        alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                                    else:
                                        alloc_df1 = df[df['ticker'].isin(['BTAL'])]
                            else:
                                if df['STDR_20'][df['ticker'] == 'DBC'].values[0] > df['STDR_20'][df['ticker'] == 'SPY'].values[0]:
                                    alloc_df = df[df['ticker'].isin(['SPXS', 'EPI', 'TECS', 'SOXS', 'SQQQ'])].sort_values(by='RSI_5', ascending=True).head(1)
                                else:
                                    alloc_df = df[df['ticker'].isin(['TECL', 'TQQQ', 'SOXL', 'TMF'])].sort_values(by='SMR_5', ascending=False).head(1)

    return alloc_df