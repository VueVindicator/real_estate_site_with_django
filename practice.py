import datetime
from datetime import date
from time import time

# pip modules
import camelcase

today = date.today()
timestamp = time()
print(today)
print(timestamp)

camel = camelcase.CamelCase()
text = 'Hello there world'
print(camel.hump(text))