import requests
import os
import time
import datetime
from conf import (OUTPUT_FILE_PATH_DOWNLOAD)
from core import log_duration


def delete_file(downloaded_file_name):
    try:
        if os.path.isfile(downloaded_file_name):
            os.remove(downloaded_file_name)
    except Exception as e:
        print("failed to delete test file download with exception: " + str(e))


def get_downloaded_file(url):
    return os.path.join(local_downloads_folder, url.rsplit('/', 1)[-1])


def get_download_duration(url, downloaded_file_path):
    start_timestamp = datetime.datetime.now()
    downloaded_obj = requests.get(url)
    with open(downloaded_file_path, "wb") as file:
        file.write(downloaded_obj.content)
    while not (os.path.isfile(downloaded_file_path)):
        time.sleep(0.1)
    end_timestamp = datetime.datetime.now()
    duration = end_timestamp - start_timestamp
    return duration


if __name__ == '__main__':
    local_downloads_folder = os.path.join(os.path.expanduser('~'), 'downloads')
    url = 'https://artifacts.elastic.co/downloads/kibana/kibana-7.8.0-windows-x86_64.zip'
    downloaded_file_path = get_downloaded_file(url)
    delete_file(downloaded_file_path)
    duration = get_download_duration(url, downloaded_file_path)
    log_duration(duration, OUTPUT_FILE_PATH_DOWNLOAD)
    delete_file(downloaded_file_path)
