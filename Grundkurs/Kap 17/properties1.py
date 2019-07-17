class Roboter:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('Hole Wert')
        return self.__name

    @name.setter
    def name(self, name):
        print('Setze Wert')
        self.__name = name
    

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self.__temperature = value