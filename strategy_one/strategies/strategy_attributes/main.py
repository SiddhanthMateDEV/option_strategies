class atr:
    def __init__(self,
                n_slow_atr = None,
                n_fast_atr = None,
                n_tma = None,
                ):
        
        self.n_slow_atr = n_slow_atr
        self.n_fast_atr = n_fast_atr
        self.n_tma = n_tma

        def display_attr(self):
            if (self.n_slow_atr and self.n_fast_atr and self.n_tma):
                print(f"Larger ATR Timeframe: {self.n_slow_atr}")
                print(f"Smaller ATR Timeframe: {self.n_fast_atr}")
                print(f"Breakout Window Timeframe: {self.tsl}")

class dma:
    def __init__(self,
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


        def display_attr(self):
            if (self.n_udma and self.n_ldma and self.n_tma and self.n_signal and self.n_trend_filter):
                print(f"Upper Band Timeframe: {self.n_udma}")
                print(f"Lower Band Timeframe: {self.n_ldma}")
                print(f"Upper Band Timeframe Percent: {self.n_udma_percent}")
                print(f"Lower Band Timeframe Percent: {self.n_ldma_percent}")
                print(f"TMA Timeframe: {self.n_tma_dma}")
