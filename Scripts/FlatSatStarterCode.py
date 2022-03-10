#complete CAPITALIZED sections

#AUTHOR: 
#DATE:

#import libraries
import time
from datetime import datetime
from datetime import date
import os
import board
import busio
import adafruit_bno055
#from git import Repo
from picamera import PiCamera

#setup imu and camera
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
camera = PiCamera()

"""
#bonus: function for uploading image to Github
def git_push():
    try:
        repo = Repo('/home/pi/FlatSatChallenge') #PATH TO YOUR GITHUB REPO
        repo.git.add('folder path') #PATH TO YOUR IMAGES FOLDER WITHIN YOUR GITHUB REPO
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')
        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
"""

    
#SET THRESHOLD
threshold = 25

timeCooldown = 2
cameraTime = 5
#read acceleration
while True:
    accelX, accelY, accelZ = sensor.acceleration
    
    try:
        if ((abs(accelX) + abs(accelY)) > threshold) :
            
            #print(date.today().strftime("%m/%d/%y"), " " , datetime.now().strftime("%H:%M:%S"))
            
            #Take a picture and save it
            camera.start_preview()
            
            time.sleep(cameraTime)
            currentTime = datetime.now().strftime("%H:%M:%S")
            currentDate = date.today().strftime("%m-%d-%y")
            dateTime = currentDate + " " + currentTime

            #Take photo
            camera.capture('/home/pi/Downloads/Captures/Capture%s.jpg' % dateTime)
            
            camera.stop_preview()
            #Upload image to GitHub
            
            
            print("Snapshot taken")
            #Value refers to the length in seconds of the pause between snapshots
            time.sleep(cameraTime + timeCooldown)
    except:
        print("Failure")
        
    #CHECK IF READINGS ARE ABOVE THRESHOLD
        #PAUSE
