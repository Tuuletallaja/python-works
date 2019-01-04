print("Tere tulemast 0st 12ni korrutamisse.")
x = int(input("Palun sisesta arv mida korrutada: "))

t = 0

while t <= 12:
    print(str(x) + " x " + str(t) + " = " + str(x * t))
    t = t + 1