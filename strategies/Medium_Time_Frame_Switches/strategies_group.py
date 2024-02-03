import pandas as pd

### 60 Day RSI Strategy ###

df = pd.DataFrame()

def dia_rsi(df):

    if df['RSI_60'][df['ticker'] == 'DIA'].values[0] > 50:
        if df['RSI_10'][df['ticker'] == 'DIA'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['UDOW'])]
        else:
            if df['RSI_10'][df['ticker'] == 'DIA'].values[0] > 80:
                alloc_df = df[df['ticker'].isin(['VIXY'])]
            else:
                if df['CUMR_10'][df['ticker'] == 'DIA'].values[0] > 0:
                    alloc_df = df[df['ticker'].isin(['DIA', 'UDOW'])].sort_values(by='RSI_10',ascending=False).head(1)
                else:
                    alloc_df = df[df['ticker'].isin(['DIA'])]
    else:
        if df['RSI_10'][df['ticker'] == 'DIA'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['UDOW'])]
        else:
            if df['CUMR_6'][df['ticker'] == 'UDOW'].values[0] < -0.12:
                if df['CUMR_1'][df['ticker'] == 'UDOW'].values[0] > 0.045:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]
            else:
                if df['close'][df['ticker'] == 'DIA'].values[0] > df['SMA_20'][df['ticker'] == 'DIA'].values[0]:
                    alloc_df = df[df['ticker'].isin(['UDOW'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]

    return alloc_df



def spy_rsi(df):

    if df['RSI_60'][df['ticker'] == 'SPY'].values[0] > 50:
        if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['UPRO'])]
        else:
            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
                alloc_df = df[df['ticker'].isin(['VIXY'])]
            else:
                if df['CUMR_10'][df['ticker'] == 'SPY'].values[0] > 0:
                    alloc_df = df[df['ticker'].isin(['SPY', 'UPRO'])].sort_values(by='RSI_10',ascending=False).head(1)
                else:
                    alloc_df = df[df['ticker'].isin(['SPY'])]
    else:
        if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['UPRO'])]
        else:
            if df['CUMR_6'][df['ticker'] == 'UPRO'].values[0] < -0.12:
                if df['CUMR_1'][df['ticker'] == 'UPRO'].values[0] > 0.045:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]
            else:
                if df['close'][df['ticker'] == 'SPY'].values[0] > df['SMA_20'][df['ticker'] == 'SPY'].values[0]:
                    alloc_df = df[df['ticker'].isin(['UPRO'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]

    return alloc_df


def qqq_rsi(df):

    if df['RSI_60'][df['ticker'] == 'QQQ'].values[0] > 50:
        if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['TQQQ'])]
        else:
            if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 80:
                alloc_df = df[df['ticker'].isin(['VIXY'])]
            else:
                if df['CUMR_10'][df['ticker'] == 'QQQ'].values[0] > 0:
                    alloc_df = df[df['ticker'].isin(['QQQ', 'TQQQ'])].sort_values(by='RSI_10',ascending=False).head(1)
                else:
                    alloc_df = df[df['ticker'].isin(['QQQ'])]
    else:
        if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['TQQQ'])]
        else:
            if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.13:
                if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]
            else:
                if df['close'][df['ticker'] == 'QQQ'].values[0] > df['SMA_20'][df['ticker'] == 'QQQ'].values[0]:
                    alloc_df = df[df['ticker'].isin(['TQQQ'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]

    return alloc_df


def xlk_rsi(df):

    if df['RSI_60'][df['ticker'] == 'XLK'].values[0] > 50:
        if df['RSI_10'][df['ticker'] == 'XLK'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['TECL'])]
        else:
            if df['RSI_10'][df['ticker'] == 'XLK'].values[0] > 80:
                alloc_df = df[df['ticker'].isin(['VIXY'])]
            else:
                if df['CUMR_10'][df['ticker'] == 'XLK'].values[0] > 0:
                    alloc_df = df[df['ticker'].isin(['XLK', 'TECL'])].sort_values(by='RSI_10',ascending=False).head(1)
                else:
                    alloc_df = df[df['ticker'].isin(['XLK'])]
    else:
        if df['RSI_10'][df['ticker'] == 'XLK'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['TECL'])]
        else:
            if df['CUMR_6'][df['ticker'] == 'TECL'].values[0] < -0.135:
                if df['CUMR_1'][df['ticker'] == 'TECL'].values[0] > 0.045:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]
            else:
                if df['close'][df['ticker'] == 'XLK'].values[0] > df['SMA_20'][df['ticker'] == 'XLK'].values[0]:
                    alloc_df = df[df['ticker'].isin(['TECL'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]

    return alloc_df


def soxx_rsi(df):

    if df['RSI_60'][df['ticker'] == 'SOXX'].values[0] > 50:
        if df['RSI_10'][df['ticker'] == 'SOXX'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['SOXL'])]
        else:
            if df['RSI_10'][df['ticker'] == 'SOXX'].values[0] > 80:
                alloc_df = df[df['ticker'].isin(['VIXY'])]
            else:
                if df['CUMR_10'][df['ticker'] == 'SOXX'].values[0] > 0:
                    alloc_df = df[df['ticker'].isin(['SOXX', 'SOXL'])].sort_values(by='RSI_10',ascending=False).head(1)
                else:
                    alloc_df = df[df['ticker'].isin(['SOXX'])]
    else:
        if df['RSI_10'][df['ticker'] == 'SOXX'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['SOXL'])]
        else:
            if df['CUMR_6'][df['ticker'] == 'SOXL'].values[0] < -0.135:
                if df['CUMR_1'][df['ticker'] == 'SOXL'].values[0] > 0.045:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]
            else:
                if df['close'][df['ticker'] == 'SOXX'].values[0] > df['SMA_20'][df['ticker'] == 'SOXX'].values[0]:
                    alloc_df = df[df['ticker'].isin(['SOXL'])]
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]

    return alloc_df

