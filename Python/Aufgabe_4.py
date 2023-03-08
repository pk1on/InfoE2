schulden = int(input("Schulden: "))
zinsen = int(input("Zinssatz (in %): "))
jahre = 0

while schulden > 0:
    jahre += 1
    schulden -= 120
    schulden = schulden * ((zinsen / 100) + 1)

print(jahre)