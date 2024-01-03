import pandas as pd
import pandas_ta as ta
from datetime import datetime, timedelta
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import numpy as np

def get_technical_data(sym_list, stock_hist_data_df, hist_days_list):
    stock_tech_hist_data = pd.DataFrame()
    stock_tech_summ_data = pd.DataFrame()
    for i in sym_list:
        try:
            df = stock_hist_data_df.copy()
            df = df[df['ticker'] == i ]
            df.columns = map(str.lower, df.columns)
            df.sort_values(by=['date'], ascending = True)

            for i in hist_days_list:
                df.ta.rsi(length=i, append=True)

            for i in hist_days_list:
                df.ta.ema(length=i, append=True)

            for i in hist_days_list:
                df.ta.sma(length=i, append=True)

            df.ta.percent_return(append=True)

            for i in hist_days_list:
                df['SMR_' + str(i)] = df['PCTRET_1'].rolling(window=i).mean()

            for i in hist_days_list:
                df['CUMR_' + str(i)] = np.exp(np.log(df['PCTRET_1']+1).rolling(i).sum())-1

            for i in hist_days_list:
                df['STDP_' + str(i)] = df['close'].rolling(window=i).std()

            for i in hist_days_list:
                df['MDD_' + str(i)] = -1 * df['close'].rolling(i).apply(lambda s: ((s - s.cummax()) / s.cummax()).min())

            df_summary = df.tail(1)
            stock_tech_summ_data = pd.concat([stock_tech_summ_data, df_summary], ignore_index=True)
        except Exception as e:
            print(f"Error processing {i}: {e}")
    return stock_tech_hist_data, stock_tech_summ_data
