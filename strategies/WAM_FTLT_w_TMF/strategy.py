import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from datetime import datetime, timedelta
from strategies.WAM_FTLT_w_TMF.TQQQ_or_Not import tqqq_or_not as tqqq

def execute_strategy():

    strategy_name = 'WAM FTLT'
    sym_list = ['SHY','TMF','IEF','IWM','XBI','QQQ','SPY','TQQQ','BND','TLT','LABD','SPXS','UVXY',
                'UPRO','TECL','DRN','SOXL','URTY','LABU','SPXL','PSQ','TYO','DRV','TMV','SH']

    tqqq_sym_list = ['TQQQ', 'SOXS', 'SOXL', 'BIL', 'UVXY', 'QQQ', 'TMF', 'SPY', 'BND', 'TLT', 'IEF']

    sym_list = sym_list + list(set(tqqq_sym_list) - set(sym_list))

    end_date = datetime.today()
    start_date = end_date - timedelta(days=1000)
    hist_days_list = [1, 4, 6, 10, 11, 14, 16, 25, 45, 60, 200, 575, 600]

    stock_historical_data = ed.get_hist_data(sym_list,start_date,end_date)

    #stock_historical_data.to_csv('stock_historical_data.csv')
    #stock_historical_data = pd.read_csv('stock_historical_data.csv')
    #stock_historical_data = stock_historical_data[stock_historical_data['date']<='2024-01-02']

    stock_tech_summ_data = ti.get_technical_data(sym_list,stock_historical_data,hist_days_list)

    df = stock_tech_summ_data

    if df['SMR_575'][df['ticker'] == 'SHY'].values[0] < 0:
        if df['RSI_14'][df['ticker'] == 'TMF'].values[0] > 60:
            if df['RSI_11'][df['ticker'] == 'IEF'].values[0] < df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                alloc_df = df[df['ticker'].isin(['TECL','TQQQ','DRN','URTY','TMF','LABU','SPXL'])].sort_values(by='SMR' + '_' + '4',ascending=False).head(1)
            else:
                alloc_df = df[df['ticker'].isin(['PSQ', 'TYO', 'DRV', 'TMV', 'SH', 'LABD', 'SPXS'])].sort_values(by='SMR' + '_' + '4', ascending=False).head(1)
        else:
            if df['RSI_11'][df['ticker'] == 'IEF'].values[0] > df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                alloc_df = df[df['ticker'].isin(['TECL', 'TQQQ', 'DRN', 'SOXL', 'URTY', 'TMF', 'LABU', 'SPXL'])].sort_values(by='SMR' + '_' + '4', ascending=True).head(1)
            else:
                alloc_df = df[df['ticker'].isin(['PSQ', 'TYO', 'DRV', 'TMV', 'SH', 'LABD', 'SPXS'])].sort_values(by='SMR' + '_' + '4', ascending=True).head(1)

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

    alloc_df['strategy_name'] = strategy_name
    alloc_df['eff_date'] = end_date

    alloc_df = (alloc_df.groupby(['strategy_name', 'eff_date']).agg({'ticker': lambda x: ' , '.join(x)}).reset_index())

    curr_alloc_df = alloc_df[['strategy_name','eff_date','ticker']]

    return curr_alloc_df