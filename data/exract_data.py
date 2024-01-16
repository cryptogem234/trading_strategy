import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"

import pandas as pd

import yfinance as yf

def get_hist_data(sym_list, hist_period):

    stock_hist_data_df = pd.DataFrame()
    for i in sym_list:
        try:
            df = yf.download(i, period = hist_period)
            df = df.reset_index()
            df.columns = map(str.lower, df.columns)
            df = df.drop(['close'], axis=1)
            df = df.rename(columns={'adj close': 'close'})
            df = df.sort_values(by=['date'], ascending=True)
            df['ticker'] = i
            stock_hist_data_df = pd.concat([stock_hist_data_df, df], ignore_index=True)
        except Exception as e:
            print(f"Error processing {i}: {e}")
    return stock_hist_data_df

