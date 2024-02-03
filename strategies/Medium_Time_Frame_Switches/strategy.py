import pandas as pd
from data import exract_data as ed, tech_indicators as ti
from strategies.Medium_Time_Frame_Switches import strategies_group as stg
from strategies.Medium_Time_Frame_Switches import config as cfg

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
    # stock_historical_data = pd.read_csv('stock_tech_full_data.csv')
    # stock_historical_data = stock_historical_data[stock_historical_data['date']=='2024-02-02']
    # stock_tech_summ_data = stock_historical_data

    df = stock_tech_summ_data.copy()

    ### 60 Day RSI Strategy ###

    alloc_df1 = stg.dia_rsi(df)
    alloc_df2 = stg.spy_rsi(df)
    alloc_df3 = stg.qqq_rsi(df)
    alloc_df4 = stg.xlk_rsi(df)
    alloc_df5 = stg.soxx_rsi(df)

    alloc_df_rsi = pd.concat([alloc_df1, alloc_df2, alloc_df3, alloc_df4, alloc_df5], ignore_index=True, sort=False)

    alloc_df_rsi = alloc_df_rsi.sort_values(by='STDR_37', ascending=False).head(4)
    alloc_df_rsi['strategy_typ'] = '60 Day RSI'


    ### 20 Day BND Vs 60 Day SH ###
    alloc_df_20d_bnd_60d_sh = stg.bnd20_sh60_v1(df)
    alloc_df_20d_bnd_60d_sh['strategy_typ'] = '20 Day BND Vs 60 Day SH'

    ### 60 Day BND vs BIL ###
    alloc_df_60d_bnd_bil = stg.bnd60_bil_v1(df)
    alloc_df_60d_bnd_bil['strategy_typ'] = '60 Day BND vs BIL'

    ### V1 BWC: Sub-Zero RSI MA Crossover (BT June 2 2015) Spicy Edition incl. UVXY & Extreme Beta ###
    alloc_df_rsi_crossover = stg.rsi_crossover(df)
    alloc_df_rsi_crossover['strategy_typ'] = 'Sub-Zero RSI MA Crossover'

    alloc_df = pd.concat([alloc_df_rsi, alloc_df_20d_bnd_60d_sh, alloc_df_60d_bnd_bil, alloc_df_rsi_crossover], ignore_index=True, sort=False)

    alloc_df['strategy_name'] = cfg.strategy_name
    curr_alloc_df = alloc_df[['strategy_name', 'strategy_typ', 'date', 'ticker', 'close', 'PCTRET']]
    curr_alloc_df['close'] = curr_alloc_df['close'].round(2)
    curr_alloc_df['PCTRET'] = (curr_alloc_df['PCTRET'] * 100).round(4)
    curr_alloc_df = curr_alloc_df.rename(columns={'PCTRET': 'pctreturn'})
    curr_alloc_df['date'] = pd.to_datetime(curr_alloc_df['date']).dt.strftime('%m/%d/%Y')

    curr_alloc_df['pct_alloc'] = (1 / curr_alloc_df['ticker'].count() * 100).round(0)

    curr_alloc_df = (curr_alloc_df.groupby(['strategy_name', 'date', 'ticker', 'close', 'pctreturn']).agg({'pct_alloc': 'sum'}).reset_index())
    return curr_alloc_df

