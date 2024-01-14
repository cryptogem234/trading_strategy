import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from strategies.WAM_FTLT_w_TMF.TQQQ_or_Not import tqqq_or_not as tqqq
from strategies.WAM_FTLT_w_TMF import config as cfg

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

    if df['SMR_575'][df['ticker'] == 'SHY'].values[0] < 0:
        if df['RSI_14'][df['ticker'] == 'TMF'].values[0] > 60:
            if df['RSI_11'][df['ticker'] == 'IEF'].values[0] < df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                if df['SMR_600'][df['ticker'] == 'XBI'].values[0] < 0:
                    alloc_tkr1 = ['LABU']
                else:
                    alloc_tkr1 = ['SPXL']
                alloc_tkr = ['TECL','TQQQ','DRN','URTY','TMF','LABU','SPXL']
                alloc_tkr = alloc_tkr + alloc_tkr1
                alloc_df = df[df['ticker'].isin(alloc_tkr)].sort_values(by='SMR' + '_' + '4',ascending=False).head(1)
            else:
                if df['SMR_600'][df['ticker'] == 'XBI'].values[0] < 0:
                    alloc_tkr1 = ['LABD']
                else:
                    alloc_tkr1 = ['SPXS']
                alloc_tkr = ['PSQ', 'TYO', 'DRV', 'TMV', 'SH', 'LABD', 'SPXS']
                alloc_tkr = alloc_tkr + alloc_tkr1
                alloc_df = df[df['ticker'].isin(alloc_tkr)].sort_values(by='SMR' + '_' + '4', ascending=False).head(1)
        else:
            if df['RSI_11'][df['ticker'] == 'IEF'].values[0] > df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                if df['SMR_600'][df['ticker'] == 'XBI'].values[0] < 0:
                    alloc_tkr1 = ['LABU']
                else:
                    alloc_tkr1 = ['SPXL']
                alloc_tkr = ['TECL','TQQQ','DRN','URTY','TMF','LABU','SPXL']
                alloc_tkr = alloc_tkr + alloc_tkr1
                alloc_df = df[df['ticker'].isin(alloc_tkr)].sort_values(by='SMR' + '_' + '4', ascending=True).head(1)
            else:
                if df['SMR_600'][df['ticker'] == 'XBI'].values[0] < 0:
                    alloc_tkr1 = ['LABD']
                else:
                    alloc_tkr1 = ['SPXS']
                alloc_tkr = ['PSQ', 'TYO', 'DRV', 'TMV', 'SH', 'LABD', 'SPXS']
                alloc_tkr = alloc_tkr + alloc_tkr1
                alloc_df = df[df['ticker'].isin(alloc_tkr)].sort_values(by='SMR' + '_' + '4', ascending=True).head(1)

    else:
        if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['SOXL'])]
        else:
            if df['RSI_14'][df['ticker'] == 'SPY'].values[0] < 30:
                alloc_df = df[df['ticker'].isin(['UPRO'])]
            else:
                if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 80:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    alloc_tkr = tqqq(df)
                    alloc_df = df[df['ticker'].isin([alloc_tkr])]

    alloc_df['strategy_name'] = cfg.strategy_name
    curr_alloc_df = alloc_df[['strategy_name','date','ticker','close','PCTRET']]
    curr_alloc_df['close'] = curr_alloc_df['close'].round(2)
    curr_alloc_df['PCTRET'] = (curr_alloc_df['PCTRET'] * 100).round(4)
    curr_alloc_df = curr_alloc_df.rename(columns={'PCTRET': 'pctreturn'})
    curr_alloc_df['date'] = pd.to_datetime(curr_alloc_df['date']).dt.strftime('%m/%d/%Y')

    return curr_alloc_df
