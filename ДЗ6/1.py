import time
import sys
class TrafficLight:
    __color = "Off"
    def running(self):
        print("Светофор включен")
        TrafficLight.color = "Красный"
        print(f"Светофор горит, цвет: {TrafficLight.color}")
        for i in range(7,0,-1):
            sys.stdout.write(str(i)+' ')
            sys.stdout.flush()
            time.sleep(1)
        TrafficLight.color = "Желтый"
        print(f"\nСветофор горит, цвет: {TrafficLight.color}")
        for i in range(2,0,-1):
            sys.stdout.write(str(i)+' ')
            sys.stdout.flush()
            time.sleep(1)
        TrafficLight.color = "Зеленый"
        print(f"\nСветофор горит, цвет: {TrafficLight.color}")
        for i in range(5,0,-1):
            sys.stdout.write(str(i)+' ')
            sys.stdout.flush()
            time.sleep(1)
        TrafficLight.color = "Off"
        print("\nСветофор выключен")
svetofor = TrafficLight()
svetofor.running()