### 20 Day BND Vs 60 Day SH

def bnd20_sh60(df):
    if df['RSI_20'][df['ticker'] == 'BND'].values[0] > df['RSI_60'][df['ticker'] == 'SH'].values[0]:
        if df['close'][df['ticker'] == 'SPY'].values[0] > df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
            alloc_df = df[df['ticker'].isin(['TQQQ'])]
        else:
            if df['close'][df['ticker'] == 'TQQQ'].values[0] > df['SMA_20'][df['ticker'] == 'TQQQ'].values[0]:
                if df['RSI_10'][df['ticker'] == 'PSQ'].values[0] < 30:
                    alloc_df = df[df['ticker'].isin(['PSQ'])]
                else:
                    alloc_df = df[df['ticker'].isin(['TQQQ'])]
            else:
                alloc_df = df[df['ticker'].isin(['BIL'])]
    else:
        alloc_df = df[df['ticker'].isin(['BIL'])]

    return alloc_df

def bnd20_sh60_v1(df):
    if df['RSI_60'][df['ticker'] == 'SPY'].values[0] > 61:
        alloc_df = df[df['ticker'].isin(['VIXY', 'BIL'])]
    else:
        if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 81:
            alloc_df = df[df['ticker'].isin(['VIXY', 'BIL'])]
        else:
            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
                alloc_df = df[df['ticker'].isin(['VIXY', 'BIL'])]
            else:
                if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 32:
                    alloc_df = df[df['ticker'].isin(['TECL'])]
                else:
                    if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
                        alloc_df = df[df['ticker'].isin(['UPRO'])]
                    else:
                        if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.105:
                            if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                                alloc_df = df[df['ticker'].isin(['VIXY', 'BIL'])]
                            else:
                                alloc_df = bnd20_sh60(df)
                        else:
                            alloc_df = bnd20_sh60(df)

    return alloc_df

### 60 Day BND vs BIL ###
def bnd60_bil(df):
    if df['CUMR_60'][df['ticker'] == 'BND'].values[0] > df['CUMR_60'][df['ticker'] == 'BIL'].values[0]:
        if df['close'][df['ticker'] == 'SPY'].values[0] > df['SMA_100'][df['ticker'] == 'SPY'].values[0]:
            alloc_df = df[df['ticker'].isin(['UPRO'])]
        else:
            if df['close'][df['ticker'] == 'UPRO'].values[0] > df['SMA_20'][df['ticker'] == 'UPRO'].values[0]:
                if df['RSI_10'][df['ticker'] == 'SH'].values[0] < 30:
                    alloc_df = df[df['ticker'].isin(['VIXY'])]
                else:
                    alloc_df = df[df['ticker'].isin(['UPRO'])]
            else:
                alloc_df = df[df['ticker'].isin(['BTAL'])]
    else:
        alloc_df = df[df['ticker'].isin(['BTAL'])]

    return alloc_df

