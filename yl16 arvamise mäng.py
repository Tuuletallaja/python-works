from random import randint
from time import sleep

print("""
Tere!
Arvuti valib välja suvalise arvu ja sa saad selle ära arvata.""")
pakkumine = int(input("Palun tee oma esimene pakkumine: " ))

arvatav_arv = randint(1,100)


while arvatav_arv != pakkumine:
    if pakkumine < arvatav_arv:
        print('Arvuti arv on suurem.')
        pakkumine = int(input("Palun tee uus pakkumine: " ))
    else:
        print("Arvuti arv on väiksem.")
        pakkumine = int(input("Palun tee uus pakkumine: " ))

print("""Palju õnne!
Sa pakkusid õigesti""")



