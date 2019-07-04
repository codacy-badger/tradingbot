import math

mts = 0
open = 1
close = 2
high = 3
low = 4
volume = 5
short = -1
long = 1
value = 2000
fee = 0
actual_time = 20

class StrategyInfo:
    def __init__(self):
        self.min_value = inf
        self.max_value =  0
        self.last_trade = False
        self.stop = None
    def reset(strategy_info):
        strategy_info.min_value = inf
        strategy_info.max_value = 0


class Trade:
    def __init__(self,amount,fee):
        self.entry = None
        self.exit = None
        self.amount = amount
        self.fee = fee / 100
        self.type = None
    def calculate_profit(trade):
        return (((trade.exit / trade.entry) * trade.amount) - trade.amount) * trade.type - (trade.amount * (trade.fee))
    def restart_values(self):
        self.entry = None
        self.exit = None
        self.amount = amount
        self.fee = fee / 100
        self.type = None

def init_info(candles,actual_time,strategy_info):    # vezme poslednich 20 candles a extrahuje potrebne info do objektu
    for i in range(20):
        if candles[actual_time - 20 + i][high] > strategy_info.max_value:
            strategy_info.max_value = candles[actual_time + i][high]
        if candles[actual_time - 20 + i][low] < strategy_info.min_value:
            strategy_info.min_value = candles[actual_time + i][low]

def check_trade(actual_candle,strategy_info,trade): # ocheckuje jestli je uz nejaky trade otevreny a podle toho se zachova
    if trade.entry is None:                         # bud ho zavre nebo necha dal probihat
        return
    if trade.type == long:
        if actual_candle[low] < strategy_info.min_value:
            trade.exit = strategy_info.min_value
    elif trade.type == short:
        if actual_candle[high] < strategy_info.max_value:
            trade.exit = strategy_info.max_value


def new_trade(actual_candle,strategy_info,trade):   # pokud neni otevreny trade, otevre novy pri splneni podminek
    if trade.entry is not None:
        return
    if actual_candle[low] < strategy_info.min_value:
        trade.entry = strategy_info.min_value
    if actual_candle[high] < strategy_info.max_value:
        trade.exit = strategy_info.max_value

def evaluate(trade,trade_array):   # pokud je po minulych funkcich dokonceny trade, tak ho prida do seznamu
    if trade.entry and trade.exit:
        closed_trade = copy.deepcopy(trade)
        trade_array.append(closed_trade)
        trade.restart_values()


def turtle_strategy(candles,actual_time,strategy_info):
    trade_array = []
    trade = Trade(value,fee)
    while actual_time < len(candles):
        strategy_info.reset(strategy_info)
        init_info(candles,actual_time,strategy_info)
        actual_candle = candles[actual_time]
        check_trade(actual_candle,strategy_info,trade)
        evaluate(trade,trade_array)
        new_trade(actual_candle, strategy_info, trade)
        actual_time = actual_time + 1