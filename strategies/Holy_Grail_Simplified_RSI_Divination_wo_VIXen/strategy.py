import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from strategies.Holy_Grail_Simplified_RSI_Divination_wo_VIXen import config as cfg

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

    # stock_historical_data.to_csv('stock_historical_data.csv')
    # stock_historical_data = pd.read_csv('stock_historical_data.csv')
    # stock_historical_data = stock_historical_data[stock_historical_data['date']<='2023-12-11']

    df = stock_tech_summ_data.copy()

    if df['close'][df['ticker'] == 'SPY'].values[0] > df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
        if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 81:
            alloc_df = df[df['ticker'].isin(['UVXY', 'SQQQ'])].sort_values(by='RSI' + '_' + '13', ascending=False).head(1)
        else:
            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 80:
                alloc_df = df[df['ticker'].isin(['UVXY', 'SPXU'])].sort_values(by='RSI' + '_' + '13',ascending=False).head(1)
            else:
                if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] > 65:
                    alloc_df = df[df['ticker'].isin(['TQQQ'])]
                else:
                    alloc_df = df[df['ticker'].isin(['TQQQ', 'STIP'])].sort_values(by='RSI' + '_' + '11',ascending=True).head(1)
    else:
        if df['RSI_10'][df['ticker'] == 'QQQ'].values[0] < 30:
            alloc_df = df[df['ticker'].isin(['TECL', 'SHY'])].sort_values(by='RSI' + '_' + '11', ascending=True).head(1)
        else:
            if df['RSI_10'][df['ticker'] == 'SPY'].values[0] < 30:
                alloc_df = df[df['ticker'].isin(['UPRO', 'SHY'])].sort_values(by='RSI' + '_' + '11',ascending=True).head(1)
            else:
                if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.11:
                    if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.055:
                        alloc_df = df[df['ticker'].isin(['UVXY', 'SQQQ'])].sort_values(by='RSI' + '_' + '11',ascending=False).head(1)
                    else:
                        if df['CUMR_1'][df['ticker'] == 'SQQQ'].values[0] > 0.028:
                            alloc_df1 = df[df['ticker'].isin(['TQQQ','UDN'])].sort_values(by='RSI' + '_' + '11',ascending=True).head(1)
                            alloc_df2 = df[df['ticker'].isin(['TQQQ', 'TMV'])].sort_values(by='RSI' + '_' + '11',ascending=False).head(1)
                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                        else:
                            alloc_df1 = df[df['ticker'].isin(['SOXL','SHV'])].sort_values(by='RSI' + '_' + '11',ascending=True).head(1)
                            alloc_df2 = df[df['ticker'].isin(['TQQQ', 'STIP'])].sort_values(by='RSI' + '_' + '11',ascending=True).head(1)
                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True, sort=False)
                else:
                    if df['close'][df['ticker'] == 'QLD'].values[0] > df['SMA_20'][df['ticker'] == 'QLD'].values[0]:
                        alloc_df = df[df['ticker'].isin(['TQQQ', 'STIP'])].sort_values(by='RSI' + '_' + '11',ascending=True).head(1)
                    else:
                        if df['SMR_20'][df['ticker'] == 'TLT'].values[0] > df['SMR_20'][df['ticker'] == 'UDN'].values[0]:
                            alloc_df1 = df[df['ticker'].isin(['TLT', 'SQQQ'])].sort_values(by='RSI' + '_' + '11',ascending=False).head(1)
                        else:
                            alloc_df1 = df[df['ticker'].isin(['UUP', 'SQQQ'])].sort_values(by='RSI' + '_' + '10',ascending=True).head(1)
                        alloc_df2 = df[df['ticker'].isin(['UGL', 'SQQQ'])].sort_values(by='RSI' + '_' + '12',ascending=True).head(1)
                        alloc_df = pd.concat([alloc_df1,alloc_df2], ignore_index=True, sort=False)

    alloc_df['strategy_name'] = cfg.strategy_name
    curr_alloc_df = alloc_df[['strategy_name', 'date', 'ticker', 'close', 'PCTRET']]
    curr_alloc_df['close'] = curr_alloc_df['close'].round(2)
    curr_alloc_df['PCTRET'] = (curr_alloc_df['PCTRET'] * 100).round(4)
    curr_alloc_df = curr_alloc_df.rename(columns={'PCTRET': 'pctreturn'})
    curr_alloc_df['date'] = pd.to_datetime(curr_alloc_df['date']).dt.strftime('%m/%d/%Y')

    curr_alloc_df['pct_alloc'] = (1 / curr_alloc_df['ticker'].count() * 100).round(0)

    curr_alloc_df = (curr_alloc_df.groupby(['strategy_name', 'date', 'ticker', 'close', 'pctreturn']).agg({'pct_alloc': 'sum'}).reset_index())

    #curr_alloc_df = (curr_alloc_df.groupby(['strategy_name', 'eff_date']).agg({'ticker': lambda x: ' , '.join(x)}).reset_index())

    return curr_alloc_df