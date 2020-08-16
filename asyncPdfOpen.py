# setup pdf files list
import os, multiprocessing as mp, datetime, subprocess, pathlib, pywinauto, time
from pywinauto.application import Application
from pywinauto.timings import wait_until

pdfFilesPath = r"C:\PE\asyncPdfFiles\\"
durationFile = "c:\pe\downloadDuration.txt"


def check(expectedTitle):
    return pywinauto.findwindows.find_windows(title=expectedTitle)


def execFile(process, file):
    durationFile = "c:\pe\\" + file + "_duration.txt"
    executionCmd = process + " " + pdfFilesPath + file
    print(executionCmd)
    startTs = datetime.datetime.now()

    try:

        #   startupinfo = subprocess.STARTUPINFO()
        #   startupinfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
        # #   print("In exec process")
        p = subprocess.Popen([process, '/A', 'page=1', pdfFilesPath + file], shell=False, stdout=subprocess.PIPE)
        pid = p.pid
        #   print(p.returncode)
        #   p.poll()

        #  (output, err) = p.communicate()

        # This makes the wait possible
        # p_status = p.wait()
        # pywinauto.timings.(5, 0.1, check(file))  # Important: 'check' without brackets
        # pywinauto.findwindows.find_elements(title=file)
        #  app = Application(backend="win32").start(executionCmd)
        #  app.WindowSpecification.wait('exists')

        app = Application(backend='uia').connect(process=pid)
        win = app.top_window().children()[0].element_info.parent.name
        while file not in win:
            # print ("waiting for title to be i")
            time.sleep(0.1)
            win = app.top_window().children()[0].element_info.parent.name
        print("file openend, includes title: " + win)
        # win.wait('exists', timeout=5)
        wrapper = app.top_window().children()

        endTs = datetime.datetime.now()
        duration = endTs - startTs
        with open(durationFile, 'w') as f:
            print(duration, file=f)

        p.kill()
    #   os.system('taskkill /IM acrord32.exe')
    # p.kill()
    except Exception as e:
        print("failed to execute pdf with exception: " + str(e))


if __name__ == "__main__":
    pdfFilesList = os.listdir(pdfFilesPath)
    [pdfFilesPath + file for file in pdfFilesList]

    print(pdfFilesList)
    # execute them async
    process = "c:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
    pool = mp.Pool(processes=len(pdfFilesList))
    results = [pool.apply_async(execFile(process, p), args=(p,)) for p in pdfFilesList]
    # write launch time of each PDF to a separate results file
