import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from datetime import datetime, timedelta

def execute_strategy():

    strategy_name = 'Short Vol with SVXY | SVXY FTLT'
    sym_list = ['SVXY', 'UVXY', 'VIXY', 'XLK', 'SPY', 'SHV', 'QQQ']
    end_date = datetime.today()
    start_date = end_date - timedelta(days=50)
    hist_days_list = [1 , 5, 10, 14, 20, 21]

    stock_historical_data = ed.get_hist_data(sym_list,start_date,end_date)
    # stock_historical_data = pd.read_csv('stock_historical_data.csv')
    # stock_historical_data = stock_historical_data[stock_historical_data['date'] <= '2023-10-26']
    stock_tech_summ_data = ti.get_technical_data(sym_list,stock_historical_data,hist_days_list)

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

    alloc_df['strategy_name'] = strategy_name
    alloc_df['eff_date'] = end_date

    curr_alloc_df = alloc_df[['strategy_name','eff_date','ticker']]

    return curr_alloc_df