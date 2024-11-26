import math
import unittest
from CurrencyManager import CurrencyManager
from Currency import Currency
from Money import Money

class TestMoney(unittest.TestCase):

    def setUp(self):
        self.eur = Currency("EUR","Euro")
        self.dollar = Currency("USD","Dollar")
        self.jpy = Currency("JPY","Japanese Yen")
        self.money = Money(100,self.eur)
        
        self.manager = CurrencyManager(self.eur)


    def test_add_money(self):
        self.money.add_money(50)
        self.assertEqual(150,self.money.amount)
        
        self.money.add_money(20)
        self.assertEqual(170,self.money.amount)

    def test_add_money_negative(self):
        with self.assertRaises(ValueError):
             self.money.add_money(-50)
        
        self.assertEqual(100,self.money.amount)

    def test_subtract_money(self):
        self.money.subtract_money(50)
        self.assertEqual(50,self.money.amount)
        
        self.money.subtract_money(20)
        self.assertEqual(30,self.money.amount)

    def test_subtract_money_negative(self):
        with self.assertRaises(ValueError):
             self.money.subtract_money(-50)
        
        self.assertEqual(100,self.money.amount)

    def test_convert_to(self):
        self.manager.add_currency(self.dollar)
        self.manager.add_currency(self.jpy)
        self.manager.add_exchange_rate("USD", 1.08)
        self.manager.add_exchange_rate("JPY", 165.58)
        self.money.convert_to(self.dollar, self.manager)
        #calculate 1 => eur to usd
        self.assertEqual(108,self.money.amount)
        #calculate 2 => usd to jpy
        self.money.convert_to(self.jpy, self.manager)
        self.assertAlmostEqual(16558,self.money.amount,1)
        #calculate 2 => jpy to eur
        self.money.convert_to(self.eur, self.manager)
        self.assertAlmostEqual(100,self.money.amount,1)

    def test_convert_to_noCurrency(self):
        with self.assertRaises(ValueError):
            self.money.convert_to(self.jpy,self.manager)

if __name__ == "__main__":
    unittest.main()
