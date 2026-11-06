from abc import ABC,abstractmethod



class Vehicle(ABC):
    def __init__(self,brand,model,year):#структура транспорта
        self.brand=brand
        self.model=model
        self.year=year
        self._speed=0


    @property
    def speed(self):#чтение текущ скокрости
        return self._speed
    @speed.setter
    def speed(self,value):#запись скорости
        if value<0:
            raise ValueError('скорость не может быть отрицательной')
        self._speed=value


    
    def accelerate(self,value):#скорость увелич
        if value<0:
            raise ValueError('значение не может быть отрицательным')
        self.speed+=value
    
    
    def brake(self,value):#скорость уменьшение но не меньше 0
        if value<0:
            raise ValueError('значение не может быть отрицательным')
        self.speed=max(0,self.speed-value)



    def stop(self):#полная остановка
        self.speed=0

    def get_info(self):#текущая инфа 
        return f'марка:{self.brand}, модель:{self.model}, год:{self.year}, текущая скорость:{self.speed}км/ч'


    def __str__(self):
        return self.get_info()

    @abstractmethod
    def move(self):
        pass
         
