class Car:
    def __new__(cls,name,color):
        return object.__new__(cls)

    def __init__(self,name,color):
        self.name = name
        self.color = color

        self.speed = 0

    def speed_increase(self):
        self.speed += 10


car1 = Car('black','yellow')


print(car1.speed)
