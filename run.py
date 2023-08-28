import sys
import os
import time
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), './fygen/'))

import fygen

serial_path = sys.argv[1]
fy = fygen.FYGen(serial_path=serial_path)

fy.get_measurement()

time.sleep(1.5)

print("time,freq_hz,period_sec,positive_width_sec,negative_width_sec,duty_cycle")

while True:
    try:
        elms = fy.get_measurement()
        print("{},{},{},{},{},{}".format(
            str(datetime.datetime.now()),
            elms["freq_hz"],
            format(elms["period_sec"], '.9f'),
            format(elms["positive_width_sec"], '.9f'),
            format(elms["negative_width_sec"], '.9f'),
            elms["duty_cycle"]
            ))
    except:
        sys.stderr.print("unknown error")
    sys.stdout.flush()
    time.sleep(1.0)
