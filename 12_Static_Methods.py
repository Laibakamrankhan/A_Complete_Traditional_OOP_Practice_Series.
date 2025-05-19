#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

f1 = TemperatureConverter.celsius_to_fahrenheit(100)
print(f"100°C is {f1}°F")  
