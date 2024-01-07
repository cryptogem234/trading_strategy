import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from datetime import datetime, timedelta
import numpy as np
import os
from strategies.Nothing_But_Bonds.TMF_Momentum import tmf_momentum_string as tmf
from strategies.Nothing_But_Bonds.TMV_Momentum import tmv_momentum_string as tmv
from strategies.Nothing_But_Bonds.TLT_Macro_Momentum import tlt_macro_momentum_string as tlt
from strategies.Nothing_But_Bonds.IEF_Macro_Momentum import ief_momentum_string as ief

def execute_strategy():

    strategy_name = 'Bonds Momentum - IEF, TLT, TMF, TMV Momentums'
    sym_list = ['TMF', 'TMV', 'TQQQ', 'BND', 'TLT', 'SHV', 'SHY', 'IEF', 'UBT']
    end_date = datetime.today()
    start_date = end_date - timedelta(days=1000)
    hist_days_list = [1, 3, 5, 8, 10, 15, 20, 21, 50, 60, 110, 200, 350, 450, 550]

    stock_historical_data = ed.get_hist_data(sym_list,start_date,end_date)

    # stock_historical_data.to_csv('stock_historical_data.csv')
    # stock_historical_data = pd.read_csv('stock_historical_data.csv')
    # stock_historical_data = stock_historical_data[stock_historical_data['date']<='2023-12-11']

    stock_tech_summ_data = ti.get_technical_data(sym_list,stock_historical_data, hist_days_list)

    df = stock_tech_summ_data.copy()

    if df['RSI_10'][df['ticker'] == 'TMF'].values[0] < 30:
        alloc_df = df[df['ticker'] == 'TMF']
    else:
        if df['MDD_10'][df['ticker'] == 'TMV'].values[0] < 0.07:
            if df['MDD_10'][df['ticker'] == 'TQQQ'].values[0] < 0.07:
                alloc_df = df[df['ticker'] == 'TMF']
            else:
                if df['EMA_5'][df['ticker'] == 'TMF'].values[0] > df['SMA_200'][df['ticker'] == 'TMF'].values[0]:
                    alloc_df = df[df['ticker'] == 'TMF']
                else:
                    if df['EMA_3'][df['ticker'] == 'TMV'].values[0] > df['SMA_20'][df['ticker'] == 'TMV'].values[0]:
                        alloc_df = df[df['ticker'] == 'TMV']

                    else:
                        alloc_tkr_1 = tmf(df)
                        alloc_tkr_2 = tmv(df)
                        alloc_tkr_3 = tlt(df)
                        alloc_tkr_4 = ief(df)
                        alloc_tkr = [alloc_tkr_1, alloc_tkr_2, alloc_tkr_3, alloc_tkr_4]
                        alloc_df = df[df['ticker'].isin(alloc_tkr)]

        else:
            alloc_tkr_1 = tmf(df)
            alloc_tkr_2 = tmv(df)
            alloc_tkr_3 = tlt(df)
            alloc_tkr_4 = ief(df)
            alloc_tkr = [alloc_tkr_1, alloc_tkr_2, alloc_tkr_3, alloc_tkr_4]
            alloc_df = df[df['ticker'].isin(alloc_tkr)]

    alloc_df['strategy_name'] = strategy_name
    alloc_df['eff_date'] = end_date

    curr_alloc_df = alloc_df[['strategy_name','eff_date','ticker']]
    curr_alloc_df = (curr_alloc_df.groupby(['strategy_name', 'eff_date']).agg({'ticker': lambda x: ' , '.join(x)}).reset_index())

    return curr_alloc_df


