print("Palun sisesta tekst, millset täishäälikuid otsida.")
tekst = str(input())
tekst.lower()               # Muudan kõik väiketähtedeks
tähed = list(tekst)         # Panen iga kirjamärgi eraldi listi

while " " in tähed:         # Eemaldan listist tühikud 
    tähed.remove(" ")
    
täishäälikud = ["a","e","i","o","u","õ","ä","ö","ü"]

for t in täishäälikud:
    n = tähed.count(t)
    if n == 1:
        print("Tekstis on " + str(n) + " " + t + " täht.")
    else:
        print("Tekstis on " + str(n) + " " + t + " tähte.")

