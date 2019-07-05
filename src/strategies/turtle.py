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
        self.atr = None
    def reset(self):
        self.min_value = inf
        self.max_value = 0
        self.atr = None


class Trade:
    def __init__(self,amount,fee):
        self.entry = None
        self.exit = None
        self.stop = None
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
class Eval:
    def __init__(self):
        self.trade_list = []
        self.profit = 0
    def print_results(self):
        for i in range(len(self.trade_list)):
            print("Vstupni cena:", self.trade_list[i].entry, "Vystupni cena:",self.trade_list[i].exit)
            print("Profit:", self.trade_list[i].calculate_profit())
            self.profit = self.profit + self.trade_list[i].calculate_profit()
        print("Konecna bilance:", self.profit)
        print("Pocet tradu:", len(self.trade_

def init_info(candles,actual_time,strategy_info):    # vezme poslednich 20 candles a extrahuje potrebne info do objektu
    for i in range(20):
        if candles[actual_time - 20 + i][high] > strategy_info.max_value:
            strategy_info.max_value = candles[actual_time + i][high]
        if candles[actual_time - 20 + i][low] < strategy_info.min_value:
            strategy_info.min_value = candles[actual_time + i][low]

def calculate_atr(candles, actual_time, strategy_info):  # vypocita ukazatel ohledne volatility
    atr = []
    for i in range(20):
        f_value = candles[actual_time - 20 + i][high] - candles[actual_time - 21 + i][close]
        s_value = candles[actual_time - 20 + i][low] - candles[actual_time - 21 + i][close]
        t_value = candles[actual_time - 20 + i][high] - candles[actual_time - 20 + i][close]
        atr.append(max(abs(f_value),abs(s_value),abs(t_value)))
    strategy_info.atr = statistics.mean(atr)

def check_trade(actual_candle,strategy_info,trade): # ocheckuje jestli je uz nejaky trade otevreny a podle toho se zachova
    if trade.entry is None:                         # bud ho zavre nebo necha dal probihat
        return
    if trade.type == long:
        if actual_candle[low] < strategy_info.min_value:
            trade.exit = strategy_info.min_value
        elif trade.stop > actual_candle[low]:
            trade.exit = trade.entry - strategy_info.atr
    elif trade.type == short:
        if actual_candle[high] < strategy_info.max_value:
            trade.exit = strategy_info.max_value
        elif trade.entry + strategy_info.atr < actual_candle[high]:
            trade.exit = trade.entry + strategy_info.atr


def new_trade(actual_candle,strategy_info,trade):   # pokud neni otevreny trade, otevre novy pri splneni podminek
    if trade.entry is not None:
        return
    if actual_candle[low] < strategy_info.min_value:
        trade.entry = strategy_info.min_value
        trade.type = short
        trade.stop = trade.entry + ( 2* strategy_info.min_value)
    if actual_candle[high] < strategy_info.max_value:
        trade.exit = strategy_info.max_value
        trade.type = long
        trade.stop = trade.entry - (2 * strategy_info.min_value)

def evaluate(trade,eval,strategy_info):   # pokud je po minulych funkcich dokonceny trade, tak ho prida do seznamu
    if trade.entry and trade.exit:
        closed_trade = copy.deepcopy(trade)
        if strategy_info.last_trade == False:
            eval.trade_list.append(closed_trade)
        if ((trade.exit - trade.entry) * trade.type) > 0 :
            strategy_info.last_trade = True
        else (trade.exit - trade.entry) * trade.type:
            strategy_info.last_trade = False
        trade.restart_values()


def turtle_strategy(candles,actual_time,strategy_info):
    eval = Eval()
    trade = Trade(value,fee)
    while actual_time < len(candles):
        strategy_info.reset(strategy_info)
        init_info(candles,actual_time,strategy_info)
        calculate_atr(candles, actual_time, strategy_info)
        actual_candle = candles[actual_time]
        check_trade(actual_candle,strategy_info,trade)
        evaluate(trade,trade_array,strategy_info)
        new_trade(actual_candle, strategy_info, trade)
        actual_time = actual_time + 1
    eval.print_results()
