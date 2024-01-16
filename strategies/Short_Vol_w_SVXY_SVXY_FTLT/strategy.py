import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from strategies.Short_Vol_w_SVXY_SVXY_FTLT import config as cfg

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

    if df['RSI_10'][df['ticker'] == 'VIXY'].values[0] > 70:
        if df['CUMR_1'][df['ticker'] == 'SPY'].values[0] < -0.05:
            alloc_df = df[df['ticker'] == 'SVXY']
        else:
            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 15:
                alloc_df = df[df['ticker'] == 'SVXY']
            else:
                if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 15:
                    alloc_df = df[df['ticker'] == 'SVXY']
                else:
                    if df['CUMR_1'][df['ticker'] == 'SPY'].values[0] > 0.025:
                        alloc_df = df[df['ticker'] == 'UVXY']
                    else:
                        if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 80:
                            alloc_df = df[df['ticker'] == 'VIXY']
                        else:
                            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
                                alloc_df = df[df['ticker'] == 'VIXY']
                            else:
                                if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
                                    alloc_df = df[df['ticker'] == 'XLK']
                                else:
                                    if df['close'][df['ticker'] == 'SVXY'].values[0] > df['SMA_21'][df['ticker'] == 'SVXY'].values[0]:
                                        alloc_df = df[df['ticker'].isin(['SVXY', 'SPY'])].sort_values(by='SMR' + '_' + '20', ascending=False).head(1)
                                    else:
                                        alloc_df = df[df['ticker'] == 'SHV']

    else:
        if df['RSI_14'][df['ticker'] == 'SPY'].values[0] < 30:
            alloc_df = df[df['ticker'] == 'SVXY']
        else:
            if df['RSI_14'][df['ticker'] == 'QQQ'].values[0] < 30:
                alloc_df = df[df['ticker'] == 'SVXY']
            else:
                if df['CUMR_1'][df['ticker'] == 'SPY'].values[0] < -0.03:
                    alloc_df = df[df['ticker'] == 'SVXY']
                else:
                    if df['CUMR_5'][df['ticker'] == 'SPY'].values[0] < -0.10:
                        alloc_df = df[df['ticker'] == 'SVXY']
                    else:
                        if df['RSI_14'][df['ticker'] == 'SPY'].values[0] > 65:
                            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
                                alloc_df = df[df['ticker'] == 'UVXY']
                            else:
                                if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 80:
                                    alloc_df = df[df['ticker'] == 'VIXY']
                                else:
                                    if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
                                        alloc_df = df[df['ticker'] == 'XLK']
                                    else:
                                        if df['close'][df['ticker'] == 'SVXY'].values[0] > \
                                                df['SMA_21'][df['ticker'] == 'SVXY'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['SVXY', 'SPY'])].sort_values(
                                                by='SMR' + '_' + '20', ascending=False).head(1)
                                        else:
                                            alloc_df = df[df['ticker'] == 'SHV']
                        else:
                            if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 80:
                                alloc_df = df[df['ticker'] == 'VIXY']
                            else:
                                if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
                                    alloc_df = df[df['ticker'] == 'VIXY']
                                else:
                                    if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
                                        alloc_df = df[df['ticker'] == 'XLK']
                                    else:
                                        if df['close'][df['ticker'] == 'SVXY'].values[0] > \
                                                df['SMA_21'][df['ticker'] == 'SVXY'].values[0]:
                                            alloc_df = df[df['ticker'].isin(['SVXY', 'SPY'])].sort_values(
                                                by='SMR' + '_' + '20', ascending=False).head(1)
                                        else:
                                            alloc_df = df[df['ticker'] == 'SHV']

    alloc_df['strategy_name'] = cfg.strategy_name
    curr_alloc_df = alloc_df[['strategy_name','date','ticker','close','PCTRET']]
    curr_alloc_df['close'] = curr_alloc_df['close'].round(2)
    curr_alloc_df['PCTRET'] = (curr_alloc_df['PCTRET'] * 100).round(4)
    curr_alloc_df = curr_alloc_df.rename(columns={'PCTRET': 'pctreturn'})
    curr_alloc_df['date'] = pd.to_datetime(curr_alloc_df['date']).dt.strftime('%m/%d/%Y')

    return curr_alloc_df