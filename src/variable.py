from typing import Tuple


class Time():
    def __init__(self, hour:int, minute:int) -> None:
        self.hour = hour
        if (minute < 0) | (minute > 60):
            error = "minute {} not in range 0 to 60".format(minute)
            raise ValueError(error)
        self.minute = minute
    
    def __repr__(self) -> str:
        return "Time({}, {})".format(self.hour, self.minute)
    
    def __str__(self) -> str:
        return "{}:{:02}".format(self.hour, self.minute)
    
    def __eq__(self, __o:object) -> bool:
        if __o is None:
            return False
        return (self.hour == __o.hour) and (self.minute == __o.minute)
    
    def __ne__(self, __o:object) -> bool:
        return not(self == __o)
    
    @staticmethod
    def time2minute(time:object) -> int:
        return time.hour*60 + time.minute
    
    @staticmethod
    def minute2time(minute:int) -> object:
        hour = minute // 60
        minute = minute - hour*60
        
        return Time(hour, minute)
    
    def __ge__(self, __o:object) -> bool:
        diff = self.time2minute(self) - self.time2minute(__o)
        return (diff >= 0)
    
    def __gt__(self, __o:object) -> bool:
        diff = self.time2minute(self) - self.time2minute(__o)
        return (diff > 0)
    
    def __le__(self, __o:object) -> bool:
        diff = self.time2minute(self) - self.time2minute(__o)
        return (diff <= 0)
    
    def __lt__(self, __o:object) -> bool:
        diff = self.time2minute(self) - self.time2minute(__o)
        return (diff < 0)
    
    def __add__(self, __o:object) -> object:
        total = self.time2minute(self) + self.time2minute(__o)
        return self.minute2time(total)
    
    def __sub__(self, __o:object) -> object:
        diff = self.time2minute(self) - self.time2minute(__o)
        if diff < 0:
            error = "{} is less than {}".format(self.__repr__(), __o.__repr__())
            return ValueError(error)
        return self.minute2time(diff)
    
    def __mul__(self, num:int) -> object:
        total = self.time2minute(self) * num
        return self.minute2time(total)
    
    def __truediv__(self, num:int) -> object:
        total = self.time2minute(self) // num
        return self.minute2time(total)
    
    @staticmethod
    def str2int(time_string:str) -> Tuple[int, int]:
        hhh, mm = tuple(map(int, time_string.split(":")))
        return hhh, mm
    
    @staticmethod
    def str2time(time_string:str) -> object:
        hhh, mm = tuple(map(int, time_string.split(":")))
        return Time(hhh, mm)
        
    
if __name__ == "__main__":
    import unittest
    
    class TestTimeClass(unittest.TestCase):
        def test_add(self):
            t1 = Time(3, 20)
            t2 = Time(3, 50)
            self.assertEqual(t1+t2, Time(7, 10))
        def test_sub(self):
            t1 = Time(3, 50)
            t2 = Time(3, 10)
            self.assertEqual(t1-t2, Time(0, 40))
    
    unittest.main()