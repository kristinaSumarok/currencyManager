from Currency import Currency
from CurrencyManager import CurrencyManager
from Money import Money

def main():
    eur = Currency("EUR","Euro")
    usd = Currency("USD", "Dollar")
    jpy = Currency("JPY", "Japanese yen")

    manager = CurrencyManager(eur)
    money = Money(100,eur)
    
    manager.add_currency(usd)
    manager.add_currency(jpy)
    manager.add_exchange_rate("USD",1.08)
    manager.add_exchange_rate("JPY",165.79)
    print(manager.get_exchange_rate_table("USD"))

    manager.change_exchange_rate("USD", 1.10)
    print(manager.get_exchange_rate_table("EUR"))

    money.add_money(25)
    money.subtract_money(50)
    money.convert_to(usd,manager)
    print(money.amount)
    print(money.currency.name)

if __name__ == "__main__":
    main()
