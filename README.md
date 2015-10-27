# chrome-refresh-tabs
Python script to refresh specific tabs in chrome/chromium. Useful in build scripts when working with webservers.

## Installation
Clone this repository.
Install `websocket_client` for Python2 using either `pip install -r requirements.txt` from the cloned repository or `pip install websocket_client`. If you have multiple versions of Python installed you may need to use pip2 instead of pip.

## Usage
Start Chrome/Chromium with the flag: `--remote-debugging-port=9222` as this script uses the [Remote debugging protocol](https://developer.chrome.com/devtools/docs/debugger-protocol). (You can check if this is enabled by going to [http://localhost:9222])(http://localhost:9222). If the webpage exists, the flag is enabled.

Run chromeRefresh.py with python2. It can take the following optional arguments: `python2 chromeRefresh.py [queryString] [delay]` where [queryString] is a string contained in the web url in which pages will be refreshed and [delay] is a the delay before refreshing in seconds.

Example: `python2 chromeRefresh.py youtube 2`: Will refresh all tabs with the string 'youtube' in their URL after 2 seconds of delay.

Example: `python2 chromeRefresh.py`: Will refresh all open tabs.


Based on [http://stackoverflow.com/questions/11344414/windows-chrome-refresh-tab-0or-current-tab-via-command-line](http://stackoverflow.com/questions/11344414/windows-chrome-refresh-tab-0or-current-tab-via-command-line)