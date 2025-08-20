class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def fromCelsius(cls, celsius):
        return cls(celsius)

    @classmethod
    def fromFahrenheit(cls, fahrenheit):
        celsius = cls.toCelsius(fahrenheit)
        return cls(celsius)

    @staticmethod
    def toFahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def toCelsius(fahrenheit):
        return (fahrenheit - 32) * 5/9


if __name__ == '__main__':
    #from Celsius
    temp1 = Temperature.fromCelsius(34)
    print(f"Temp1: {temp1.celsius}°C = {Temperature.toFahrenheit(temp1.celsius):.2f}°F")

    #from Fahrenheit
    temp2 = Temperature.fromFahrenheit(100)
    print(f"Temp2: {temp2.celsius:.2f}°C = 86°F")