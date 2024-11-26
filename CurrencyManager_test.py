import math
import unittest
from CurrencyManager import CurrencyManager
from Currency import Currency
from ExchangeRate import ExchangeRate

class TestCurrencyManager(unittest.TestCase):

    def setUp(self):
        self.eur = Currency("EUR","Euro")
        self.dollar = Currency("USD","Dollar")
        self.jpy = Currency("JPY","Japanese Yen")
        
        self.manager = CurrencyManager(self.eur)


    def test_add_currency(self):
        self.manager.add_currency(self.dollar)
        self.manager.add_currency(self.jpy)

        self.assertEqual(self.jpy,self.manager.currencies[2])
        self.assertEqual(self.dollar,self.manager.currencies[1])
        self.assertEqual(self.manager.base_currency,self.manager.currencies[0])

    def test_add_currency_same(self):
        self.manager.add_currency(self.dollar)
        with self.assertRaises(ValueError):
            self.manager.add_currency(self.dollar)

    def test_add_exchage_rate(self):
        self.manager.add_currency(self.dollar)
        self.manager.add_exchange_rate("USD", 1.08)
        
        self.assertEqual(self.dollar,self.manager.exchange_rates[0].currencyTo)
        self.assertEqual(self.eur,self.manager.exchange_rates[0].currencyFrom)
        self.assertEqual(1.08,self.manager.exchange_rates[0].rate)

    def test_add_exchange_rate_same(self):
        self.manager.add_currency(self.dollar)
        self.manager.add_exchange_rate("USD", 1.08)
        with self.assertRaises(ValueError):
            self.manager.add_exchange_rate("USD", 1.08)

    def test_add_exchange_rate_noCurrency(self):
        with self.assertRaises(ValueError):
            self.manager.add_exchange_rate("USD", 1.08)

    def test_get_exchange_rate(self):
        self.manager.add_currency(self.dollar)
        self.manager.add_currency(self.jpy)
        self.manager.add_exchange_rate("USD", 1.08)
        self.manager.add_exchange_rate("JPY", 165.12)
        #regular calculation
        self.assertAlmostEqual(152.89,self.manager.get_exchange_rate("USD","JPY"),1)
        #revert calculation = 1/rate
        self.assertAlmostEqual(0.92,self.manager.get_exchange_rate("USD","EUR"),1)
        #same currency rate = 1
        self.assertEqual(1,self.manager.get_exchange_rate("EUR","EUR"))

    def test_get_exchange_rate_noExchangeRate(self):
        with self.assertRaises(ValueError):
            self.manager.get_exchange_rate("USD","JPY")

        with self.assertRaises(ValueError):
            self.manager.get_exchange_rate("USD","EUR")
            
    def test_change_exchange_rate(self):
        self.manager.add_currency(self.dollar)
        self.manager.add_exchange_rate("USD", 1.08)
        self.manager.change_exchange_rate("USD", 1.03)

        self.assertEqual(1.03,self.manager.exchange_rates[0].rate)

    def test_change_exchange_rate_noExchangeRate(self):
        with self.assertRaises(ValueError):
            self.manager.change_exchange_rate("USD", 1.03)


        
if __name__ == "__main__":
    unittest.main()
