from forex_python.converter import CurrencyRates
from datetime import datetime
import tkinter

now = datetime.now()
c = CurrencyRates()

window = tkinter.Tk()
window.title("X-Change")
window.minsize(500, 300)


# some_day = datetime(2018, 9, 11)

# print(c.get_rate('GBP', 'HUF', some_day))


# from_currency = input("Which currency would you like to exchange?: ")
# to_currency = input("Which currency would you like to get?: ")
# amount = float(input("What is the amount?: "))


def converter(from_curr, to_curr, money):
    converted = c.convert(from_curr, to_curr, money)
    return converted


my_label = tkinter.Label(text="YaDDA YADDA", font=("Courier", 18, "bold"))
my_label.pack(side="left")

window.mainloop()
