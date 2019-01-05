aasta = int(input("Liigaasta kontroll, sisesta aasta: "))

if aasta % 4 == 0:
    if aasta % 100 == 0:
        if aasta % 400 == 0:
            print(str(aasta) + " on liigaasta!")
        else:
            print(str(aasta) + " ei ole liigaasta!")
    else:
        print(str(aasta) + " on liigaasta!")
else:
    print(str(aasta) + " ei ole liigaasta!")

if aasta % 4 == 0 and aasta % 100 != 0 or aasta % 400 == 0:
    print(str(aasta) + " on liigaasta!")
else:
    print(str(aasta) + " ei ole liigaasta!")