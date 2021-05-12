class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f"{self.color} {self.name} едет")
    def stop(self):
        print("{self.color} {self.name} останавливается")
    def turn(self, direction):
        print(f"{self.color} {self.name} поворачивает {direction}")
    def show_speed(self):
        print(f"Скорость {self.color} {self.name} равна {self.speed} км/ч")
class TownCar(Car):
    def show_speed(self):
        print(f"Скорость {self.color} {self.name} равна {self.speed} км/ч")
        if self.speed > 60:
            print(f"{self.color} {self.name}: Превышение скорости!")
class SportCar(Car):()
class WorkCar(Car):
    def show_speed(self):
        if speed > 40:
            print(f"{self.name}: Превышение скорости!")
class PoliceCar(Car):()

car1 = PoliceCar(60, "Красный", "Dodge", True)
car2 = SportCar(120, "Зеленый", "Ferrari", False)
car3 = TownCar(61, "Черный", "Ford", False)

car2.go()
car2.show_speed()
car2.turn("вправо")
car3.go()
car3.show_speed()
