import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"

import pandas as pd

import yfinance as yf


def get_hist_data(sym_list, start_date, end_date):

    stock_hist_data_df = pd.DataFrame()
    for i in sym_list:
        try:
            df = yf.download(i, start=start_date, end=end_date)
            df = df.reset_index()
            df.columns = map(str.lower, df.columns)
            df = df.drop(['close'], axis=1)
            df = df.rename(columns={'adj close': 'close'})
            df.sort_values(by=['date'])
            df['ticker'] = i
            stock_hist_data_df = stock_hist_data_df.append(df)
        except:
            print(i)
    return stock_hist_data_df

