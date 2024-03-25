import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from datetime import datetime, timedelta
from strategies.Simple_20d_BND_vs_60d_SH import config as cfg

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
    df = stock_tech_summ_data

    if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 81:
        alloc_df = df[df['ticker'].isin(['VXX'])]
    else:
        if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
            alloc_df = df[df['ticker'].isin(['VXX'])]
        else:
            if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 32:
                alloc_df = df[df['ticker'].isin(['TECL'])]
            else:
                if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
                    alloc_df = df[df['ticker'].isin(['UPRO'])]
                else:
                    if df['RSI_60'][df['ticker'] == 'SPY'].values[0] > 61:
                        alloc_df = df[df['ticker'].isin(['SPY'])]
                    else:
                        if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.105:
                            if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                                alloc_df = df[df['ticker'].isin(['VXX'])]
                            else:
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
                        else:
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


    alloc_df['strategy_name'] = cfg.strategy_name
    curr_alloc_df = alloc_df[['strategy_name','date','ticker','close','PCTRET']]
    curr_alloc_df['close'] = curr_alloc_df['close'].round(2)
    curr_alloc_df['PCTRET'] = (curr_alloc_df['PCTRET'] * 100).round(4)
    curr_alloc_df = curr_alloc_df.rename(columns={'PCTRET': 'pctreturn'})
    curr_alloc_df['date'] = pd.to_datetime(curr_alloc_df['date']).dt.strftime('%m/%d/%Y')

    curr_alloc_df['pct_alloc'] = (1 / curr_alloc_df['ticker'].count() * 100).round(0)

    curr_alloc_df = (curr_alloc_df.groupby(['strategy_name', 'date', 'ticker', 'close', 'pctreturn']).agg({'pct_alloc': 'sum'}).reset_index())

    return curr_alloc_df
















