import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from strategies.WMDYN_FTLT import config as cfg

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

    #stock_tech_full_data.to_csv('stock_tech_full_data.csv')
    #stock_tech_full_data = pd.read_csv('stock_tech_full_data.csv')
    #stock_tech_summ_data = stock_tech_full_data[stock_tech_full_data['date']=='2023-11-16']


    df = stock_tech_summ_data.copy()


    if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] > 79:
        alloc_df = df[df['ticker'].isin(['UVXY'])]
    else:
        if df['RSI_10'][df['ticker'] == 'XLK'].values[0] > 79:
            alloc_df = df[df['ticker'].isin(['UVXY'])]
        else:
            if df['RSI_10'][df['ticker'] == 'VOX'].values[0] > 79:
                alloc_df = df[df['ticker'].isin(['UVXY'])]
            else:
                if df['RSI_10'][df['ticker'] == 'VTV'].values[0] > 79:
                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                else:
                    if df['RSI_10'][df['ticker'] == 'SOXX'].values[0] > 79:
                        alloc_df = df[df['ticker'].isin(['UVXY'])]
                    else:
                        if df['RSI_10'][df['ticker'] == 'SPY'].values[0] > 79:
                            alloc_df = df[df['ticker'].isin(['UVXY'])]
                        else:
                            if df['RSI_13'][df['ticker'] == 'QQQ'].values[0] < 30:
                                alloc_df = df[df['ticker'].isin(['TECL'])]
                            else:
                                if df['RSI_5'][df['ticker'] == 'SPY'].values[0] < 25:
                                    alloc_df = df[df['ticker'].isin(['TLT', 'SVXY', 'TECL', 'SOXL'])].sort_values(by='RSI_5', ascending=False).head(1)
                                else:
                                    if df['STDR_10'][df['ticker'] == 'SPY'].values[0] > 0.025:
                                        alloc_df = df[df['ticker'].isin(['UVXY', 'TMF', 'SPXU'])].sort_values(by='RSI_5', ascending=False).head(1)
                                    else:
                                        if df['SMR_100'][df['ticker'] == 'BIL'].values[0] < df['SMR_100'][df['ticker'] == 'TLT'].values[0]:
                                            if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.08:
                                                if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.04:
                                                    alloc_df = df[df['ticker'].isin(['UVXY'])]
                                                else:
                                                    alloc_df = df[df['ticker'].isin(['SOXL'])]
                                            else:
                                                alloc_df = df[df['ticker'].isin(['TLT', 'SVXY', 'TECL', 'SOXL'])].sort_values( by='RSI_5', ascending=False).head(1)

                                        else:
                                            if df['RSI_10'][df['ticker'] == 'IEF'].values[0] > df['RSI_20'][df['ticker'] == 'PSQ'].values[0]:
                                                alloc_df = df[df['ticker'].isin(['TLT', 'SVXY', 'TECL', 'SOXL'])].sort_values(by='RSI_5', ascending=False).head(1)
                                            else:
                                                if df['close'][df['ticker'] == 'SPY'].values[0] > df['SMA_200'][df['ticker'] == 'SPY'].values[0]:
                                                    alloc_df = df[df['ticker'].isin(['BTAL', 'SPLV', 'DBC', 'UGL'])].sort_values(by='RSI_5', ascending=False).head(2)
                                                else:
                                                    if df['RSI_60'][df['ticker'] == 'SPY'].values[0] > 50:
                                                        alloc_df1 = df[df['ticker'].isin(['SOXS'])]
                                                        alloc_df2 = df[df['ticker'].isin(['SOXS', 'TLT', 'TECS'])].sort_values(by='RSI_5', ascending=False).head(1)
                                                        alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True,sort=False)
                                                    else:
                                                        if df['RSI_200'][df['ticker'] == 'IEF'].values[0] < df['RSI_200'][df['ticker'] == 'TLT'].values[0]:
                                                            alloc_df1 = df[df['ticker'].isin(['SQQQ'])]
                                                            alloc_df2 = df[df['ticker'].isin(['SQQQ', 'TMV', 'SOXS'])].sort_values(by='RSI_5', ascending=False).head(1)
                                                            alloc_df = pd.concat([alloc_df1, alloc_df2], ignore_index=True,sort=False)
                                                        else:
                                                            alloc_df = df[df['ticker'].isin(['TLT', 'SVXY', 'TECL', 'SOXL'])].sort_values(by='RSI_5', ascending=False).head(1)

    alloc_df['pct_alloc'] = (1 / alloc_df['ticker'].count() * 100).round(0)

    alloc_df['strategy_name'] = cfg.strategy_name
    curr_alloc_df = alloc_df[['strategy_name', 'date', 'ticker', 'close', 'PCTRET', 'pct_alloc']]
    curr_alloc_df['close'] = curr_alloc_df['close'].round(2)
    curr_alloc_df['PCTRET'] = (curr_alloc_df['PCTRET'] * 100).round(4)
    curr_alloc_df = curr_alloc_df.rename(columns={'PCTRET': 'pctreturn'})
    curr_alloc_df['date'] = pd.to_datetime(curr_alloc_df['date']).dt.strftime('%m/%d/%Y')
    curr_alloc_df = (curr_alloc_df.groupby(['strategy_name', 'date', 'ticker', 'close', 'pctreturn']).agg({'pct_alloc': 'sum'}).reset_index())

    return curr_alloc_df


