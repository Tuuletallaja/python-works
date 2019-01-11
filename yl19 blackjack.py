from random import randint
from random import shuffle
from time import sleep
from os import system
from os import name

def hit_player():
        c_count = len(cardpack)
        r_numb = randint(0, c_count - 1)
        card = cardpack[r_numb]
        c_text = card[0]
        c_value = card[1]
        c_card = card[2]
        p_cards.append(c_text)
        p_score.append(c_value)
        p_hand.append(c_card)
        del cardpack[r_numb]

def hit_dealer():
        c_count = len(cardpack)
        r_numb = randint(0, c_count - 1)
        card = cardpack[r_numb]
        c_text = card[0]
        c_value = card[1]
        c_card = card[2]
        d_cards.append(c_text)
        d_score.append(c_value)
        d_hand.append(c_card)
        del cardpack[r_numb]

def d_bust_control():
    if sum(d_score) > 21:
        if 11 in d_score:
            x = d_score.index(11)
            d_score[x] = 1

def p_bust_control():
    if sum(p_score) > 21:
        if 11 in p_score:
            x = p_score.index(11)
            p_score[x] = 1    

def clear():
    system('cls' if name == 'nt' else 'clear')

def p_read():
    print("Sul on käes: ")
    for c in p_cards:
        print(c)
    print(" ")
    print("Sinu kaardite summa on " + str(sum(p_score)))





print("""Tere tulemast mängima Blackjacki.""")

wallet = 0
while wallet <= 0:
    print("Kui suure summa sa lauda tood, et mängida:")
    wallet = input()
    try:
        wallet = int(wallet)
    except:
        wallet = 0
    wallet = int(wallet)
    clear()
clear()

menu = 0
choice = []
p_hand = []
d_hand = []
count = 0
p_cards = []
p_score = []
d_score = []
d_cards = []
game = 1
hit = 1
bet = 0

new_cardpack = [("Ruutu 2",2,2),("Ruutu 3",3,3),("Ruutu 4",4,4),("Ruutu 5",5,5),("Ruutu 6",6,6),("Ruutu 7",7,7),("Ruutu 8",8,8),("Ruutu 9",9,9),("Ruutu 10",10,10),("Ruutu poiss",10,11),("Ruutu emand",10,12),("Ruutu kuningas",10,13),("Ruutu äss",11,14),("Poti 2",2,2),("Poti 3",3,3),("Poti 4",4,4),("Poti 5",5,5),("Poti 6",6,6),("Poti 7",7,7),("Poti 8",8,8),("Poti 9",9,9),("Poti 10",10,10),("Poti poiss",10,11),("Poti emand",10,12),("Poti kuningas",10,13),("Poti äss",11,14),("Risti 2",2,2),("Risti 3",3,3),("Risti 4",4,4),("Risti 5",5,5),("Risti 6",6,6),("Risti 7",7,7),("Risti 8",8,8),("Risti 9",9,9),("Risti 10",10,10),("Risti poiss",10,11),("Risti emand",10,12),("Risti kuningas",10,13),("Risti äss",11,14),("Ärtu 2",2,2),("Ärtu 3",3,3),("Ärtu 4",4,4),("Ärtu 5",5,5),("Ärtu 6",6,6),("Ärtu 7",7,7),("Ärtu 8",8,8),("Ärtu 9",9,9),("Ärtu 10",10,10),("Ärtu poiss",10,11),("Ärtu emand",10,12),("Ärtu kuningas",10,13),("Ärtu äss",11,14)]

cardpack = [("Ruutu 2",2,2),("Ruutu 3",3,3),("Ruutu 4",4,4),("Ruutu 5",5,5),("Ruutu 6",6,6),("Ruutu 7",7,7),("Ruutu 8",8,8),("Ruutu 9",9,9),("Ruutu 10",10,10),("Ruutu poiss",10,11),("Ruutu emand",10,12),("Ruutu kuningas",10,13),("Ruutu äss",11,14),("Poti 2",2,2),("Poti 3",3,3),("Poti 4",4,4),("Poti 5",5,5),("Poti 6",6,6),("Poti 7",7,7),("Poti 8",8,8),("Poti 9",9,9),("Poti 10",10,10),("Poti poiss",10,11),("Poti emand",10,12),("Poti kuningas",10,13),("Poti äss",11,14),("Risti 2",2,2),("Risti 3",3,3),("Risti 4",4,4),("Risti 5",5,5),("Risti 6",6,6),("Risti 7",7,7),("Risti 8",8,8),("Risti 9",9,9),("Risti 10",10,10),("Risti poiss",10,11),("Risti emand",10,12),("Risti kuningas",10,13),("Risti äss",11,14),("Ärtu 2",2,2),("Ärtu 3",3,3),("Ärtu 4",4,4),("Ärtu 5",5,5),("Ärtu 6",6,6),("Ärtu 7",7,7),("Ärtu 8",8,8),("Ärtu 9",9,9),("Ärtu 10",10,10),("Ärtu poiss",10,11),("Ärtu emand",10,12),("Ärtu kuningas",10,13),("Ärtu äss",11,14)]

