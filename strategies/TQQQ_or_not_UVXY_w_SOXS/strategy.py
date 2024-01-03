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

    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path to the CSV file
    hist_alloc_df_path = os.path.join(current_directory, 'hist_alloc_df.csv')
    hist_alloc_df = pd.read_csv(hist_alloc_df_path)

    hist_alloc_df['eff_date'] = pd.to_datetime(hist_alloc_df['eff_date'], errors='coerce')
    latest_hist_alloc_df = hist_alloc_df[['ticker']][hist_alloc_df['eff_date'] == hist_alloc_df['eff_date'].max()]

    df_1 = curr_alloc_df[['ticker']].astype(str).reset_index(drop=True)
    df_2 = latest_hist_alloc_df[['ticker']].astype(str).reset_index(drop=True)

    if df_1.equals(df_2) != True:
        curr_alloc_df['action'] = 'Rebalancing Required'
        curr_alloc_df.to_csv(hist_alloc_df_path, mode='a', index=False, header=False)
    else:
        curr_alloc_df['action'] = 'NO Rebalancing Required'

    curr_alloc_df['eff_date'] = pd.to_datetime(curr_alloc_df['eff_date']).apply(lambda x: x.strftime('%Y-%m-%d %I:%M %p'))

    return curr_alloc_df
