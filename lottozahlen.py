#lottozahlen
import random
random.seed()
lottozahlen = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
lottogezogen = []
for i in range(0,6):
	ziehung = random.randint(1,45)
	lottogezogen.append(lottozahlen(ziehung))
	lottozahlen.remove(lottozahlen(ziehung))
print(lottogezogen)
	