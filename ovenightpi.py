from __future__ import division
import math
import time
from datetime import datetime

passed = False

while 1:
    pi = 0
    count = int(raw_input("To what intensity would you like this program to run to? "))
    print('\nEstimated time to completion: ' + str(round(count/330000, 3)) + ' seconds on your average iPhone 5')
    print('\nEstimated time to completion: ' + str(round(count/1000000, 3)) + ' seconds on your average PC')
    start = time.time()
    now = datetime.now()

    print('\nStarted at: ' + str(now.hour) + ": " + str(now.minute) + ": " + str(now.second))
    
    for x in range(int(count/100000000)):
        for y in range(100000000):
            pi += math.sqrt(1-((y+(100000000*x))/count)**2)
            if y % 100000000 == 0:
                print "\nJust reached: " + str(y+(100000000*x))
    
    end = time.time() - start
    print('\nPi: ' + str(4/count*pi))
    print('Total time: ' + str(end))
    print('Calculations per second: ' + str(count / end))
    now = datetime.now()
    print('Completed at: ' + str(now.hour) + ": " + str(now.minute) + ": " + str(now.second))
