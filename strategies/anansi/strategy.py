import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from strategies.anansi import config as cfg
from strategies.anansi.frontrunner_mild_tqqq import frontrunner_mild_tqqq
from strategies.anansi.moderated_wmdyn_ftlt import moderated_wmdyn_ftlt
from strategies.anansi.frontrunner_200d_inverse import frontrunner_200d_inverse
from strategies.anansi.indecent_vixation import indecent_vixation
from strategies.anansi.beta_baller_cleaned_up import beta_baller_cleaned_up
pd.options.display.max_columns = None
pd.options.display.max_rows = None

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
    #stock_tech_summ_data = stock_tech_full_data[stock_tech_full_data['date']=='2024-03-19']

    df = stock_tech_summ_data.copy()

    if df['RSI_14'][df['ticker'] == 'VIXM'].values[0] > 65:

        ### 'Frontrunner Mild TQQQ Stuff | 2011-11-01' ###
        alloc_df = frontrunner_mild_tqqq(df)
        alloc_df['strategy_name'] = 'Frontrunner Mild TQQQ Stuff | 2011-11-01'

    else:
        alloc_df1 = moderated_wmdyn_ftlt(df)
        alloc_df1['strategy_name'] = 'Moderated WMDYN FTLT | Anansi + WHS | 2018-01-30'
        alloc_df1['pct_alloc'] = (1 / alloc_df1['ticker'].count() * 100).round(0)

        alloc_df2 = frontrunner_200d_inverse(df)
        alloc_df2['strategy_name'] = 'Frontrunner 200D Inverse | 2018-02-06'
        alloc_df2['pct_alloc'] = (1 / alloc_df2['ticker'].count() * 100).round(0)

        alloc_df3 = frontrunner_mild_tqqq(df)
        alloc_df3['strategy_name'] = 'Frontrunner Mild TQQQ Stuff | 2011-11-01'
        alloc_df3['pct_alloc'] = (1 / alloc_df3['ticker'].count() * 100).round(0)

        alloc_df4 = indecent_vixation(df)
        alloc_df4['strategy_name'] = 'Indecent VIXation V2 | 2011-10-18'
        alloc_df4['pct_alloc'] = (1 / alloc_df4['ticker'].count() * 100).round(0)

        alloc_df5 = beta_baller_cleaned_up(df)
        alloc_df5['strategy_name'] = 'Beta Baller Anti-Twitch | Cleaned Up | Anansi | 2014-01-04'
        alloc_df5['pct_alloc'] = (1 / alloc_df5['ticker'].count() * 100).round(0)

        alloc_df = pd.concat([alloc_df1, alloc_df2, alloc_df3, alloc_df4, alloc_df5], ignore_index=True, sort=False)

    curr_alloc_df = alloc_df[['strategy_name', 'date', 'ticker', 'close', 'PCTRET', 'pct_alloc']]
    curr_alloc_df['close'] = curr_alloc_df['close'].round(2)
    curr_alloc_df['PCTRET'] = (curr_alloc_df['PCTRET'] * 100).round(4)
    curr_alloc_df = curr_alloc_df.rename(columns={'PCTRET': 'pctreturn'})
    curr_alloc_df['date'] = pd.to_datetime(curr_alloc_df['date']).dt.strftime('%m/%d/%Y')
    curr_alloc_df = (curr_alloc_df.groupby(['strategy_name', 'date', 'ticker', 'close', 'pctreturn']).agg({'pct_alloc': 'sum'}).reset_index())

    return curr_alloc_df