binario = input("Dame un numero binario: ")
decimal = 0

for i,valor in enumerate(reversed(binario)):
    if valor == "1":
        decimal += (2**i)

print(decimal)