from random import randint
print("Tere tulemas mängima mängu kivi-paber-käärid")
print("Sinu vastaseks on arvuti")

fin = 1                     # 1 - mäng jätkub; 2 - mäng lõppeb


while fin == 1:
    a_valik = randint(1,3)
    print  ("""Vali kas:
    1 - KIVI
    2 - PABER
    3 - KÄÄRID""")            
    m_valik = int(input())

    if m_valik == 1:
        print("Valisid kivi.")
    elif m_valik == 2:
        print("Valisid paberi.")
    else:
        print("Valisid käärid.")
        
    if a_valik == 1:        #KIVI
        if m_valik == 1:
            print("Arvuti valis sammuti kivi. Jäite viiki.")
        elif m_valik == 2:
            print("Arvuti valis kivi. Sina võitsid")
        else:
            print("Arvuti valis kivi. Sina kaotasid.")
        
    elif a_valik == 2:      #PABER
        if m_valik == 1:
            print("Arvuti valis paberi. Sina kaotasid")
        elif m_valik == 2:
            print("Arvuti valis sammuti paberi. Jäite viiki.")
        else:
            print("Arvuti valis paberi. Sina võitsid")
    
    else:                   #KÄÄRID
        if m_valik == 1:
            print("Arvuti valis käärid. Sina võitsid.")
        elif m_valik == 2:
            print("Arvuti valis käärid. Sina kaotasid.")
        else:
            print("Arvuti valis käärid. Jäite viiki.")

    print("""Tahad sa veel mängida?
    1 - JAH
    2 - Ei""")
    fin = int(input())