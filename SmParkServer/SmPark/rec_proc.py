#Backend

from openalpr import Alpr
import time #Keep track of time, at least at a local level. (Used for scheduling the recognition process)
import cv2
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

alpr = Alpr("us", "/usr/local/src/openalpr/openalpr.conf.user","/usr/local/src/openalpr/runtime_data/")
v = cv2.VideoCapture(0)

if not alpr.is_loaded():
    print "There's an error, consider checking the correctness of paths"
    sys.exit(1) #Just exit
    
alpr.set_top_n(20)
alpr.set_default_region('md')

def onDetected():
    #The stuff
    GPIO.output(18,GPIO.HIGH)
def notDetected():
    #other
    GPIO.output(18,GPIO.LOW)
def recognize(path,in_file):
    f = open(in_file,'w')
    i = 0
    results = alpr.recognize_file(path) #Use local path in Django app

    #Parse output
    if len(results['results']) == 0:
        print "No license plates detected"
        notDetected()
    
    for plate in results['results']:
        i += 1
        print "Plate %d" %(i)
        print " %12s %12s " %("Plate", "Confidence")
        for candidate in plate['candidates']:
            prefix = "-"
            if candidate['matches_template']:
                prefix = "*"
            f.write(str(candidate['plate']))
            print " %s %12s%12f"%(prefix, candidate['plate'],candidate['confidence'])
            onDetected()
            break
    f.close()




TBSR= 2 #Time Between Successive Recognitions, in seconds
prev_time = time.time() #Record current time
RES_FILE = 'file.txt'
while v.isOpened():
    success, frame = v.read()
    
    if abs(time.time() - prev_time) >= TBSR:
        cv2.imwrite('img.jpg', frame) #Save current image at a local directory
        recognize('img.jpg', RES_FILE) #Recognize the image
        prev_time = time.time() #"Your time is our time!"
    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #To quit press 'q'
       break

#Kill everything (and everyone)
v.release()
cv2.destroyAllWindows()
alpr.unload()
