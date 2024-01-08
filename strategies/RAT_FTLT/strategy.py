import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from datetime import datetime, timedelta
from strategies.RAT_FTLT.TQQQ_or_Not import tqqq_or_not as tqn

def execute_strategy():

    strategy_name = 'RAT FTLT Banks, Small Cap, Russell, HealthCare, Real Estate, High Beta, Foreign'
    list = ['SPY','SHY','TMF','IEF','IWM','UVXY','TQQQ','BIL','QQQ','BND','TLT']
    bank = ['FAS','FAZ']
    house = ['DRN','DRV']
    smallcap = ['TNA','TZA']
    lab = ['LABU','LABD']
    russell = ['URTY','SRTY']
    beta = ['HIBL', 'HIBS']
    foreign = ['EDC', 'EDZ']
    sym_list = list + bank + house + smallcap + lab + russell + beta + foreign

    end_date = datetime.today()
    start_date = end_date - timedelta(days=1000)
    hist_days_list = [1,5,6,10,11,14,16,25,45,60,200,600]

    stock_historical_data = ed.get_hist_data(sym_list, start_date, end_date)

    # stock_historical_data.to_csv('stock_historical_data.csv')
    # stock_historical_data = pd.read_csv('stock_historical_data.csv')
    #stock_historical_data = stock_historical_data[stock_historical_data['date']<='2023-11-30']

    stock_tech_summ_data = ti.get_technical_data(sym_list, stock_historical_data, hist_days_list)

    df = stock_tech_summ_data

    if df['RSI_10'][df['ticker']=='SPY'].values[0] > 71:
        ### TMF Check ###
        if df['SMR_600'][df['ticker'] == 'SHY'].values[0] < 0:
            if df['RSI_14'][df['ticker'] == 'TMF'].values[0] > 60:
                if df['RSI_11'][df['ticker'] == 'IEF'].values[0] < df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                    alloc_tkr = ['FAS','DRN','TNA','LABU','URTY','HIBL', 'EDC']
                    alloc_df = df[df['ticker'].isin(alloc_tkr)]
                else:
                    alloc_tkr = ['FAZ', 'DRV', 'TZA','LABD','SRTY','HIBS', 'EDZ']
                    alloc_df = df[df['ticker'].isin(alloc_tkr)]
            else:
                if df['RSI_11'][df['ticker'] == 'IEF'].values[0] > df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                    alloc_tkr = ['FAS', 'DRN', 'TNA', 'LABU', 'URTY', 'HIBL', 'EDC']
                    alloc_df = df[df['ticker'].isin(alloc_tkr)]
                else:
                    alloc_tkr = ['FAZ', 'DRV', 'TZA', 'LABD', 'SRTY', 'HIBS', 'EDZ']
                    alloc_df = df[df['ticker'].isin(alloc_tkr)]
        else:
            ###TQQQ Or Not ###
            alloc_tkr_1 = tqn(df)
            alloc_tkr = [alloc_tkr_1]
            alloc_df = df[df['ticker'].isin(alloc_tkr)]
    else:
        ### Russell Rat FTLT - No TMF Check ###
        if df['SMR_600'][df['ticker'] == 'SHY'].values[0] < 0:
            if df['RSI_11'][df['ticker'] == 'IEF'].values[0] > df['RSI_16'][df['ticker'] == 'IWM'].values[0]:
                alloc_tkr = ['FAS', 'DRN', 'TNA', 'LABU', 'URTY', 'HIBL', 'EDC']
                alloc_df = df[df['ticker'].isin(alloc_tkr)]
            else:
                alloc_tkr = ['FAZ', 'DRV', 'TZA', 'LABD', 'SRTY', 'HIBS', 'EDZ']
                alloc_df = df[df['ticker'].isin(alloc_tkr)]
        else:
            ###TQQQ Or Not ###
            alloc_tkr_1 = tqn(df)
            alloc_tkr_tqqq = [alloc_tkr_1]
            alloc_df = df[df['ticker'].isin(alloc_tkr_tqqq)]

    #alloc_df = alloc_df.sort_values(by='SMR' + '_' + '10', ascending=True).head(3)
    alloc_df['strategy_name'] = strategy_name
    alloc_df['eff_date'] = end_date

    alloc_df = (alloc_df.groupby(['strategy_name','eff_date']).agg({'ticker': lambda x: ' , '.join(x)}).reset_index())

    curr_alloc_df = alloc_df[['strategy_name','eff_date','ticker']]

    return curr_alloc_df
