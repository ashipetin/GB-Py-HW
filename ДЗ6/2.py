class Road:
    _length = 20
    _width = 5000
    def __init__(self, length, width, mass, thickness):
        self.length = length
        self.width = width
        print("Дорога создана")
        print("Масса асфальта:",int(length * width * int(mass) * int(thickness) / 1000), "т")
Road1 = Road(
Road._length,
Road._width,
input("Введите массу асфальта для покрытия 1м2 дороги: "),
input("Введите толщину полотна в сантиметрах: "))