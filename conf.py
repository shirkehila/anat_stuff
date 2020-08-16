import json
import os

with open('config.json', 'rt') as f:
    json_config = json.load(f)
OS = json_config['os']
BASE_PATH = json_config['base_path'][OS]
OUTPUT_FILENAME_BROWSE = json_config['output_filename_browse']
OUTPUT_FILENAME_DOWNLOAD = json_config['output_filename_download']
CHROME_DRIVER_PATH = os.path.join(BASE_PATH, 'chromedriver.exe')
OUTPUT_FILE_PATH_BROWSE = os.path.join(BASE_PATH, OUTPUT_FILENAME_BROWSE)
OUTPUT_FILE_PATH_DOWNLOAD = os.path.join(BASE_PATH, OUTPUT_FILENAME_DOWNLOAD)
