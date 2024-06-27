import pandas as pd 
import numpy as np
import datetime as datetime

try:
    from csv_reader.main import csv_reader
    from equity_strategies.main import atr, dma, macd
    from trade_attributes.main import trade_attributes
except ImportError as e:
    raise ImportError(f"Error: Could not import a module | {e}")


class equity_strategies(trade_attributes,atr,dma):
    def __init__(self, 
                 sl = None, tsl = None, pb = None, init_cap = None, cp = None, stock = None, start_time = None, new_tick = None, eod_tick = None,
                 n_slow_atr = None ,n_fast_atr = None,n_tma = None,
                 n_udma = None, n_ldma = None, n_udma_percent = None, n_ldma_percent = None, n_tma_dma = None, n_signal = None, n_trend_filter = None,
                 n_slow_ema = None,n_fast_ema = None,n_ema_variable = None,n_signal_line = None):
        
        # Calling all classes into one
        trade_attributes.__init__(sl, tsl, pb, init_cap, cp, stock, start_time, new_tick, eod_tick)
        atr.__init__(n_slow_atr,n_fast_atr,n_tma)
        dma.__init__(n_udma,n_udma_percent,n_ldma,n_ldma_percent,n_tma_dma,n_signal,n_trend_filter)
        macd.__init__(n_slow_ema,n_fast_ema,n_ema_variable,n_signal_line)


        



        

