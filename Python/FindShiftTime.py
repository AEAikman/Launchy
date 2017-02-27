'''
FindShiftTime.py
Aaron Aikman
Finds 4.5 hours from two entered arguments of starting hour and minute
Then it starts a timer for that time using Hourglass.exe

'''

import sys
import subprocess
from datetime import datetime, timedelta

args = sys.argv

s = '2013-08-11 ' + args[1] + ':' + args[2] +':49'
mytime = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
mytime += timedelta(minutes=((4 * 60) + 30))
myHours = int(mytime.strftime("%H"))
myMinutes = mytime.strftime("%M")

if myHours > 12:
    myHours -= 12

endTime = str(myHours) + ':' + myMinutes + ' pm'
hourglassArgs = [r'C:\Users\aaikman\AppData\Local\Launchy\plugins\Hourglass\Hourglass.exe', endTime]
subprocess.call(hourglassArgs)
sys.exit()