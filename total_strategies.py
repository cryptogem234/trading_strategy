
from strategies.TQQQ_or_not_UVXY_w_SOXS import strategy as tqqq_or_not
from strategies.Russell_Rat_FTLT import strategy as russell_rat_ftlt


def execute_tqqq_or_not_strategy():
    tqqq_or_not_strategy = tqqq_or_not.execute_strategy()
    return  tqqq_or_not_strategy

def execute_russell_rat_ftlt_strategy():
    russell_rat_ftlt_strategy = russell_rat_ftlt.execute_strategy()
    return  russell_rat_ftlt_strategy