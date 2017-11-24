from __future__ import division
import math
import time
from datetime import datetime

passed = False

while 1:
    pi = 0
    count = int(raw_input('\nTo what accuracy would you like your calculation done to? '))
    print('\nEstimated time to completion: ' + str(round(count/330000, 3)) + ' seconds on your average iPhone 5')
    print('\nEstimated time to completion: ' + str(round(count/1000000, 3)) + ' seconds on your average PC')
    start = time.time()
    now = datetime.now()

    print('\nStarted at: ' + str(now.hour) + ": " + str(now.minute) + ": " + str(now.second))
    
    for x in range(count):
        pi += math.sqrt(1-(x/count)**2)
    
    end = time.time() - start
    print('\nPi: ' + str(4/count*pi))
    print('Total time: ' + str(end))
    print('Calculations per second: ' + str(count / end))
    now = datetime.now()
    print('Completed at: ' + str(now.hour) + ": " + str(now.minute) + ": " + str(now.second))
