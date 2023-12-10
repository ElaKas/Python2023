import pandas
import matplotlib.pyplot as plt

platy = pandas.read_csv("platy.csv", names=['cislo_zamestnance', 'plat'], index_col='cislo_zamestnance')

#plt.hist(platy)
#plt.show()

#nebo:
platy=platy.astype(float)
platy.plot.hist(bins=2000)
plt.show()
