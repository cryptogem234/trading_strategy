from datetime import datetime, timedelta


strategy_name = 'Short Vol with SVXY | SVXY FTLT'
sym_list = ['SVXY', 'UVXY', 'VIXY', 'XLK', 'SPY', 'SHV', 'QQQ']
sym_list = list(set(sym_list))
end_date = datetime.today()
start_date = end_date - timedelta(days=1000)
hist_days_list = [1 , 5, 10, 14, 20, 21]