import time
import datetime
from selenium import webdriver
from conf import (CHROME_DRIVER_PATH, OUTPUT_FILE_PATH_BROWSE)
from core import log_duration


def init_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    d = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
    return d


def get_chrome_opening_duration():
    start_timestamp = datetime.datetime.now()
    d = init_webdriver()
    d.get('https://python.org')

    while not (d.title == "Welcome to Python.org"):
        time.sleep(0.1)
    end_timestamp = datetime.datetime.now()
    d.quit()
    duration = end_timestamp - start_timestamp
    return duration


if __name__ == '__main__':
    duration = get_chrome_opening_duration()
    log_duration(duration, OUTPUT_FILE_PATH_BROWSE)
