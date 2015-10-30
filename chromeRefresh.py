#!/usr/bin/python2
#Originally from http://stackoverflow.com/questions/11344414/windows-chrome-refresh-tab-0or-current-tab-via-command-line
#Documentation https://developer.chrome.com/devtools/docs/debugger-protocol#extension

#Refreshes pages open in chrome which contain the first argument passed.
#If there is a 2nd argument it will be parsed as the delay
import urllib2
import urllib
import os
import subprocess
import json
import sys
import time

from websocket import create_connection

def refresh_page(url):
    data = json.load(urllib2.urlopen('http://localhost:9222/json'))

    found_page = False
    for page in data:
        if page['url'].find(url) != -1:
            if 'webSocketDebuggerUrl' in page:
                found_page = True
                websocketURL = page['webSocketDebuggerUrl']
                ws = create_connection(websocketURL)

                obj = {  "id": 0,
                        "method": "Page.reload",
                        "params":
                        {
                        "ignoreCache": False,
                        "scriptToEvaluateOnLoad": ""
                        }
                    }

                dev_request = json.dumps(obj)
                ws.send(dev_request)
                result =  ws.recv()
                ws.close()
    if not found_page:
        raise Exception("No page found")
try:
    time.sleep(float(sys.argv[2]))
except:
    pass #No 2nd arg passed, or it wasn't a number
refresh_page(sys.argv[1])
