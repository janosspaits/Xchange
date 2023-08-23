import install_requirements
from forex_python.converter import CurrencyRates, CurrencyCodes
from datetime import datetime
from tkinter import *
import customtkinter


now = datetime.now()
c = CurrencyRates()
currency_codes = CurrencyCodes()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title("X-Change")
window.geometry("780x270")
window.iconbitmap("dollarico.ico")

currency_options = [
    f"{code} - \n{currency_codes.get_currency_name(code)}" for code in ["GBP", "USD", "EUR", "CHF", "AUD", "CAD", "HUF",
                                                                        "JPY", "CNY", "HKD", "DKK", "PLN", "TRY", "KRW",
                                                                        "ZAR"]
]


def change_appearance_mode_event(new_appearance_mode):
    """Changes appearance mode to light/dark"""
    customtkinter.set_appearance_mode(new_appearance_mode)


def perform_conversion():
    """This is the function that performs the conversion"""
    global result_textbox
    start_currency = start_cur.get().split(' ')[0]
    end_currency = end_cur.get().split(' ')[0]

    if not money_entered.get().strip():
        result_textbox.delete('1.0', '1.100')
        result_textbox.insert('1.0', "Please enter an amount.")
        return

    try:
        money = float(money_entered.get())
    except ValueError:
        result_textbox.delete('1.0', '1.100')
        result_textbox.insert('1.0', "Invalid amount entered.")
        return

    try:
        result = c.get_rate(start_currency, end_currency, now) * money
        result_textbox.delete('1.0', '1.100')
        result_textbox.insert('1.0', f"{money} {start_currency} = {round(result, 3)} {end_currency}")
    except Exception as e:
        print(f"Error: {e}")
        result_textbox.delete('1.0', '1.100')
        result_textbox.insert('1.0', f"Error: {e}")


# Start amount entry box
money_entered = customtkinter.CTkEntry(master=window, width=180, height=35, border_width=2, corner_radius=5,
                                       placeholder_text="Enter the amount", placeholder_text_color="silver",
                                       font=('Arial', 16, 'bold'), justify='center')
money_entered.grid(row=1, column=1, pady=15, columnspan=2)

# Start currency button
start_cur = StringVar()
start_cur.set("Choose a Currency\n to convert from")
start_drop = customtkinter.CTkOptionMenu(window, width=200, height=50, variable=start_cur, values=currency_options,
                                         dropdown_font=('Arial', 12), dynamic_resizing=False, anchor='center',
                                         font=('Arial', 14, 'bold'), corner_radius=7)
start_drop.grid(row=2, column=0, padx=20, pady=10)

# End currency button
end_cur = StringVar()
end_cur.set("Choose a Currency\n to convert to")
end_drop = customtkinter.CTkOptionMenu(window, width=200, height=50, variable=end_cur, values=currency_options,
                                       dropdown_font=('Arial', 12), dynamic_resizing=False, anchor='center',
                                       font=('Arial', 14, 'bold'), corner_radius=7)
end_drop.grid(row=2, column=5, pady=10, padx=20)


# Result Textbox
result_textbox = customtkinter.CTkTextbox(window, font=("Arial", 16, "bold"), width=300, height=35, border_width=2)
result_textbox.grid(row=3, column=1, pady=15, columnspan=2)
result_textbox.delete('1.0', '1.100')
result_textbox.insert('1.0', '                              Result')


# Convert button
convert_button = customtkinter.CTkButton(master=window, width=120, height=40, text="Convert",
                                         command=perform_conversion, corner_radius=7, font=('Arial', 16, 'bold'))
convert_button.grid(row=4, column=1, pady=10, columnspan=2)


# Dark mode switch
switch_var = customtkinter.StringVar(value="Dark")
appearance_option = customtkinter.CTkSwitch(window, onvalue="Dark", offvalue="Light", width=80, text="Dark mode",
                                            command=lambda: change_appearance_mode_event(appearance_option.get()),
                                            variable=switch_var)
appearance_option.grid(row=4, column=0, ipadx=50)


window.mainloop()
