import math

#prvni funkce
def overeni_cisla(cislo):
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13:
        predvolba = cislo[:4]
        if predvolba == "+420":
            return True
        else: return False
    else:
        return False

#druha funkce

def cena_SMS(text):
    cena_za_180 = 3
    pocet_zprav = math.ceil(len(text)/180)
    cena = cena_za_180 * pocet_zprav
    return cena

zadane_cislo = input("Zadej telefonni cislo: ")
if overeni_cisla(zadane_cislo) == True:
    SMS_zprava = input("Napis zpravu, kterou chces poslat: ")
    print(f"Zprava SMS te bude stat {cena_SMS(SMS_zprava)} korun.")
else:
    print("Zadane cislo je spatne. Zkus to znovu.")