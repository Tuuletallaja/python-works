from random import randint

# Loome puuviljade listi
viljad = ["õun","kirss","apelsin"]
print(viljad)

# Lisame mandariini listi lõppu
viljad.append("mandariin")
print(viljad[-1])

# vahetame listi esimese liikme pirni vastu
viljad[0] = "pirn"
print(viljad)

# Loeme mitu eset on listis
print("Listis on " + str(len(viljad)) + " puuvilja")

# Eemaldame listis ühe eseme suvaliselt
stopp = len(viljad)
del viljad[randint(0,stopp - 1)]
print(viljad)

# Otsime listist kirssi
if "kirss" in viljad:
    print("Kirss leitud!")
else:
    print("Kirssi pole! :(")

# Põõrame listi vastupidiseks
viljad.reverse()
print(viljad)

# Sorteerime listi
viljad.sort()
print(viljad)