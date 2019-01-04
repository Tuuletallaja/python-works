print("Tere!")
nimi = str(input("Kellega on mul au kohtuda? "))
nimi = nimi.lower()
nimi = nimi.capitalize()

print("Väga meeldiv " + nimi + "!")

kodu = str(input("Mis sinu kodu maakond on? "))
print(kodu)
kodu = kodu.lower()
saar = "saaremaa"

if kodu != saar:
    print("Oleks pakkunud, et sa oled Saaremaalt. Sa õhkad saare inimese energiat.")
else:
    print("Eesti viiking oled jah. Väga hea.")

vanus = int(input("Kui vana sa oled? "))

if vanus < 18:
    print("Kahjuks sa autoga sõita ei või")
elif vanus == 18:
    print("Palju õnne täisealiseks saamise puhul!")
else:
    print("Sa võid autoga sõita.")