def bnd60_bil_v1(df):
    if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 79:
        alloc_df = df[df['ticker'].isin(['VIXY', 'BIL'])]
    else:
        if df['RSI_60'][df['ticker'] == 'SPY'].values[0] > 60:
            alloc_df = df[df['ticker'].isin(['VIXY', 'BIL'])]
        else:
            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
                alloc_df = df[df['ticker'].isin(['UPRO'])]
            else:
                if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
                    alloc_df = df[df['ticker'].isin(['TQQQ'])]
                else:
                    if df['CUMR_6'][df['ticker'] == 'UPRO'].values[0] < -0.105:
                        if df['CUMR_1'][df['ticker'] == 'UPRO'].values[0] > 0.05:
                            alloc_df = df[df['ticker'].isin(['SDS'])]
                        else:
                            alloc_df = bnd60_bil(df)
                    else:
                        alloc_df = bnd60_bil(df)
    return alloc_df

### V1 BWC: Sub-Zero RSI MA Crossover (BT June 2 2015) Spicy Edition incl. UVXY & Extreme Beta ###
def rsi_crossover(df):
    if df['CUMR_10'][df['ticker'] == 'SH'].values[0] > 0:
        if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['TECL', 'SOXL', 'UPRO', 'TQQQ'])].sort_values(by='RSI' + '_' + '10', ascending=True).head(2)
        else:
            if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
                alloc_df = df[df['ticker'].isin(['TECL', 'SOXL', 'UPRO', 'TQQQ'])].sort_values(by='RSI' + '_' + '10', ascending=True).head(2)
            else:
                if df['close'][df['ticker'] == 'SPY'].values[0] < df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                    alloc_df = df[df['ticker'].isin(['BTAL', 'SDS', 'SH', 'BIL'])].sort_values(by='CUMR_5', ascending=False).head(2)
                else:
                    alloc_df = df[df['ticker'].isin(['BTAL'])]
    else:
        if df['RSI_30'][df['ticker'] == 'SPY'].values[0] > df['RSI_45'][df['ticker'] == 'SPY'].values[0]:
            if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 80:
                alloc_df = df[df['ticker'].isin(['UVXY'])]
            else:
                if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    if df['RSI_10'][df['ticker'] == 'SOXX'].values[0] > 80:
                        alloc_df = df[df['ticker'].isin(['SOXS'])]
                    else:
                        if df['RSI_10'][df['ticker'] == 'TECL'].values[0] > 80:
                            alloc_df = df[df['ticker'].isin(['TECS'])]
                        else:
                            if df['RSI_10'][df['ticker'] == 'USO'].values[0] > 85:
                                alloc_df = df[df['ticker'].isin(['DRIP'])]
                            else:
                                if df['RSI_10'][df['ticker'] == 'TLT'].values[0] > df['RSI_10'][df['ticker'] == 'SPY'].values[0]:
                                    alloc_df = df[df['ticker'].isin(['BND', 'AGG', 'TBX', 'SHV', 'TLT', 'IEF', 'BIL', 'BTAL', 'SHV'])].\
                                        sort_values(by='SMR_10', ascending=False).head(2)
                                else:
                                    alloc_df1 = df[df['ticker'].isin(
                                        ['DBC', 'UPRO', 'TQQQ', 'SVXY', 'BTAL', 'SH'])]. \
                                        sort_values(by='CUMR_20', ascending=False).head(2)
                                    alloc_df2 = df[df['ticker'].isin(
                                        ['DBC', 'UPRO', 'TQQQ', 'SVXY', 'BTAL', 'SH'])]. \
                                        sort_values(by='MDD_10', ascending=True).head(2)
                                    alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
        else:
            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
                alloc_df = df[df['ticker'].isin(['TECL', 'SOXL', 'UPRO', 'TQQQ'])].sort_values(by='RSI' + '_' + '10', ascending=True).head(2)
            else:
                if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
                    alloc_df = df[df['ticker'].isin(['TECL', 'SOXL', 'UPRO', 'TQQQ'])].sort_values(by='RSI' + '_' + '10', ascending=True).head(2)
                else:
                    if df['close'][df['ticker'] == 'SPY'].values[0] < df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                        alloc_df = df[df['ticker'].isin(['BTAL', 'SDS', 'SH', 'BIL'])].sort_values(by='CUMR_5',ascending=False).head(2)
                    else:
                        alloc_df = df[df['ticker'].isin(['BTAL'])]

    return alloc_df