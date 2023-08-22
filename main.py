from forex_python.converter import CurrencyRates
from datetime import datetime
from tkinter import *

now = datetime.now()
c = CurrencyRates()

window = Tk()
window.title("X-Change")
window.minsize(400, 300)
window.resizable(False, False)
# window.iconbitmap("icon path here")

# some_day = datetime(2018, 9, 11)
# print(c.get_rate('GBP', 'HUF', some_day))
# from_currency = input("Which currency would you like to exchange?: ")
# to_currency = input("Which currency would you like to get?: ")
# amount = float(input("What is the amount?: "))


# def converter(from_curr, to_curr, money=1):
#     converted = c.convert(from_curr, to_curr, money)
#     return converted


my_label = Label(text="Currency Converter", font=("Courier", 18, "bold"))
my_label.pack()

currency_options = [
    "GBP",
    "USD",
    "EUR",
    "CHF",
    "AUD",
    "CAD",
    "HUF",
    "JPY",
    "CNY",
    "HKD",
]

start_cur = StringVar()
start_cur.set("Choose a Currency")
start_drop = OptionMenu(window, start_cur, *currency_options)
start_drop.configure(width=18)
start_drop.pack(side="left")


end_cur = StringVar()
end_cur.set("Choose a Currency")
end_drop = OptionMenu(window, end_cur, *currency_options)
end_drop.configure(width=18)
end_drop.pack(side="right")

money_entered = Entry(width=10)
money_entered.pack()


def perform_conversion():
    start_currency = start_cur.get()
    end_currency = end_cur.get()
    money = float(money_entered.get())

    try:
        result = c.get_rate(start_currency, end_currency, now) * money
        # Update the label text with the result
        result_label["text"] = f"{money} {start_currency} = {round(result, 3)} {end_currency}"
    except Exception as e:
        print(f"Error: {e}")
        result_label["text"] = f"Error: {e}"


# def on_click():
#     result_label["text"] = "Python"
#     convert_button["state"] = "disabled"


convert_button = Button(window, text="Convert", command=perform_conversion, height=3, width=10)
convert_button.pack(side="bottom")

result_label = Label(text="Result", font=("Courier", 10, "bold"))
result_label.pack(side="right")

window.mainloop()

