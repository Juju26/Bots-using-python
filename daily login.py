#https://github.com/Juju26

import webbrowser
import os
import time
def open_browser():
    url1="https://github.com/Juju26"
    #url2="https://leetcode.com/Ju_ju/"
    url3=""
    webbrowser.open_new_tab(url1)
open_browser()
time.sleep(5)
os.system("taskkill /f /im msedge.exe")