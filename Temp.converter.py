def convert_temperature(value, unit):
    unit = unit.lower()

    if unit == "celsius":
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin

    elif unit == "fahrenheit":
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, kelvin

    elif unit == "kelvin":
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit

    else:
        return None


# User input
value = float(input("Enter the temperature value: "))
unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")

result = convert_temperature(value, unit)

if result:
    if unit.lower() == "celsius":
        print(f"{value}°C = {result[0]:.2f}°F and {result[1]:.2f}K")
    elif unit.lower() == "fahrenheit":
        print(f"{value}°F = {result[0]:.2f}°C and {result[1]:.2f}K")
    elif unit.lower() == "kelvin":
        print(f"{value}K = {result[0]:.2f}°C and {result[1]:.2f}°F")
else:
    print("Invalid unit entered.")
