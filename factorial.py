import sys
sys.set_int_max_str_digits(1000000000)
factorial = int(input("Faktöriyelini bulmak istediğiniz sayıyı giriniz: "))
sonuc = 1
while factorial > 1:
    sonuc = sonuc * factorial
    factorial = factorial - 1
print(sonuc)