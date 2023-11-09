import pandas as pd

adopce_zvirat = pd.read_csv("data_zvirata.csv", sep=";", encoding="utf-8")

print(f"Tabulka ma {adopce_zvirat.shape[0]} radku a {adopce_zvirat.shape[1]} sloupcu.")
print(f"Sloupce se jmenuji takto: {adopce_zvirat.columns}")

cesky_nazev = adopce_zvirat["nazev_cz"].iloc[35]
anglicky_nazev = adopce_zvirat["nazev_en"].iloc[35]
print(f"Zvire s indexem 34 to: cesky - {cesky_nazev}, anglicky - {anglicky_nazev}.")

#Adopce kterých zvířat je nejdražší?

print(adopce_zvirat.sort_values(by="cena").iloc[-1])

#Které zvíře je alfabeticky poslední v češtině? Které v angličtině?
posledni_cz = adopce_zvirat.sort_values(by="nazev_cz").iloc[-1]
print(f"V cestine je alfabeticky posledni {posledni_cz}.")
posledni_en = adopce_zvirat.sort_values(by="nazev_en").iloc[-1]
print(posledni_en)