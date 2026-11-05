from models.vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self,brand,model,year,color,max_people):
        super().__init__(brand,model,year)
        self.color = color
        self.max_people = max_people

    def move(self):
        return 'Автобус везёт людей через город'
    def get_info(self):
        return f'{self.brand} {self.model} {self.year} цвет: {self.color}, вместимость: {self.max_people} человек, скорость: {self.speed} км/ч' 

        