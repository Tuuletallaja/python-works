from random import randint
print("Tere tulemas mängima mängu kivi-paber-käärid")
print("Sinu vastaseks on arvuti")

fin = 0               


while fin != 2:
    a_valik = randint(1,3)
    m_valik = 0

    while m_valik not in (1,2,3):
        print("""Vali kas:
        1 - KIVI
        2 - PABER
        3 - KÄÄRID""") 
        kpk = input()
        try:
            m_valik = int(kpk)
        except:
            kpk = 0
        m_valik = int(kpk)
        if m_valik not in (1,2,3):
            print("Sellist valikut ei ole, proovi uuesti.")


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
    
    cont = 0
    while cont not in (1,2):
        print("""
Tahad sa veel mängida?
    1 - JAH
    2 - EI""")
        cont = input()
        try:
            cont = int(cont)
        except:
            cont = 0
        cont = int(cont)
        
    
    if cont == 2:
        fin = 2
    else:
        print("Jätkame mängu!")