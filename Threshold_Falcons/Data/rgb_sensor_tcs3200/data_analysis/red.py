# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

#paramètres utilisés sur chaque graph
N = 3
total = (100, 100, 100)
ind = np.arange(N)    
width = 0.40
fig = plt.figure()
fig.subplots_adjust(bottom=0.05, left=0.025, top = 0.9, right=0.95)     
tot = plt.bar(ind, total, width, color='w')

#pourcentage de RGB absorbé en lumière rouge
rouge = (1, 47,48)
R = plt.bar(ind, rouge, width, color = 'y')
plt.ylabel("Percentage")
plt.xlabel('Wavelenght domain')
plt.title('Percentage of absorbed RGB value for Red light')
plt.xticks(ind, ('Red', 'Green', 'Blue'))
plt.legend((tot[0], R[0]), ('Total', 'Absorbed percentage'))


plt.show()
