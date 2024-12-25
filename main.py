import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("por favor ingrse la longitud de su contraseña"))
password = ""

for i in range(longitud):
    x = random.choice(caracteres)
    password += x

print(password)
