from Currency import Currency
from CurrencyManager import CurrencyManager

class Money:
    def __init__(self, amount : float, currency: Currency):
        self.amount = amount
        self.currency = currency

    def add_money(self, add_amount:float):
        if add_amount>0:
            self.amount += add_amount
        else:
            raise ValueError('Amount must be positive.')

    def subtract_money(self, take_amount: float):
        if take_amount>0 & take_amount <= self.amount:
            self.amount -= take_amount
        elif take_amount > self.amount:
             raise ValueError(f"Cannot subtract {take_amount} {self.currency.code}, current balance is {self.amount}.")
        elif take_amount<0:
             raise ValueError(f"Cannot subtract {take_amount} {self.currency.code}, amount must be positive.")
            
    def convert_to(self, target_currency: Currency, manager: CurrencyManager):
        rate = manager.get_exchange_rate(self.currency.code, target_currency.code)
        self.amount *= rate 
        self.currency = target_currency
