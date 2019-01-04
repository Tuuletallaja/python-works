from random import randint
from time import sleep

print("Arvuti püüab ära arvate sinu pakutud arvu. Mitu pakkumist tal läheb, et see ära arvata?")

arvatav_arv = int(input("Sisesta naturaalarv ühest sajani: "))
min_arv = 1
max_arv = 100
pakkumine = randint(min_arv,max_arv)

t = 0


# Arvuti valib arvu ja teeb pakkumise

while arvatav_arv != pakkumine:
    t = t + 1
    pakkumine = randint(min_arv,max_arv)
    
    print("Arvuti pakkus sinu arvuks " + str(pakkumine))
    sleep(0.7)
    if pakkumine < arvatav_arv:
        min_arv = pakkumine + 1
                
    else:
        max_arv = pakkumine - 1
        
print("Arvuti arvas ära sinu arvu! See oli " + str(pakkumine) + ". Tal kulus selleks " + str(t) + " arvamist.")
    



        
