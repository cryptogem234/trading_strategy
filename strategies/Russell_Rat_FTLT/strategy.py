import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from datetime import datetime, timedelta
from strategies.Russell_Rat_FTLT.TQQQ_or_Not import tqqq_or_not as tqn
import numpy as np
import os

def execute_strategy():

    strategy_name = 'Russell Rat FTLT'
    sym_list = ['SPY','SHY','TMF','IEF','IWM','URTY','SRTY','UVXY','TQQQ','BIL','QQQ','BND','TLT']

    end_date = datetime.today()
    start_date = end_date - timedelta(days=1000)
    hist_days_list = [1,5,6,10,11,14,16,25,45,60,200,600]

    stock_historical_data = ed.get_hist_data(sym_list, start_date, end_date)

    # stock_historical_data.to_csv('stock_historical_data.csv')
    # stock_historical_data = pd.read_csv('stock_historical_data.csv')
    # stock_historical_data = stock_historical_data[stock_historical_data['date']<='2022-10-13']

    stock_tech_hist_data, stock_tech_summ_data = ti.get_technical_data(sym_list, stock_historical_data, hist_days_list)

    df = stock_tech_summ_data

    if df['RSI_10'][df['ticker']=='SPY'].values[0] > 71:
        ### Russell Rat FTLT - TMF Check ###
        if df['SMR_600'][df['ticker'] == 'SHY'].values[0] < 0:
            if df['RSI_14'][df['ticker'] == 'TMF'].values[0] > 60:
                if df['RSI_11'][df['ticker'] == 'IEF'].values[0] < df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                    alloc_df = df[df['ticker'] == 'URTY']
                else:
                    alloc_df = df[df['ticker'] == 'SRTY']
            else:
                if df['RSI_11'][df['ticker'] == 'IEF'].values[0] > df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                    alloc_df = df[df['ticker'] == 'URTY']
                else:
                    alloc_df = df[df['ticker'] == 'SRTY']
        else:
            ###TQQQ Or Not ###
            alloc_tkr_1 = tqn(df)
            alloc_tkr = [alloc_tkr_1]
            alloc_df = df[df['ticker'].isin(alloc_tkr)]
    else:
        ### Russell Rat FTLT - No TMF Check ###
        if df['SMR_600'][df['ticker'] == 'SHY'].values[0] < 0:
            if df['RSI_11'][df['ticker'] == 'IEF'].values[0] > df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                alloc_df = df[df['ticker'] == 'URTY']
            else:
                alloc_df = df[df['ticker'] == 'SRTY']
        else:
            ###TQQQ Or Not ###
            alloc_tkr_1 = tqn(df)
            alloc_tkr = [alloc_tkr_1]
            alloc_df = df[df['ticker'].isin(alloc_tkr)]

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
