from forex_python.converter import CurrencyRates, CurrencyCodes
from datetime import datetime
from tkinter import *

now = datetime.now()
c = CurrencyRates()
currency_codes = CurrencyCodes()

window = Tk()
window.title("X-Change")
window.geometry("490x230")
window.iconbitmap("dollarico.ico")

instructions = Label(text="Enter the amount:", font=("Arial", 12, "bold"))
instructions.grid(row=0, column=1)

to_label = Label(text="", font=("Arial", 10, "bold"))
to_label.grid(row=2, column=1)

currency_options = [
    f"{code} - \n{currency_codes.get_currency_name(code)}" for code in ["GBP", "USD", "EUR", 
                                                                      "CHF", "AUD", "CAD", "HUF", 
                                                                      "JPY", "CNY", "HKD"]
]

money_entered = Entry(width=10)
money_entered.grid(row=1, column=1, pady=5)

start_cur = StringVar()
start_cur.set("Choose a Currency\n to convert from")
start_drop = OptionMenu(window, start_cur, *currency_options)
start_drop.configure(width=18)
start_drop.grid(row=2, column=0, padx=10, pady=10)

end_cur = StringVar()
end_cur.set("Choose a Currency\n to convert to")
end_drop = OptionMenu(window, end_cur, *currency_options)
end_drop.configure(width=18)
end_drop.grid(row=2, column=2, padx=1, pady=10)


def perform_conversion():
    start_currency = start_cur.get().split(' ')[0]
    end_currency = end_cur.get().split(' ')[0]      
    
    if not money_entered.get().strip():
        result_label["text"] = "Please enter an amount."
        return

    try:
        money = float(money_entered.get())
    except ValueError:
        result_label["text"] = "Invalid amount entered."
        return
    
    try:
        result = c.get_rate(start_currency, end_currency, now) * money
        result_label["text"] = f"{money} {start_currency} = {round(result, 3)} {end_currency}"
    except Exception as e:
        print(f"Error: {e}")
        result_label["text"] = f"Error: {e}"


convert_button = Button(window, text="Convert", command=perform_conversion, height=2, width=8)
convert_button.grid(row=4, column=1, pady=10)

result_label = Label(text="Result", font=("Arial", 10, "bold"))
result_label.grid(row=3, column=1, pady=15)

window.mainloop()

