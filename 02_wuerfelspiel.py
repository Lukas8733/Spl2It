#02_wuerfelspiel.py
import random
random.seed()
angabe = input("Wie oft soll gewürfelt werden")
schaetzung = input("Welche Zahl wird gezogen")
schaetzung = int(schaetzung)
angabe = int(angabe)
    
for i in range (0,angabe):
	zahl = random.randint(1,6)
	print(zahl)

if schaetzung == zahl:
	print("Deine Zahl wurde gezogen")
	break
	
elif schaetzung != zahl:
	print("Verloren")
