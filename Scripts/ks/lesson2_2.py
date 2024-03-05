import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
num = []
cnt = "00000000"
for i in range(len(cnt)):
    num.append(int(cnt[i]))
#num = [1,1,1,1,1,1,1,1]
GPIO.setup(dac,GPIO.OUT)
GPIO.output(dac, num)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()
#number = [0,0,0,0,0,0,1,0]
