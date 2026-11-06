from garage import Garage

from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle
from models.bus import Bus
def main():
    garage=Garage()

    car=Car("Toyota", "Camry", 2024, 4)
    truck=Truck('беларус','82.1',2023,3200)
    motorcycle=Motorcycle('ИМЗ (Ирбит)','урал М-72',2016,True)
    bus=Bus('ЛиАЗ','ЛиАЗ-677',2000,'Зеленый',110)

    garage.add_vehicle(car)
    garage.add_vehicle(truck)
    garage.add_vehicle(motorcycle)
    garage.add_vehicle(bus)

    garage.show_all()


if __name__ == '__main__':
    main()