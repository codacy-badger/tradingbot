short = -1
long = 1


class Trade:
    def __init__(self,amount,fee,type):
        self.entry = None
        self.exit = None
        self.amount = amount
        self.fee = fee / 100
        self.type = type

    def calculate_profit(self):
        return (((self.exit / self.entry) * self.amount) - self.amount) * self.type - (self.amount * (self.fee))

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
        print("Pocet tradu:", len(self.trade_list))