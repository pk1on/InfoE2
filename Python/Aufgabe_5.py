dec = int(input("Decimalzahl: "))
bin = ""

while not (dec / 2) == 0:
    bin = str((dec % 2)) + bin
    dec = int(dec / 2)

print(bin)