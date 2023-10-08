sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

# key = kód součástky 
# value = počet součástek na skladě

kod_soucastky = input("Jaky kod ma soucastka? ")
kod_soucastky = kod_soucastky.upper()   #vadila mi velka pismena v kodu soucastky, tak jsem si to vylepsila
mnozstvi = int(input("Kolik kusu potrebujes? "))

#Varianta 1
if not kod_soucastky in sklad:
    print("Součástka není skladem.")

#Varianta 2
if kod_soucastky in sklad:
    if (sklad[kod_soucastky]) <= mnozstvi:
        print(f"Muzu prodat jen {sklad[kod_soucastky]} kusu.")
        del sklad[kod_soucastky]
    #else:
     #   print("Nakup neprobehl.")

#print(sklad)

#Varianta 3

if kod_soucastky in sklad:
    if (sklad[kod_soucastky]) >= mnozstvi:
         print("Soucastku pridavam do objednavky.")
         sklad[kod_soucastky] -= mnozstvi
    #else:
        #print("Nakup neprobehl.")
#print(sklad)

#else a print(sklad) tam mam pro kontrolu, jestli vse funguje