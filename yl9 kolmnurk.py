print("Palun sisesta kolmnurga külgede pikkused.")
a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))

# Koosatab nimekirja külgedest ja sorteerib küljed väiksemast suuremaks
sides = []          # List külgede pikkuste hoidmiseks
sides.append(a)     
sides.append(b)     # Paneb külje pikkused listi
sides.append(c)

sides.sort()        # Sorteerib listi

a = sides[0]
b = sides[1]        # Võtab listist väärtused välja
c = sides[2]


if a + b < c:      # Kontrollib, kas on võimalik antud külgedega kolmnurka moodustada
    print("Kahjuks ei ole võimlik antud külgedega kolmnurka moodustada.")
else:               # Määrab kolmnurga tüübi
    if a == b and b == c:
        print("Kolmnurk abc on võrdkülgne kolmnurk.")
    elif a == b and b != c:
        print("Kolmnurk abc on võrdhaarne kolmnurk.")
    else:
        print("Kolmnurk abc on erikülgne kolmnurk.")
