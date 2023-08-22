from forex_python.converter import CurrencyRates
from datetime import datetime
c = CurrencyRates()
now = datetime.now()


print(c.get_rate('GBP', 'HUF'))

some_day = datetime(2023, 8, 22)
print(c.get_rate('GBP', 'HUF', now))
