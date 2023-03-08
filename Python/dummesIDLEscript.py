import random
geheimnis = random.randint (1,99)
tipp = 0
versuche = 0
print("Ich bin die Eule Ludwig und habe ein Geheimnis!")
print("""Wenn du mein Passwort, eine Zahl zwischen 1 und 99 errätst, werde ich es dir verraten! Aber Achtung: Du hast nur 6 versuche.""")

while tipp != geheimnis and versuche < 6:
    tipp = int(input("Wie lautet dein Vorschlag?"))
    if tipp < geheimnis:
        print("zu niedrig!")
    elif tipp > geheimnis:
        print("zu hoch!")

    versuche += 1

if tipp == geheimnis:
    print("Mist,du hast meine geheime Zahl erraten. Mein Geheimnis lautet... Deine Mutter LOL!")
else:
    print("Alle Versuche Verbraucht! Versuche es noch einmal!")
    print("Mein Passwort lautete ", geheimnis)
