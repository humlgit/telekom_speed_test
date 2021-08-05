#!/usr/bin/env python3

###scriptexecution for linux or windows
import platform
import time             #Benennung der Ordner, Timedelay

#check OS
win = 0
linux = 0

if platform.system() == "Linux":
    linux = 1
elif platform.system() == "Windows":
    win = 1
else:
    print("Error with OS detection\nClose in ...")
    for i in range(5):
        print(5-i)
        time.sleep(1)
    quit()

###Imports
import webbrowser       #open chrome tab
import os               #create folder
if win:
    import pyautogui        #screenshot
    import urllib.request   #read webelements
if linux:
    from PIL import ImageGrab       #console:    python3 -m pip install --upgrade pip
                                    #            python3 -m pip install Pillow
                                    #            python3 -m pip install --upgrade Pillow
    import subprocess
    import urllib.request
    import urllib.parse
    import re

###create path if not available
path = ''
if win:
    #find user
    user = os.environ.get("USERPROFILE")
    path = os.path.join(user, 'Pictures', 'telekom')
    #create folder
    if not os.path.exists(path):
        os.makedirs(path)
        
if linux:
    #find user
    user = os.getlogin()
    path = os.path.join('/home', user, 'Pictures', 'telekom')
    #create folder
    if not os.path.exists(path):
        os.mkdir(path)


num = 744
saves = 0
url = 'http://kabelspeed.telekom-dienste.de/'

while saves < num:
    t = time.strftime("%M")
    if t == '58' :          #repetition every 58th minute
        ###open and exe Telekom Speed Test
        if win:     chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                    #chrome
        if linux:   webbrowser.open_new(url)

        ###wait for results
        if win:
            time.sleep(60)
            #bit better: read out webelements...
            '''
            responds = urllib.request.urlopen(url)
            # get the result code and print it
            print("result code: " + str(responds.code))
            
            # read the data from the URL and print it
            data = responds.read()
            print(data)
            print(type(data))
            
            html = data.decode('iso-8859-1')
            print(type(html))
            #'''
            '''
            time.sleep(5)
            if (url_code.read().decode('speed-assembly monochrome-primary') == true):
                print('ok')
            
            else:
                print('skipped')
            #'''

        if linux:
            time.sleep(60)
            '''url = 'http://kabelspeed.telekom-dienste.de/'
            values = {'s':'basics', 'submit':'search'}
            data = urllib.parse.urlencode(values)
            data = data.encode('utf-8')
            req = urllib.request.Request(url, data)
            resp = urllib.request.urlopen(req)
            respData = resp.read()
            paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
            #print(respData)
            for eachStyle in paragraphs:
                print(eachStyle)
            '''
            


        ###screenshot result
        timestr = time.strftime("%Y-%m-%d_%H-%M") #get date and time

        if win:
            screen = pyautogui.screenshot()
            screen_path = os.path.join(path, timestr+'.png')
            screen.save(screen_path)

        if linux:
            screen=ImageGrab.grab()
            os.chdir('/home/pi/Pictures/telekom')
            screen.save(timestr+'.png', 'PNG')
            
        ###evaluation....
            
        ###close browser
        saves = saves + 1
        print(saves, '. screenshot')
        subprocess.call(["killall","chromium-browse"])
    else:
        time.sleep(60)    
