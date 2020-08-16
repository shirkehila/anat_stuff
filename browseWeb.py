import time
import datetime
import json
import os
from selenium import webdriver

BASE_PATH = ''
OS = ''
OUTPUT_FILENAME = ''
CHROME_DRIVER_PATH = ''
OUTPUT_FILE_PATH = ''


def get_config():
    global BASE_PATH
    global OS
    global OUTPUT_FILENAME
    with open('config.json', 'rt') as f:
        json_config = json.load(f)
        OS = json_config['os']
        BASE_PATH = json_config['base_path'][OS]
        OUTPUT_FILENAME = json_config['output_filename']


def create_paths():
    global CHROME_DRIVER_PATH
    global OUTPUT_FILE_PATH
    CHROME_DRIVER_PATH = os.path.join(BASE_PATH, 'chromedriver.exe')
    OUTPUT_FILE_PATH = os.path.join(BASE_PATH, OUTPUT_FILENAME)


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


def log_duration(duration):
    print(duration)
    with open(OUTPUT_FILE_PATH, 'w') as f:
        print(duration, file=f)


if __name__ == '__main__':
    get_config()
    create_paths()
    duration = get_chrome_opening_duration()
    log_duration(duration)
