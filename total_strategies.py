import pandas as pd

from strategies.TQQQ_or_not_UVXY_w_SOXS import strategy as tqqq_or_not
#from strategies.Nothing_But_Bonds import strategy as nothing_but_bonds
#from strategies.Russell_Rat_FTLT import strategy as russell_rat_ftlt


def execute_all_strategies():
    tqqq_or_not_strategy = tqqq_or_not.execute_strategy()
    # nothing_but_bonds_strategy = nothing_but_bonds.execute_strategy()
    # russell_rat_ftlt_strategy = russell_rat_ftlt.execute_strategy()

    #total_strategy_summary = pd.concat([tqqq_or_not_strategy,russell_rat_ftlt_strategy], axis=0)

    return  tqqq_or_not_strategy