class ExchangeRate:
    def __init__(self, currencyFrom: object, currencyTo: object, rate: float):
        self.rate = rate
        self.currencyFrom = currencyFrom
        self.currencyTo = currencyTo

    def change_rate(self, new_rate):
        self.rate = new_rate
        
