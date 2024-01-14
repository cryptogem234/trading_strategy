from datetime import datetime, timedelta

strategy_name = 'RAT FTLT Banks, Small Cap, Russell, HealthCare, Real Estate, High Beta, Foreign'
tkr = ['SPY', 'SHY', 'TMF', 'IEF', 'IWM', 'UVXY', 'TQQQ', 'BIL', 'QQQ', 'BND', 'TLT']
bank_tkr = ['FAS', 'FAZ']
house_tkr = ['DRN', 'DRV']
smallcap_tkr = ['TNA', 'TZA']
lab_tkr = ['LABU', 'LABD']
russell_tkr = ['URTY', 'SRTY']
beta_tkr = ['HIBL', 'HIBS']
foreign_tkr = ['EDC', 'EDZ']
sym_list = tkr + bank_tkr + house_tkr + smallcap_tkr + lab_tkr + russell_tkr + beta_tkr + foreign_tkr
sym_list = list(set(sym_list))

end_date = datetime.today()
start_date = end_date - timedelta(days=1000)
hist_days_list = [1, 5, 6, 10, 11, 14, 16, 25, 45, 60, 200, 600]