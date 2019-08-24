import random
import time
import device
from pushsafer import init, Client

MIN_TEMP = 60
MAX_TEMP = 78

def main():
    heater = device.Device("heater")
    fan = device.Device("fan")

    while True:
        current_temp = get_temperature()
        print("The current temperature is {} degrees.".format(current_temp))
        time.sleep(2)

        if current_temp > MAX_TEMP:
            fan.set_power(True)
            time.sleep(1)
            heater.set_power(False)
            time.sleep(1)
            print("\n")
        elif current_temp < MIN_TEMP:
            fan.set_power(False)
            time.sleep(1)
            heater.set_power(True)
            time.sleep(1)
            print("\n")
        else:
            fan.set_power(False)
            time.sleep(1)
            heater.set_power(False)
            time.sleep(1)
            print("\n")
        
        time.sleep(5)

def get_temperature():
    return random.randint(50, 90)


if __name__ == '__main__':
    main()