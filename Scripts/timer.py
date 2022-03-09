import time

coolDown = 5
endTime = time.time() + coolDown

while True:
    currentTimeSec = time.time()
    currentTime = time.ctime(time.time())
    if currentTimeSec >= endTime:
        print("Loop Ends")
        break
    print(currentTime)
    time.sleep(1)