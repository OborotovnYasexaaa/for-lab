from models.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self,brand,model,year,has_sidecar):
        super().__init__(brand,model,year)
        self.has_sidecar=has_sidecar
    def get_info(self):
        return f'{self.brand} {self.model} {self.year} наличие коляски: {self.has_sidecar}, скорость: {self.speed} км/ч'
    def move(self):
        return 'мотоцикл движется по дороге'