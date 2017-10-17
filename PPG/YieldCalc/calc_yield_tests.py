import unittest
import datetime as dt
import decimal as dec
import calc_yield as c_y


class CalcYieldTests(unittest.TestCase):

    def test_1(self):
        result = c_y.calc_yield( dt.date(2017, 1, 1), 
                            dec.Decimal("1000.1"),
                            dt.date(2017,1, 30), 
                            dec.Decimal("1100.2"))
        
        self.assertTrue ( 1.1 < result and result < 1.3)

    def test_2(self):
        result =  c_y.calc_yield_per_dollar_day( dt.date(2017, 1, 1), 
                dec.Decimal("1000.1"),
                dt.date(2017,1, 30), 
                dec.Decimal("1100.2"))
        self.assertTrue ( 1.1 < result and result < 1.3)





if __name__ == '__main__':
    unittest.main()