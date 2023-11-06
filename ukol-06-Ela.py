class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def pujc_auto(self):
        if self.dostupne == True:
            return "Potvrzuji zapůjčení vozidla."
            self.dostupne = False
        else:
            self.dostupne == False
            return "Vozidlo není k dispozici."
        
    def get_info(self):
        return f"Auto {self.typ_vozidla} ma SPZ {self.registracni_znacka}."

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253, True)

auto = input("Jakou znacku auta si prejete? ")
if auto == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif auto == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
else:
    print(f"Nemame takove auto.")