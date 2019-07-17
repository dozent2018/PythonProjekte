class Roboter:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('Hole Wert')
        return self.__name

    def set_name(self, name):
        print('Setze Wert')
        self.__name = name

    name = property(get_name,set_name)
    

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)