a = int(input("Sisesta esimene arv (a): "))
b = int(input("Sisesta teine arv (b): "))
c = int(input("Sisesta kolmas arv (c): "))

if a > b and a > c:
    print("Suurim arv on " + str(a))
elif b > a and b > c:
    print("Suurim arv on " + str(b))
else:
    print("Suurim arv on " + str(c))

