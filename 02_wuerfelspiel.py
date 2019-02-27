#02_wuerfelspiel.py
angabe  =("Wie oft soll gewürfelt werden")
schaetzung = ("Welche Zahl wird gezogen")
schaetzung = int(schaetzung)
angabe = int(angabe)
for zahl in range (0,anzahl)
	import random
    random.seed()
    zahl = random.randint(1,6)
	print(zahl)

if schaetzung == zahl:
	print("Deine Zahl wurde gezogen")
if schaetzung != zahl:
	print("Verloren")
