class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne, tachometr):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne
        self.tachometr = tachometr

    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            self.dostupne == False
            return "Vozidlo není k dispozici."
        
    def get_info(self):
        return f"Auto {self.typ_vozidla} ma SPZ {self.registracni_znacka} a {self.dostupne}."
    
    '''def vrat_auto(self, tachometr, delka_vypujceni):
        self.dostupne = True
        cena_vypujceni = 0
        delka_vypujceni = int(input("Kolik dni bylo auto pujcene? "))
        if delka_vypujceni >= 7:
            return cena_vypujceni == 400 * delka_vypujceni
        else:
            return cena_vypujceni == 300 * delka_vypujceni'''


auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True, 26382)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253, True, 36528)

auto = input("Jakou znacku auta si prejete? ").title()
if auto == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif auto == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
else:
    print(f"Nemame takove auto.")

print(auto1.get_info())
print(auto2.get_info())
