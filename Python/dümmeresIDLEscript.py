print("Wie lang und breit ist ihr Raum guter Herr?")
a = input("Höhe (in m)")
b = input("Breite (in m)")
a = a.replace(",", ".")
b = b.replace(",", ".")
a = float(a)
b = float(b)

print("Sie benötigen ", a * b ,"m² Teppich für den Raum.")
