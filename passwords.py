import random 
caracteres = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"

longitud = int(input("Introduce la longitud de la contraseña"))
password = ""
for i in range(longitud):
    password += random.choice(caracteres)

print(password)
