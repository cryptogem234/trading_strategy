
from datetime import datetime, timedelta

strategy_name = 'TQQQ OR Not Short Via SOXS'
sym_list = ['TQQQ', 'SOXS', 'SOXL', 'BIL', 'UVXY', 'QQQ', 'TMF', 'SPY', 'BND', 'TLT', 'IEF']
sym_list = list(set(sym_list))
end_date = datetime.today()
start_date = end_date - timedelta(days=300)
hist_days_list = [1, 3, 5, 6, 8, 10, 15, 20, 25, 45, 50, 60, 110, 200]