c_count = len(cardpack)         # Number of cards in pack
shuffle(cardpack)        

while game != 2:

    while bet <= 0:
        clear()
        print("Sul on laual " + str(wallet) + " eurot.")
        print("Kui suure panusega sa soovid mängida: ")
        bet = input()
        try:
            bet = int(bet)
        except:
            bet = 0
        bet = int(bet)
        if bet > wallet:
            print(" ")
            print("Sul ei ole nii palju raha, tee sobiv panus.")
            bet = 0
            sleep(2)
    wallet = wallet - bet
    clear()

    print("""Diiler  jagab nüüd kaardid laiali.""")

    # First round of dealing cards
    t = 0
    while t <= 1:
        t = t + 1                    
        hit_player()
        hit_dealer()
    sleep(1)
    clear()

    if sum(p_score) == 21:
        print("Sul on käes: ")
        for c in p_cards:
            print(c)
        print(" ")
        print("Diileri üks kaart on laual varjatud, nähtav kaart on " + str(d_cards[0]))
        print(" ")
        print("Blackjack!")
        print("Sinu kaardite summa on " + str(sum(p_score)))

        if sum(d_score) == 21:
            print(" ")  
            print("Diileri kaardid on")
            for c in d_cards:
                print(c)
            print(" ")
            print("Nende summa on " + str(sum(d_score)))
            print(" ")
            print("Diileril on samuti Blackjack, jäite viiki.")
            wallet = wallet + bet
        else:
            print("Diileri kaardid on")
            for c in d_cards:
                print(c)
            d_bust_control()
            print(" ")
            print("Nende summa on " + str(sum(d_score)))
            print(" ")
            print("""Palju õnne! Sa võitsid ja väljamakse diileri poolt on boonusega!""")
            wallet = wallet + (bet * 3)
    
    else:
        p_bust_control()
        d_bust_control()

        call = int()
        while call not in choice:
            clear()
            print("Sul on käes: ")
            for c in p_cards:
                print(c)
            print(" ")
            print("Diileri üks kaart on laual varjatud, nähtav kaart on " + str(d_cards[0]))
            print(" ")
            print("Sinu kaardite summa on " + str(sum(p_score)))
            print("Diileri nähtava kaardi väärtus on " + str(d_score[0]))
            print("""
Sinu võimalused on:
            """)

            if sum(p_score) in range(9,12):
                print(str("[D]ouble down - Kahekordistad oma panuse ja võtad juurde ühe kaardi. Selles ringis rohkem kaarte juurde ei saa."))
                choice.append("d")
            if p_hand[0] == p_hand[1]:
                print(str("[S]plit - Jagad esialgse käe kaheks, saades kaks uut kätt ja panustad mõlema käe kohta algse käe panuse."))
                choice.append("s")
            print(str("[H]it - Võtad ühe kaardi juurde."))
            choice.append("h")
            print(str("S[t]and - Ei võta rohkem kaarte ja diiler mängib oma kaardid."))
            choice.append("t")

            call_raw = input()
            call_raw = call_raw.lower()
            try:
                call = str(call_raw)
            except:
                call_raw = str()
                call = str()
            call = call_raw
            clear()
        
        if call == "d":
            wallet = wallet - bet
            bet = bet * 2
            hit_player()
            p_bust_control()
            print("Sinu uus panus on " + str(bet) + " eurot.")
            p_read()
            
            if sum(p_score) > 21:
                print(" ")
                print("""Sinu "käsi" on lõhki ja diiler võitis.""")
                print("Diileri kaardid olid")
                for c in d_cards:
                    print(c)
                print(" ")
                print("Diileri kaartide väärtus oli " + str(sum(d_score)))
            
            else:
                print(" ")
                print("Diileri kaardid on")
                while sum(d_score) <= 16:
                    hit_dealer()
                    if sum(d_score) > 21:
                        d_bust_control()
                for c in d_cards:
                    print(c)
                print(" ")
                print("Nende summa on " + str(sum(d_score)))

                if sum(p_score) == sum(d_score):
                    print(" ")
                    print("Jäite viiki.")
                    print("Diiler tagastab sinu panuse.")
                    wallet = wallet + bet
                elif sum(p_score) < sum(d_score) and sum(d_score) <= 21:
                    print("Kahjuks kaotasid.")
                else:
                    print("Palju õnne! Sa võitsid.")
                    wallet = wallet + (bet * 2)
        
        elif call == "s":
            wallet = wallet + bet
            break

        elif call == "h":
            hit_player()
            p_bust_control()
            clear()
            y = 0

            while y not in ("h","t"):
                clear()
                p_bust_control()
                p_read()
                if sum(p_score) >= 21:
                    y = 2
                    break
                print(" ")
                print("Diileri kaardi väärtus on " + str(d_score[0]))
                print(" ")
                print("Sul on kaks valikut.")
                print("[H]it - Võtad ühe kaardi juurde.")
                print("S[t]and - Ei võta rohkem kaarte ja diiler mängib oma kaardid.")
                y = input()
                try:
                    y = str(y)
                except:
                    y = str()
                if y == "h":
                    hit_player()
                elif y == "t":
                    break
                else:
                    y = str()

            if sum(p_score) > 21:
                clear()
                p_read()
                print(" ")
                print("""Sinu "käsi" on lõhki ja diiler võitis.""")
                print(" ")
                print("Diileri kaardid olid")
                for c in d_cards:
                    print(c)
                print(" ")
                print("Diileri kaartide väärtus oli " + str(sum(d_score)))
            
            else:
                clear()
                p_read()
                print(" ")
                print("Diileri kaardid on")
                while sum(d_score) <= 16:
                    hit_dealer()
                    if sum(d_score) > 21:
                        d_bust_control()
                for c in d_cards:
                    print(c)
                print(" ")
                print("Nende summa on " + str(sum(d_score)))

                if sum(p_score) == sum(d_score):
                    print(" ")
                    print("Jäite viiki.")
                    print("Diiler tagastab sinu panuse.")
                    wallet = wallet + bet
                elif sum(p_score) < sum(d_score) and sum(d_score) <= 21:
                    print(" ")
                    print("Kahjuks kaotasid.")
                else:
                    print(" ")
                    print("Palju õnne! Sa võitsid.")
                    wallet = wallet + (bet * 2)
        
        else:
            p_read()
            print(" ")
            print("Diileri kaardid on")
            while sum(d_score) <= 16:
                hit_dealer()
                if sum(d_score) > 21:
                    d_bust_control()
            for c in d_cards:
                print(c)
            print(" ")
            print("Nende summa on " + str(sum(d_score)))
            print(" ")

            if sum(p_score) == sum(d_score):
                print("Jäite viiki.")
                print("Diiler tagastab sinu panuse.")
                wallet = wallet + bet
            elif sum(p_score) < sum(d_score) and sum(d_score) <= 21:
                print("Kahjuks kaotasid.")
            else:
                print("Palju õnne! Sa võitsid.")
                wallet = wallet + (bet * 2)



    
    close = int()
    while close not in (1,2):
        if wallet <= 0:
            game = 2
            print(" ")
            print("Kahjuks on sul raha otsas, nii et mäng on läbi.")
            print("Head aega!")
            sleep(2)
            break
        else:
            while close not in (1,2):
                print(" ")
                print("""Kas soovid mängu jätkata? 
                1 - JAH
                2 - EI""")
                close = input()
                try:
                    close = int(close)
                except:
                    close = int()
                close = int(close)
            if close == 1:
                game = 1
                bet = 0
                p_cards.clear()
                p_score.clear()
                d_cards.clear()
                d_score.clear()
                clear()
                if len(cardpack) < 15:
                    del cardpack[:]
                    cardpack.extend(new_cardpack)
                    shuffle(cardpack)
                    print("Diiler korjas mängukaardid kokku ja segas paki uuesti ära.")
                    sleep(3)
                    
            else:
                game = 2
                print("Head aega!")
                print("Sa lahkud mängust " + str(wallet) + " euroga.")
                sleep(2)
                break
