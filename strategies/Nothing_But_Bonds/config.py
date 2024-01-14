
from datetime import datetime, timedelta


strategy_name = 'Bonds Momentum - IEF, TLT, TMF, TMV Momentums'
sym_list = ['TMF', 'TMV', 'TQQQ', 'BND', 'TLT', 'SHV', 'SHY', 'IEF', 'UBT']
end_date = datetime.today()
start_date = end_date - timedelta(days=1000)
hist_days_list = [1, 3, 5, 8, 10, 15, 20, 21, 50, 60, 110, 200, 350, 450, 550]