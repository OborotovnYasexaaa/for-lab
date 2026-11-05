from models.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self,brand,model,year,max_load):
        super().__init__(brand,model,year)
        self.max_load=max_load
    def get_info(self):
        return f'{self.brand} {self.model} {self.year} грузоподъёмность: {self.max_load}, скорость: {self.speed} км/ч'
    def move(self):
        return 'трактор везёт груз'
    