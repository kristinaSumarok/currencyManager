from ExchangeRate import ExchangeRate;
from Currency import Currency;

class CurrencyManager:
    def __init__(self, base_currency: Currency):
        self.base_currency = base_currency
        self.currencies = [base_currency]
        self.exchange_rates = []

    def add_currency(self, new_currency: Currency):
        if any(currency.code == new_currency.code for currency in self.currencies):
            raise ValueError(f"Currency with code {new_currency.code} ({new_currency.name}) already exists.")
        else:
            self.currencies.append(new_currency)
            print(f"Currency {new_currency.name} ({new_currency.code}) added successfully.")

    def add_exchange_rate(self, to_currency_code: str, rate: float):
        to_currency = next((currency for currency in self.currencies if currency.code == to_currency_code), None)
    
        if to_currency is None:
            raise ValueError(f"Currency with code {to_currency_code} not found in the list of available currencies.")

        for existing_rate in self.exchange_rates:
            if (existing_rate.currencyFrom == self.base_currency and existing_rate.currencyTo == to_currency):
                raise ValueError(f"Exchange rate from {self.base_currency.code} to {to_currency.code} already exists.")

        exchange_rate = ExchangeRate(self.base_currency, to_currency, rate)
        self.exchange_rates.append(exchange_rate)
    
    def get_exchange_rate(self, from_currency_code: str, to_currency_code: str) -> float:
        if from_currency_code == to_currency_code:
            print("No conversion needed.")
            return 1.0

        elif from_currency_code == self.base_currency.code:
            for rate in self.exchange_rates:
                if rate.currencyTo.code == to_currency_code:
                    return rate.rate
            raise ValueError(f"Exchange rate not found from {self.base_currency.code} to {to_currency_code}.")
        
        elif to_currency_code == self.base_currency.code:
            for rate in self.exchange_rates:
                if rate.currencyTo.code == from_currency_code:
                    return 1 / rate.rate
            raise ValueError(f"Exchange rate not found from {self.base_currency.code} to {to_currency_code}.")

        rate_to_base = self.get_exchange_rate(from_currency_code, self.base_currency.code)
        rate_from_base = self.get_exchange_rate(self.base_currency.code, to_currency_code)
        return rate_to_base * rate_from_base

    def change_exchange_rate(self, to_currency_code: str, new_rate: float):
        for rate in self.exchange_rates:
            if rate.currencyTo.code == to_currency_code:
                rate.change_rate(new_rate)
                return
        raise ValueError(f"Exchange rate for currency {to_currency_code} not found.")

    def has_exchange_rate(self, from_currency_code: str, to_currency_code: str) -> bool:
        try:
            self.get_exchange_rate(from_currency_code, to_currency_code)
            return True
        except ValueError:
            return False
    
    def get_exchange_rate_table(self, target_currency_code: str) -> str:
        target_currency = next((cur for cur in self.currencies if cur.code == target_currency_code), None)
        if target_currency is None:
            raise ValueError(f"Currency with code {target_currency_code} not found.")

        html_table = "<table><tr><th>From</th><th>To</th><th>Rate</th></tr>"
        
        for currency in self.currencies:
            if currency.code != target_currency_code:
                if self.has_exchange_rate(target_currency_code, currency.code):
                    rate_from_target = self.get_exchange_rate(target_currency_code, currency.code)
                    html_table += f"<tr><td>{target_currency_code}</td><td>{currency.code}</td><td>{rate_from_target:.4f}</td></tr>"
        
        html_table += "</table>"
        return html_table
