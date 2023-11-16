girdi = input("fahrenheit mi celcius mu: ")
dercr = int(input("serede"))


def fahrenheit_to_celcius (fahrenheit1):
    celcius = (fahrenheit1-32)/1,8
    return celcius
def celcius_to_fahrenheit (celcius):
    fahrenheit = (celcius*1,8 + 32)
    return fahrenheit
if girdi == "f":
    print("girdiğin fahrenheit değerin celcius karşılığı: " , fahrenheit_to_celcius(dercr))
else:
    print("girdiğin celcius değerin fahrenheit karşılığı: " , celcius_to_fahrenheit(dercr))