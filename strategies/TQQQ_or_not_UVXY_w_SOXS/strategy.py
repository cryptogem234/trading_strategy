import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from datetime import datetime, timedelta
from strategies.TQQQ_or_not_UVXY_w_SOXS import config as cfg

def get_historical_data():
    sym_list = cfg.sym_list
    start_date = cfg.start_date
    end_date = cfg.end_date

    stock_historical_data = ed.get_hist_data(sym_list, start_date, end_date)

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


    alloc_df['strategy_name'] = cfg.strategy_name
    curr_alloc_df = alloc_df[['strategy_name','date','ticker','close','PCTRET']]
    curr_alloc_df['close'] = curr_alloc_df['close'].round(2)
    curr_alloc_df['PCTRET'] = (curr_alloc_df['PCTRET'] * 100).round(4)
    curr_alloc_df = curr_alloc_df.rename(columns={'PCTRET': 'pctreturn'})
    curr_alloc_df['date'] = pd.to_datetime(curr_alloc_df['date']).dt.strftime('%m/%d/%Y')

    return curr_alloc_df
