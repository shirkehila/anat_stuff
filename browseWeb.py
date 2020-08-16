import time
import datetime

url = r'https://python.org'
from selenium import webdriver

filename = r"C:\pe\browseDuration.txt"

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")

d = webdriver.Chrome(r"c:\pe\chromedriver.exe", options=options)
startTs = datetime.datetime.now()
d.get('https://python.org')

while not (d.title == "Welcome to Python.org"):
    time.sleep(0.1)
endTs = datetime.datetime.now()
duration = endTs - startTs
print(duration)
with open(filename, 'w') as f:
    print(duration, file=f)
d.quit()
