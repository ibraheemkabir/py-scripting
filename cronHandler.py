import schedule
import time
from processLiqChecks import processCurrencyList

def func():
    processCurrencyList()
  
schedule.every(1).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(1)