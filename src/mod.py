import datetime
import calendar
import jpbizday
from typing import Tuple

def search_workhours(year, month):
    pass

def get_days_monthly(date_:datetime.date) -> Tuple[int]:
    bizdates = jpbizday.month_bizdays(date_.year, date_.month)
    for i, bizdate in enumerate(bizdates):
        return i, len(bizdates)-i
    
if __name__ == "__main__":
    import unittest
    
    class TestMyFunction(unittest.TestCase):
        def test_1(self):
            date_ = datetime.date(2022, 3, 1)
            self.assertEqual(get_days_monthly(date_), (0, 22))
    
    unittest.main()