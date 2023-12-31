teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#1 Vytvoř seznam průměrných teplot pro každý den.
def average(lst):
    return sum(lst) / len(lst)

prumer = [average(teplota) for teplota in teploty]
print(prumer)

#2 Vytvoř seznam ranních teplot.
ranni_teplota = [teplota[0] for teplota in teploty]
print(ranni_teplota)

#3 Vytvoř seznam nočních teplot.
nocni_teplota = [teplota[-1] for teplota in teploty]
print(nocni_teplota)

#4 Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
poledni_nocni_teplota = [[teplota[1], teplota[-1]] for teplota in teploty]
print(poledni_nocni_teplota)

