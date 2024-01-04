import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from datetime import datetime, timedelta
import numpy as np
import os

def execute_strategy():

    strategy_name = 'V1a TQQQ or not - Replace UVXY w SOXS'
    sym_list = ['TQQQ', 'SOXS', 'SOXL', 'BIL', 'UVXY', 'QQQ', 'TMF', 'SPY', 'BND', 'TLT', 'IEF']
    end_date = datetime.today()
    start_date = end_date - timedelta(days=300)
    hist_days_list = [1, 3, 5, 6, 8, 10, 15, 20, 25, 45, 50, 60, 110, 200]

    stock_historical_data = ed.get_hist_data(sym_list,start_date,end_date)

    # stock_historical_data.to_csv('stock_historical_data.csv')
    # stock_historical_data = pd.read_csv('stock_historical_data.csv')
    # stock_historical_data = stock_historical_data[stock_historical_data['date']<='2022-10-13']

    stock_tech_hist_data, stock_tech_summ_data = ti.get_technical_data(sym_list,stock_historical_data,hist_days_list)

    df = stock_tech_summ_data

    if df['RSI_10'][df['ticker']=='TQQQ'].values[0] > 79:
        ## Risk OFF ##
        alloc_df = df[df['ticker'] == 'SOXS']

    else:
        if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.12:
            if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                alloc_df = df[df['ticker'] == 'UVXY']

            else:
                if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 32:
                    alloc_df = df[df['ticker'] == 'SOXL']

                else:
                    if df['MDD_10'][df['ticker'] == 'TMF'].values[0] < 0.07:
                        alloc_df = df[df['ticker'] == 'SOXL']

                    else:
                        alloc_df = df[df['ticker'] == 'BIL']

        else:
            if df['MDD_10'][df['ticker'] == 'QQQ'].values[0] > 0.06:
                alloc_df = df[df['ticker'] == 'BIL']

            else:
                if df['MDD_10'][df['ticker'] == 'TMF'].values[0] > 0.07:
                    alloc_df = df[df['ticker'] == 'BIL']

                else:
                    if df['close'][df['ticker'] == 'QQQ'].values[0] > df['SMA_25'][df['ticker'] == 'QQQ'].values[0]:
                        alloc_df = df[df['ticker'] == 'TQQQ']

                    else:
                        if df['RSI_60'][df['ticker'] == 'SPY'].values[0] > 50:
                            if  df['RSI_45'][df['ticker'] == 'BND'].values[0] > df['RSI_45'][df['ticker'] == 'SPY'].values[0]:
                                alloc_df = df[df['ticker'] == 'TQQQ']

                            else:
                                alloc_df = df[df['ticker'] == 'BIL']

                        else:
                            if df['RSI_200'][df['ticker'] == 'IEF'].values[0] < df['RSI_200'][df['ticker'] == 'TLT'].values[0]:
                                if df['RSI_45'][df['ticker'] == 'BND'].values[0] > df['RSI_45'][df['ticker'] == 'SPY'].values[0]:
                                    alloc_df = df[df['ticker'] == 'TQQQ']

                                else:
                                    alloc_df = df[df['ticker'] == 'BIL']

                            else:
                                alloc_df = df[df['ticker'] == 'BIL']


    alloc_df['strategy_name'] = strategy_name
    alloc_df['eff_date'] = end_date

    curr_alloc_df = alloc_df[['strategy_name','eff_date','ticker']]

    return curr_alloc_df
