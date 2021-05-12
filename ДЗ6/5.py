class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой: {self.title}")
class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом: {self.title}")
class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером: {self.title}")

tool1 = Pen("Ручка шариковая синяя")
tool2 = Pencil("Карандаш графитовый простой")
tool3 = Handle("Маркер спиртовой синий")
tool1.draw()
tool2.draw()
tool3.draw()