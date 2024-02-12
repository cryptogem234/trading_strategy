
from strategies.TQQQ_or_not_UVXY_w_SOXS import strategy as tqqq_or_not
from strategies.RAT_FTLT import strategy as rat_ftlt
from strategies.Nothing_But_Bonds import strategy as nothing_but_bonds
from strategies.Short_Vol_w_SVXY_SVXY_FTLT import strategy as short_volatility_svxy
from strategies.WAM_FTLT_w_TMF import strategy as wam_ftlt
from strategies.Holy_Grail_Simplified_RSI_Divination_wo_VIXen import strategy as holy_grail
from strategies.Simple_20d_BND_vs_60d_SH import strategy as bnd_20d_sh_60d
from strategies.Medium_Time_Frame_Switches import strategy as medium_time_frame_switches
from strategies.Short_Volatility import strategy as short_volatility

def execute_tqqq_or_not_strategy():
    tqqq_or_not_strategy = tqqq_or_not.execute_strategy()
    return  tqqq_or_not_strategy

def execute_rat_ftlt_strategy():
    rat_ftlt_strategy = rat_ftlt.execute_strategy()
    return  rat_ftlt_strategy

def execute_nothing_but_bonds_strategy():
    nothing_but_bonds_strategy = nothing_but_bonds.execute_strategy()
    return nothing_but_bonds_strategy

def execute_short_volatility_svxy_strategy():
    short_volatility_svxy_strategy = short_volatility_svxy.execute_strategy()
    return short_volatility_svxy_strategy

def execute_wam_ftlt_strategy():
    wam_ftlt_strategy = wam_ftlt.execute_strategy()
    return wam_ftlt_strategy

def execute_holy_grail_strategy():
    holy_grail_strategy = holy_grail.execute_strategy()
    return holy_grail_strategy

def execute_bnd_20d_sh_60d_strategy():
    bnd_20d_sh_60d_strategy = bnd_20d_sh_60d.execute_strategy()
    return bnd_20d_sh_60d_strategy

def execute_medium_time_frame_switches_strategy():
    medium_time_frame_switches_strategy = medium_time_frame_switches.execute_strategy()
    return medium_time_frame_switches_strategy

def execute_short_volatility_strategy():
    short_volatility_strategy = short_volatility.execute_strategy()
    return short_volatility_strategy