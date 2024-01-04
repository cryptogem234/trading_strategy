import pandas as pd

from strategies.TQQQ_or_not_UVXY_w_SOXS import test2 as tqqq_or_not
#from strategies.Nothing_But_Bonds import strategy as nothing_but_bonds
from strategies.Russell_Rat_FTLT import strategy as russell_rat_ftlt


def execute_tqqq_or_not_strategy():
    tqqq_or_not_strategy = tqqq_or_not.execute_strategy()
    return  tqqq_or_not_strategy

def execute_russell_rat_ftlt_strategy():
    russell_rat_ftlt_strategy = russell_rat_ftlt.execute_strategy()
    return  russell_rat_ftlt_strategy