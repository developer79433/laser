import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_LDR = 23

GPIO.setup(GPIO_LDR, GPIO.IN)

if __name__ == '__main__':
    try:
        while True:
            print("LDR input = %s" % ("ON" if GPIO.input(GPIO_LDR) else "OFF"))
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
