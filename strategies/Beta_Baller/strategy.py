import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from strategies.Beta_Baller import config as cfg

def get_historical_data():
    sym_list = cfg.sym_list
    hist_period = cfg.period

    stock_historical_data = ed.get_hist_data(sym_list, hist_period)

    return stock_historical_data

def get_technical_data():

    sym_list = cfg.sym_list
    hist_days_list = cfg.hist_days_list
    stock_historical_data = get_historical_data()
    stock_tech_full_data, stock_tech_summ_data = ti.get_technical_data(sym_list, stock_historical_data, hist_days_list)

    return stock_tech_full_data, stock_tech_summ_data


def execute_strategy():

    stock_tech_full_data, stock_tech_summ_data = get_technical_data()

    #stock_tech_full_data.to_csv('stock_tech_full_data.csv')
    # stock_tech_full_data = pd.read_csv('stock_tech_full_data.csv')
    # stock_tech_summ_data = stock_tech_full_data[stock_tech_full_data['date']=='2022-11-15']


    df = stock_tech_summ_data.copy()

    if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 79:
        alloc_df = df[df['ticker'].isin(['UVXY','VIXY'])].sort_values(by='RSI_13', ascending=True).head(1)
    else:
        if df['RSI_10'][df['ticker'] == 'BIL'].values[0] < df['RSI_10'][df['ticker'] == 'TLH'].values[0]:
            if df['RSI_10'][df['ticker'] == 'SOXX'].values[0] < 80:
                alloc_df = df[df['ticker'].isin(['SOXL', 'TYO'])].sort_values(by='MDD_5', ascending=True).head(1)
            else:
                alloc_df = df[df['ticker'].isin(['SOXS'])]
        else:
            if df['RSI_6'][df['ticker'] == 'SPY'].values[0] < 27:
                if df['RSI_7'][df['ticker'] == 'BSV'].values[0] < df['RSI_7'][df['ticker'] == 'SPHB'].values[0]:
                    alloc_df = df[df['ticker'].isin(['SOXS', 'SQQQ'])].sort_values(by='RSI_7', ascending=True).head(1)
                else:
                    alloc_df = df[df['ticker'].isin(['SOXL', 'TECL'])].sort_values(by='RSI_7', ascending=True).head(1)
            else:
                if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
                    alloc_df = df[df['ticker'].isin(['SOXL', 'TECL', 'TQQQ', 'SPXL', 'UPRO', 'SHY'])].sort_values(by='RSI_10', ascending=True).head(1)
                else:
                    if df['SMR_100'][df['ticker'] == 'TLT'].values[0] > df['SMR_100'][df['ticker'] == 'BIL'].values[0]:
                        if df['SMR_20'][df['ticker'] == 'SPTL'].values[0] < 0:
                            if df['EMA_210'][df['ticker'] == 'SPY'].values[0] < df['SMA_360'][df['ticker'] == 'SPY'].values[0]:
                                if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 30:
                                    alloc_df = df[df['ticker'].isin(['SOXL', 'TECL', 'TQQQ', 'UPRO'])].sort_values(by='SMR_5', ascending=True).head(1)
                                else:
                                    if df['SMR_5'][df['ticker'] == 'SH'].values[0] < df['SMR_5'][df['ticker'] == 'TLH'].values[0]:
                                        alloc_df = df[df['ticker'].isin(['SQQQ', 'EUO', 'YCS'])].sort_values(by='CUMR_5', ascending=False).head(1)
                                    else:
                                        alloc_df = df[df['ticker'].isin(['TECL', 'TQQQ', 'SOXL', 'CURE'])].sort_values(by='SMR_5', ascending=True).head(1)
                            else:
                                alloc_df1 = df[df['ticker'].isin(['BTAL', 'UGL'])].sort_values(by='SMR_21',ascending=True).head(1)
                                alloc_df2 = df[df['ticker'].isin(['UUP'])]
                                alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                        else:
                            if df['EMA_210'][df['ticker'] == 'SPY'].values[0] < df['SMA_360'][df['ticker'] == 'SPY'].values[0]:
                                if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 30:
                                    alloc_df = df[df['ticker'].isin(['SOXL', 'TECL', 'TQQQ'])].sort_values(by='SMR_5', ascending=True).head(1)
                                else:
                                    if df['CUMR_2'][df['ticker'] == 'UUP'].values[0] > 0.01:
                                        alloc_df = df[df['ticker'].isin(['TECS', 'SOXS', 'SQQQ'])].sort_values(by='CUMR_5',ascending=False).head(1)
                                    else:
                                        if df['CUMR_1'][df['ticker'] == 'SPY'].values[0] > 0.01:
                                            alloc_df = df[df['ticker'].isin(['ERX', 'EUO', 'YCS'])].sort_values(by='CUMR_5', ascending=False).head(1)
                                        else:
                                            alloc_df = df[df['ticker'].isin(['SOXL', 'EWZ', 'UMDD', 'USD'])].sort_values(by='SMR_5',ascending=True).head(1)
                            else:
                                if df['SMR_210'][df['ticker'] == 'SPY'].values[0] > df['SMR_360'][df['ticker'] == 'DBC'].values[0]:
                                    if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.10:
                                        if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                                            alloc_df = df[df['ticker'].isin(['UYXY'])]
                                        else:
                                            if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                                alloc_df = df[df['ticker'].isin(['SOXL'])]
                                            else:
                                                alloc_df = df[df['ticker'].isin(['UUP', 'EWZ', 'TMF', 'UCO'])].sort_values(by='SMR_5', ascending=False).head(1)
                                    else:
                                        if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['TECL', 'TQQQ', 'SPXL', 'QLD', 'USD'])].sort_values(by='SMR_5', ascending=True).head(1)
                                        else:
                                            alloc_df = df[df['ticker'].isin(['EWZ', 'UUP', 'TMF'])].sort_values(by='CUMR_5', ascending=False).head(1)
                                else:
                                    if df['STDR_20'][df['ticker'] == 'DBC'].values[0] > df['STDR_20'][df['ticker'] == 'SPY'].values[0]:
                                        alloc_df = df[df['ticker'].isin(['SHY', 'EWZ', 'GLD', 'SPXS', 'TECS', 'SOXS'])].sort_values(by='RSI_5', ascending=True).head(1)
                                    else:
                                        if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['SOXL', 'USD', 'TMF'])].sort_values(by='SMR_5',ascending=True).head(1)
                                        else:
                                            alloc_df = df[df['ticker'].isin(['EWZ', 'SPXS', 'SOXS', 'UCO', 'YCS'])].sort_values(by='CUMR_5',ascending=False).head(1)
                    else:
                        if df['SMR_20'][df['ticker'] == 'SPTL'].values[0] < 0:
                            if df['EMA_210'][df['ticker'] == 'SPY'].values[0] < df['SMA_360'][df['ticker'] == 'SPY'].values[0]:
                                if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 30:
                                    alloc_df = df[df['ticker'].isin(['SOXL', 'TQQQ', 'UPRO'])].sort_values(by='SMR_5', ascending=False).head(1)
                                else:
                                    if df['CUMR_2'][df['ticker'] == 'UUP'].values[0] > 0.01:
                                        alloc_df = df[df['ticker'].isin(['TECS', 'SOXS', 'SQQQ', 'SPXS', 'ERX'])].sort_values(by='CUMR_5',ascending=True).head(1)
                                    else:
                                        if df['SMR_5'][df['ticker'] == 'SH'].values[0] > df['SMR_5'][df['ticker'] == 'STIP'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['SOXS', 'SQQQ', 'EPI', 'TMV'])].sort_values(by='CUMR_5', ascending=False).head(1)
                                        else:
                                            if df['SMR_5'][df['ticker'] == 'TMF'].values[0] > 0.0:
                                                alloc_df = df[df['ticker'].isin(['TECL', 'SOXL', 'TNA'])].sort_values(by='SMR_5', ascending=True).head(1)
                                            else:
                                                alloc_df = df[df['ticker'].isin(['TECL', 'SOXL', 'TMV', 'TQQQ'])].sort_values( by='SMR_3', ascending=True).head(1)
                            else:
                                if df['SMR_210'][df['ticker'] == 'SPY'].values[0] > df['SMR_360'][df['ticker'] == 'DBC'].values[0]:
                                    if df['RSI_11'][df['ticker'] == 'TQQQ'].values[0] > 77:
                                        alloc_df = df[df['ticker'].isin(['UVXY', 'SQQQ'])]
                                    else:
                                        if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.10:
                                            if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                                                alloc_df = df[df['ticker'].isin(['UYXY'])]
                                            else:
                                                alloc_df = df[df['ticker'].isin(['SOXL', 'TMV'])].sort_values(by='SMR_5', ascending=True).head(1)
                                        else:
                                            if df['SMR_5'][df['ticker'] == 'SH'].values[0] < df['SMR_5'][df['ticker'] == 'STIP'].values[0]:
                                                alloc_df = df[df['ticker'].isin(['TQQQ', 'SOXL', 'TNA', 'UPRO', 'TMV', 'TECL'])].sort_values(by='SMR_5', ascending=False).head(2)
                                            else:
                                                alloc_df = df[df['ticker'].isin(['BTAL', 'UGL'])].sort_values(by='SMR_21', ascending=True).head(1)
                                else:
                                    if df['STDR_20'][df['ticker'] == 'DBC'].values[0] > df['STDR_20'][df['ticker'] == 'SPY'].values[0]:
                                        if df['STDR_10'][df['ticker'] == 'DBC'].values[0] > 0.03:
                                            if df['STDR_5'][df['ticker'] == 'TMV'].values[0] < df['STDR_5'][df['ticker'] == 'DBC'].values[0]:
                                                alloc_df = df[df['ticker'].isin(['TMV'])]
                                            else:
                                                alloc_df = df[df['ticker'].isin(['DBC'])]
                                        else:
                                            if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                                alloc_df = df[df['ticker'].isin(['TMV', 'SOXS', 'SPXU'])].sort_values(by='SMR_5', ascending=False).head(1)
                                            else:
                                                alloc_df = df[df['ticker'].isin(['EFA', 'EEM', 'SPXS', 'SOXS', 'UCO', 'TMV'])].sort_values(by='CUMR_5', ascending=True).head(1)
                                    else:
                                        if df['RSI_7'][df['ticker'] == 'BIL'].values[0] < df['RSI_7'][df['ticker'] == 'IEF'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['EPI', 'SOXL', 'UPRO'])].sort_values(by='SMR_5', ascending=True).head(1)
                                        else:
                                            alloc_df = df[df['ticker'].isin(['EWZ', 'TECS', 'SOXS', 'EUO', 'YCS', 'TMV'])].sort_values(by='CUMR_5', ascending=False).head(1)
                        else:
                            if df['EMA_210'][df['ticker'] == 'SPY'].values[0] < df['SMA_360'][df['ticker'] == 'SPY'].values[0]:
                                if df['CUMR_1'][df['ticker'] == 'SPY'].values[0] < -0.02:
                                    alloc_df = df[df['ticker'].isin(['SPXS', 'TECS', 'SOXS', 'SQQQ'])].sort_values(by='CUMR_5', ascending=False).head(1)
                                else:
                                    if df['SMR_10'][df['ticker'] == 'IEF'].values[0] < df['SMR_10'][df['ticker'] == 'SH'].values[0]:
                                        alloc_df = df[df['ticker'].isin(['TMF', 'TYO', 'SPXS', 'SQQQ'])].sort_values(by='CUMR_10', ascending=False).head(1)
                                    else:
                                        alloc_df = df[df['ticker'].isin(['TECL', 'TQQQ', 'SOXL', 'BRZU', 'TMF'])].sort_values(by='SMR_5', ascending=True).head(1)
                            else:
                                if df['SMR_210'][df['ticker'] == 'SPY'].values[0] > df['SMR_360'][df['ticker'] == 'DBC'].values[0]:
                                    if df['EMA_210'][df['ticker'] == 'SPY'].values[0] > df['EMA_360'][df['ticker'] == 'SPY'].values[0]:
                                        if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.10:
                                            if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                                                alloc_df = df[df['ticker'].isin(['UYXY'])]
                                            else:
                                                alloc_df = df[df['ticker'].isin(
                                                    ['TQQQ','SPXL', 'SOXL', 'EPI', 'UPRO', 'QLD', 'TECL', 'EWZ', 'UMDD', 'PUI', 'USD', 'TMF'])].sort_values(by='SMR_1',ascending=True).head(1)
                                        else:
                                            if df['SMR_10'][df['ticker'] == 'IEF'].values[0] > df['SMR_10'][df['ticker'] == 'SH'].values[0]:
                                                alloc_df1 = df[df['ticker'].isin(['TECL', 'SPXL', 'EPI', 'SOXL', 'UPRO', 'UMDD'])].sort_values(by='SMR_5',ascending=True).head(1)
                                                alloc_df2 = df[df['ticker'].isin(['TMF'])]
                                                alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                                            else:
                                                alloc_df1 = df[df['ticker'].isin(['SOXS', 'TMF'])].sort_values(by='CUMR_5', ascending=False).head(1)
                                                alloc_df2 = df[df['ticker'].isin(['BTAL', 'UGL'])].sort_values(by='SMR_21', ascending=True).head(1)
                                                alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                                    else:
                                        alloc_df = df[df['ticker'].isin(['SHY'])]
                                else:
                                    if df['STDR_20'][df['ticker'] == 'DBC'].values[0] > df['STDR_20'][df['ticker'] == 'SPY'].values[0]:
                                        alloc_df = df[df['ticker'].isin(['SPXS', 'EPI', 'TECS', 'SOXS', 'SQQQ'])].sort_values(by='RSI_5', ascending=True).head(1)
                                    else:
                                        alloc_df = df[df['ticker'].isin(['TECL', 'TQQQ', 'SOXL', 'TMF'])].sort_values(by='SMR_5', ascending=False).head(1)

    alloc_df['pct_alloc'] = (1 / alloc_df['ticker'].count() * 100).round(0)

    alloc_df['strategy_name'] = cfg.strategy_name
    curr_alloc_df = alloc_df[['strategy_name', 'date', 'ticker', 'close', 'PCTRET', 'pct_alloc']]
    curr_alloc_df['close'] = curr_alloc_df['close'].round(2)
    curr_alloc_df['PCTRET'] = (curr_alloc_df['PCTRET'] * 100).round(4)
    curr_alloc_df = curr_alloc_df.rename(columns={'PCTRET': 'pctreturn'})
    curr_alloc_df['date'] = pd.to_datetime(curr_alloc_df['date']).dt.strftime('%m/%d/%Y')
    curr_alloc_df = (curr_alloc_df.groupby(['strategy_name', 'date', 'ticker', 'close', 'pctreturn']).agg({'pct_alloc': 'sum'}).reset_index())

    return curr_alloc_df