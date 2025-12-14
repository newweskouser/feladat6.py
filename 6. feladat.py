import random

i = 0
db = 0

while i < 20:
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
        db = db + 1
    i = i + 1

print("A 3-mal osztható számok száma:", db)