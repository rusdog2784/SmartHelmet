from mq import *
import sys, time

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (round(perc["GAS_LPG"], 4), round(perc["CO"], 4), round(perc["SMOKE"], 4)))
        sys.stdout.flush()
        time.sleep(0.1)

except:
    print("\nAbort by user")
