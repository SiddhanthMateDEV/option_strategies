from validate_variables.main import validator
from csv_reader.main import csv_reader 
import numpy as np
import gc

class atr(validator, csv_reader):
    def __init__(self,
                file = None,
                n_slow_atr = None,
                n_fast_atr = None,
                n_tma = None,
                ):
        
        self.n_slow_atr = n_slow_atr
        self.n_fast_atr = n_fast_atr
        self.n_tma = n_tma
        self.validate()
        csv_reader.__init__(file)

    def display_attr(self):
        if (self.n_slow_atr and self.n_fast_atr and self.n_tma):
            print(f"Larger ATR Timeframe: {self.n_slow_atr}")
            print(f"Smaller ATR Timeframe: {self.n_fast_atr}")
            print(f"Breakout Window Timeframe: {self.n_tma}")


    def calculations(self):
        previous_close = None
        
        # Pre-Calculations
        for entry in self.data_dictionary:
            entry['high_low'] = entry['High'] - entry['Low']
            entry['high_prev_close'] = np.abs(entry['High'] - previous_close) if previous_close is not None else None
            entry['low_prev_close'] = np.abs(entry['Low'] - previous_close) if previous_close is not None else None
            entry['true_range'] = np.maximum.reduce([entry['high_low'],entry['high_prev_close'],entry['low_prev_close']]) 
            previous_close = entry['Close']
        
        
        del previous_close
        gc.collect()

    

        

class dma(validator, csv_reader):
    def __init__(self,
                file = None,
                n_udma = None,
                n_ldma = None,
                n_udma_percent = None,
                n_ldma_percent = None,
                n_tma_dma = None,
                n_signal = None,
                n_trend_filter = None,
                ):
        
        self.n_udma = n_udma
        self.n_udma_percent = n_udma_percent
        self.n_ldma = n_ldma
        self.n_ldma_percent = n_ldma_percent
        self.n_tma_dma = n_tma_dma
        self.n_signal = n_signal
        self.n_trend_filter = n_trend_filter
        self.validate()
        csv_reader.__init__(file)

    def display_attr(self):
        if (self.n_udma and self.n_ldma and self.n_tma and self.n_signal and self.n_trend_filter):
            print(f"Upper Band Timeframe: {self.n_udma}")
            print(f"Lower Band Timeframe: {self.n_ldma}")
            print(f"Upper Band Timeframe Percent: {self.n_udma_percent}")
            print(f"Lower Band Timeframe Percent: {self.n_ldma_percent}")
            print(f"TMA Timeframe: {self.n_tma_dma}")
            print(f"Signal Timeframe: {self.n_signal}")
            print(f"Trend Filter Timeframe: {self.n_trend_filter}")


class macd(validator,csv_reader):
    def __init__(self,
                file = None,
                n_slow_ema = None,
                n_fast_ema = None,
                n_ema_variable = None,
                n_signal_line = None
                ):
        self.n_slow_ema = n_slow_ema
        self.n_fast_ema = n_fast_ema
        self.n_ema_variable = n_ema_variable
        self.n_signal_line = n_signal_line
        self.validate()
        csv_reader.__init__(file)

    def display_attr(self):
        if (self.n_slow_ema and self.n_fast_ema and self.n_ema_variable and self.n_singal_line):
            print(f"Slow EMA Band Timeframe: {self.n_slow_ema}")
            print(f"Fast EMA Band Timeframe: {self.n_fast_ema}")
            print(f"EMA Variable: {self.n_ema_variable}")
            print(f"Signal Line Timframe: {self.n_signal_line}")

