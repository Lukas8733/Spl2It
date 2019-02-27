#02_wuerfelspiel.py
import random
random.seed()
angabe = input("Wie oft soll gewürfelt werden")
schaetzung = input("Welche Zahl wird gezogen")
schaetzung = int(schaetzung)
angabe = int(angabe)
counter =0
    
for i in range (0,angabe):
	zahl = random.randint(1,6)
	print(zahl)

	if(schaetzung == zahl):
		counter=counter+1
		
	else:
		print("Verloren")

print("Deine Zahl", schaetzung, "wurde", counter ,"mal gezogen")