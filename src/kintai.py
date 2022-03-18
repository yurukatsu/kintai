import tkinter as tk
from tkinter import ttk
import datetime
import dateutil.relativedelta
import calendar
import jpbizday
from variable import Time
from time_limit import LEGAL_HOURS
from mod import search_workhours
    
class App(tk.Tk):
    def __init__(self, year:int, month:int, hour:int, minute:int):
        super().__init__()
        
        self.year = tk.IntVar(value=year)
        self.month = tk.IntVar(value=month)
        self.hour = tk.IntVar(value=hour)
        self.minute = tk.IntVar(value=minute)

        self.title("勤怠チェックツール")
        # self.resizable(False, False)
        self.geometry("300x300")
        
        self.style = ttk.Style(self)
        
        self.frame1 = ttk.Frame(self, padding=(32))
        self.frame1.grid()
        
        self.label1 = ttk.Label(self.frame1, text="YYYY", padding=(5,2))
        self.label1.grid(row=0, column=0, sticky='E')
        self.entry1 = ttk.Entry(self.frame1, textvariable=self.year, width=20)
        self.entry1.grid(row=0, column=1)
        
        self.label2 = ttk.Label(self.frame1, text="MM", padding=(5,2))
        self.label2.grid(row=1, column=0, sticky='E')
        self.entry2 = ttk.Entry(self.frame1, textvariable=self.month,  width=20)
        self.entry2.grid(row=1, column=1)
        
        self.button2 = ttk.Button(self.frame1, text='Search hhhmm', command=quit)
        self.button2.grid(row=2, column=1)
        
        self.label3 = ttk.Label(self.frame1, text="hhh", padding=(5,2))
        self.label3.grid(row=3, column=0, sticky='E')
        self.entry3 = ttk.Entry(self.frame1, textvariable=self.hour, width=20)
        self.entry3.grid(row=3, column=1)
        
        self.label4 = ttk.Label(self.frame1, text="mm", padding=(5,2))
        self.label4.grid(row=4, column=0, sticky='E')
        self.entry4 = ttk.Entry(self.frame1, textvariable=self.minute, width=20)
        self.entry4.grid(row=4, column=1)
        
        self.frame2 = ttk.Frame(self.frame1, padding=(0, 5))
        self.frame2.grid(row=5, column=1, sticky='W')
        self.button1 = ttk.Button(
            self.frame2, text='Check', command=self.update)
        self.button1.pack(side='left')
        self.button3 = ttk.Button(self.frame2, text='Cancel', command=quit)
        self.button3.pack(side='left')
        
    def update(self):
        workhours = Time(self.hour.get(), self.minute.get())
        bizdays = len(jpbizday.month_bizdays(self.year.get(), self.month.get()))
        days = calendar.monthrange(self.year.get(), self.month.get())[1]
        over_legal_hours = workhours - LEGAL_HOURS[days] if workhours > LEGAL_HOURS[days] else Time(0, 0)
        legal_hours = workhours - over_legal_hours - Time(7, 30) * bizdays
        self.label_output1 = ttk.Label(
            self.frame1, 
            text="法定内残業時間：{}".format(legal_hours), 
            padding=(5,2))
        self.label_output1.grid(row=6, column=1, sticky='W')
        self.label_output2 = ttk.Label(
            self.frame1, 
            text="法定外残業時間:{}".format(over_legal_hours), 
            padding=(5,2))
        self.label_output2.grid(row=7, column=1, sticky='W')
        
    def search(self):
        search_workhours(self.year.get(), self.month.get())
    
if __name__ == '__main__':
    # last month
    last_date = datetime.date.today() + dateutil.relativedelta.relativedelta(months=-1)
    year = last_date.year
    month = last_date.month
    hour = 150
    minute = 20
    app = App(year=year, month=month , hour=hour, minute=minute)
    app.mainloop()