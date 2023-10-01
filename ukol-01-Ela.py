# zadani 01
jmeno = ["Ela"]
for jmeno in jmeno:
    email = jmeno + "@czechitas.cz"
    print (email)

#Bonus
jmeno_a_prijmeni = input ("Zadej jmeno a prijmeni: ")
# velka pismena
velka_pismena = str.upper(jmeno_a_prijmeni)
print (velka_pismena)
# mala pismena
print(str.lower(jmeno_a_prijmeni))
# standardní varianta
print(str.title(jmeno_a_prijmeni))
# iniciály
print(str.upper(jmeno_a_prijmeni[0]) + ". ") 
#A tady uz nevim jak dal. At vymyslim co vymyslim, nefunguje to.