from forex_python.converter import CurrencyRates
from datetime import datetime
from tkinter import *

now = datetime.now()
c = CurrencyRates()

window = Tk()
window.title("X-Change")
window.minsize(500, 300)
# window.iconbitmap("icon path here")

# some_day = datetime(2018, 9, 11)
# print(c.get_rate('GBP', 'HUF', some_day))
# from_currency = input("Which currency would you like to exchange?: ")
# to_currency = input("Which currency would you like to get?: ")
# amount = float(input("What is the amount?: "))


def converter(from_curr, to_curr, money):
    converted = c.convert(from_curr, to_curr, money)
    return converted


my_label = Label(text="Currency Converter", font=("Courier", 18, "bold"))
my_label.pack()

currency_options = [
    "GBP",
    "USD",
    "HUF",
    "EUR"
]

clicked = StringVar()
clicked.set("Choose a Currency")
drop = OptionMenu(window, clicked, *currency_options)
drop.pack()

myButton = Button(window, text="What what", command="converter")
myButton.pack()

window.mainloop()
