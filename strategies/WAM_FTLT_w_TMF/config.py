
strategy_name = 'WAM FTLT w TMF'
sym_list = ['SHY', 'TMF', 'IEF', 'IWM', 'XBI', 'QQQ', 'SPY', 'TQQQ', 'BND', 'TLT', 'LABD', 'SPXS', 'UVXY',
            'UPRO', 'TECL', 'DRN', 'SOXL', 'URTY', 'LABU', 'SPXL', 'PSQ', 'TYO', 'DRV', 'TMV', 'SH']

tqqq_sym_list = ['TQQQ', 'SOXS', 'SOXL', 'BIL', 'UVXY', 'QQQ', 'TMF', 'SPY', 'BND', 'TLT', 'IEF']

sym_list = sym_list + tqqq_sym_list

sym_list = list(set(sym_list))

period = '1000d'
hist_days_list = [1, 4, 6, 10, 11, 14, 16, 25, 45, 60, 200, 575, 600]