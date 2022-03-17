#complete CAPITALIZED sections

#AUTHOR: SatelliteWarriors
#DATE: 03 - 07 - 2022

#import libraries
import time
from datetime import datetime
from datetime import date
import os
import board
import busio
import adafruit_bno055
from git import Repo
from picamera import PiCamera

#setup imu and camera
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
camera = PiCamera()


#bonus: function for uploading image to Github
def git_push():
    repo = Repo('/home/pi/Downloads/repository') #PATH TO YOUR GITHUB REPO_
    repo.git.add('Pictures') #PATH TO YOUR IMAGES FOLDER WITHIN YOUR GITHUB REPO
    repo.index.commit('New Photo')
    print('Made the commit')
    #origin = repo.remote('CubeSat')
    #print('Added remote')
    repo.git.push('CubeSat', 'master')
    print('Pushed changes')

        


    
#SET THRESHOLD
threshold = 25

timeCooldown = 2
cameraTime = 5
#read acceleration
while True:
    accelX, accelY, accelZ = sensor.acceleration
    
    #try:
    if ((abs(accelX) + abs(accelY)) > threshold) :
        
        #print(date.today().strftime("%m/%d/%y"), " " , datetime.now().strftime("%H:%M:%S"))
        
        #Take a picture and save it
        camera.start_preview()
        
        time.sleep(cameraTime)
        currentTime = datetime.now().strftime("%H:%M:%S")
        currentDate = date.today().strftime("%m-%d-%y")
        dateTime = currentDate + " " + currentTime

        #Take photo
        camera.capture('/home/pi/Downloads/repository/Pictures/Capture_%s.jpg' % dateTime)
        
        camera.stop_preview()
        
        #Find Plastic in Image
        
        # Importing Image from PIL package
        from PIL import Image, ImageColor
        from functions import returnAvg, returnGreat, returnGreatString, returnLow, findSum, findDif, difGreat, determineMax, convert_rgb_to_names
        # creating a image object
        im = Image.open(r'/home/pi/Downloads/repository/Pictures/Capture_%s.jpg' % dateTime)
        px = im.load()

        # Max and Min for Pixels in Image
        xBound, yBound = im.size

        img = Image.new('RGB', (xBound, yBound))

        colorname = "red"

        needColor = True

        for x in range(xBound):
            for y in range(yBound):
                needColor = True
                while needColor:
                    r = px[x, y][0]
                    g = px[x, y][1]
                    b = px[x, y][2]
                    pxColor = convert_rgb_to_names((r, g, b))
                    print(pxColor)
                    if pxColor == colorname:
                        needColor = False
                        print("Found", colorname, "color at coords:", x, ",", y)
                        img.putpixel((x, y), (r, g, b))
                    else:
                        contrast = 50
                        f = (returnGreat(r, g, b)-contrast)
                        img.putpixel((x, y), (f, f, f))
                        needColor = False
        img.save("newImg.jpg")
        print("Image Saved!")
        img.show()
        
        #Upload image to GitHub
        
        
        print("Snapshot taken")
        #git_push()
        #Value refers to the length in seconds of the pause between snapshots
        time.sleep(cameraTime + timeCooldown)
    #except:
        #print("Failure")
        
    #CHECK IF READINGS ARE ABOVE THRESHOLD
        #PAUSE
