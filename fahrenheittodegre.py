input = input("Fahrenheit or Celsius (f or c): ")
degree = int(input("Degree"))


def fahrenheit_to_celsius (fahrenheit1):
    celsius = (fahrenheit1-32)/1,8
    return celsius
def celsius_to_fahrenheit (celcius):
    fahrenheit = (celsius*1,8 + 32)
    return fahrenheit
if input == "f":
    print("Celsius equivalent of the Fahrenheit value you entered: " , fahrenheit_to_celsius(dercr))
elif input == "c":
    print("Fahrenheit equivalent of the Celsius value you entered: " , celsius_to_fahrenheit(dercr))
