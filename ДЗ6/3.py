class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        return (self.name + " " + self.surname)
    def get_full_profit(self):
        return(int(self._income['wage']) + int(self._income['bonus']))
worker1 = Position('Dmitry','Petrov','Plumber','55000','15000')
print(worker1.get_full_name())
print(worker1.get_full_profit())