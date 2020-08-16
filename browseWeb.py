import time,os,datetime
url = r'https://python.org'
#with Browser('chrome') as browser:
from selenium import webdriver
filename=r"C:\pe\browseDuration.txt"

# start the browser
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1920,1080")



#driver.quit()

d = webdriver.Chrome(r"c:\pe\chromedriver.exe",options=options)
startTs=datetime.datetime.now()
d.get('https://python.org')


while not(d.title=="Welcome to Python.org"):
   time.sleep(0.1)
endTs=datetime.datetime.now()
duration= endTs-startTs
print (duration)
with open(filename, 'w') as f:
    print(duration, file=f)
d.quit()
# webbrowser.open(url)
#
# while True:
#     logo = pyautogui.locateOnScreen('c:\pe\python-logo.png')
#     print (logo)
#     if logo is not None:
#         break
# import subprocess
# result=subprocess.Popen([r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "https://python.org"],shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#url=r"https://docs.python.org/3/library/webbrowser.html"
# webbrowser.open(url)
# # win2find = "Welcome to Python.org"
# # whnd = FindWindow( win2find,None)
# win2find = 'Welcome to Python.org'
# hwnd=win32gui.GetForegroundWindow()
# omniboxHwnd = win32gui.FindWindowEx(hwnd, 0, win2find, None)
# def getWindowText(hwnd):
#     buf_size = 1 + win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH, 0, 0)
#     buf = win32gui.PyMakeBuffer(buf_size)
#     win32gui.SendMessage(hwnd, win32con.WM_GETTEXT, buf_size, buf)
#     return str(buf)
# getWindowText(hwnd)
# thetitle =GetWindowText( FindWindowEx(GetActiveWindow(),None,None,win2find) )
#
# while(thetitle==""):
#     time.sleep(0.1)
#
#     print("waiting for browser top open")
#     win2find = "Welcome to Python.org"
#   #  whnd = FindWindowEx(None, None, None, win2find)
#     thetitle = GetWindowText(FindWindowEx(GetActiveWindow(), None, None, win2find))


os.system('taskkill /f /im Chrome.exe')