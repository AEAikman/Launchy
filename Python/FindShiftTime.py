'''
FindShiftTime.py
Aaron Aikman
Arguments:
Start time hour,
start time minutes,
timer minutes (or timer hours and then timer minutes)
Then it starts a timer for that time using Hourglass.exe

'''

import sys
import subprocess
import threading
from datetime import datetime, timedelta
from time import sleep

if len(sys.argv) == 1:
    args = ['10', '10', '4', '30']  # For testing
else:
    args = sys.argv

minToAdd = int(args[3])

if len(sys.argv) > 4:
    minToAdd = ((int(args[3]) * 60) + int(args[4]))

s = '2013-08-11 ' + args[1] + ':' + args[2] + ':49'
mytime = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
mytime += timedelta(minutes=minToAdd)
myHours = int(mytime.strftime("%H"))
myMinutes = mytime.strftime("%M")

if myHours > 12:
    myHours -= 12

endTime = str(myHours) + ':' + myMinutes + ' pm'
hourglassArgs = [r'C:\Users\aaikman\AppData\Local\Launchy\plugins\Hourglass\Hourglass.exe', endTime]


class hourglassThread(threading.Thread):
    def run(self):
        subprocess.call(hourglassArgs)
        pass


thread = hourglassThread()
thread.daemon = True
thread.start()

sleep(0.1)
quit()
