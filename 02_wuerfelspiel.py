#02_wuerfelspiel.py
angabe = input("Wie oft soll gewürfelt werden")

schaetzung = input("Welche Zahl wird gezogen")
schaetzung = int(schaetzung)
angabe = int(angabe)
    import random
    random.seed()
for i in range (0,angabe):
	zahl = random.randint(1,6)
	print(zahl)

if schaetzung == zahl:
	print("Deine Zahl wurde gezogen")
if schaetzung != zahl:
	print("Verloren")
