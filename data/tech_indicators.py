import pandas as pd
import numpy as np

def get_technical_data(sym_list, stock_hist_data_df, hist_days_list):

    stock_tech_full_data = pd.DataFrame()
    stock_tech_summ_data = pd.DataFrame()
    for i in sym_list:
        try:
            df = stock_hist_data_df.copy()
            df = df[df['ticker'] == i]
            df.columns = map(str.lower, df.columns)
            df = df.sort_values(by=['date'], ascending=True)
            df['PCTRET'] = df['close'].pct_change()
            df['change'] = df['close'].diff()
            df['gain'] = df.change.mask(df.change < 0, 0.0)
            df['loss'] = -df.change.mask(df.change > 0, -0.0)

            for i in hist_days_list:
                df['avg_gain' + str(i)] = df['gain'].ewm(alpha=1 / i).mean()
                df['avg_loss' + str(i)] = df['loss'].ewm(alpha=1 / i).mean()
                df['RSI_' + str(i)] = 100 - (100 / (1 + df['avg_gain' + str(i)] / df['avg_loss' + str(i)]))
                df = df.drop(['avg_gain' + str(i), 'avg_loss' + str(i)], axis=1)

                df['EMA_' + str(i)] = df['close'].ewm(span=i, adjust=False).mean()
                df['SMA_' + str(i)] = df['close'].rolling(window=i).mean()
                df['SMR_' + str(i)] = df['PCTRET'].rolling(window=i).mean()
                df['CUMR_' + str(i)] = np.exp(np.log(df['PCTRET'] + 1).rolling(i).sum()) - 1
                df['STDP_' + str(i)] = df['close'].rolling(window=i).std()
                df['STDR_' + str(i)] = df['PCTRET'].rolling(window=i).std()
                df['MDD_' + str(i)] = -1 * (
                            (df.tail(i).close - df.tail(i).close.cummax()) / df.tail(i).close.cummax()).min()


            stock_tech_full_data = pd.concat([stock_tech_full_data, df], axis=0)

            df = df.tail(1)

            stock_tech_summ_data = pd.concat([stock_tech_summ_data, df], axis=0)
        except Exception as e:
            print(f"Error processing {i}: {e}")

    return stock_tech_full_data, stock_tech_summ_data




