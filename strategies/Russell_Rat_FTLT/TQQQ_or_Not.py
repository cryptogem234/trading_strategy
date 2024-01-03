import pandas as pd

def tqqq_or_not(df):

    if df['RSI_10'][df['ticker']=='TQQQ'].values[0] > 79:
        alloc_tkr = 'UVXY'

    else:
        if df['CUMR_6'][df['ticker'] == 'TQQQ'].values[0] < -0.13:
            if df['CUMR_1'][df['ticker'] == 'TQQQ'].values[0] > 0.06:
                alloc_tkr = 'UVXY'

            else:
                if df['RSI_10'][df['ticker'] == 'TQQQ'].values[0] < 32:
                    alloc_tkr = 'TQQQ'

                else:
                    if df['MDD_10'][df['ticker'] == 'TMF'].values[0] < 0.07:
                        alloc_tkr = 'TQQQ'

                    else:
                        alloc_tkr = 'BIL'

        else:
            if df['MDD_10'][df['ticker'] == 'QQQ'].values[0] > 0.06:
                alloc_tkr = 'BIL'

            else:
                if df['MDD_10'][df['ticker'] == 'TMF'].values[0] > 0.07:
                    alloc_tkr = 'BIL'

                else:
                    if df['close'][df['ticker'] == 'QQQ'].values[0] > df['SMA_25'][df['ticker'] == 'QQQ'].values[0]:
                        alloc_tkr = 'TQQQ'

                    else:
                        if df['RSI_60'][df['ticker'] == 'SPY'].values[0] > 50:
                            if  df['RSI_45'][df['ticker'] == 'BND'].values[0] > df['RSI_45'][df['ticker'] == 'SPY'].values[0]:
                                alloc_tkr = 'TQQQ'

                            else:
                                alloc_tkr = 'BIL'

                        else:
                            if df['RSI_200'][df['ticker'] == 'IEF'].values[0] < df['RSI_200'][df['ticker'] == 'TLT'].values[0]:
                                if df['RSI_45'][df['ticker'] == 'BND'].values[0] > df['RSI_45'][df['ticker'] == 'SPY'].values[0]:
                                    alloc_tkr = 'TQQQ'

                                else:
                                    alloc_tkr = 'BIL'

                            else:
                                alloc_tkr = 'BIL'

    return alloc_tkr