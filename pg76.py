import numpy as np
import matplotlib.pyplot as plt

values = np.array([23, 45, 12, 36, 29])
labels = np.array(['A', 'B', 'C', 'D', 'E'])

axs = plt.subplots(1, 3, figsize=(10, 5))[1]

axs[0].bar(labels, values, color='blue', edgecolor='black')

axs[1].barh(labels, values, color='red', edgecolor='black')

axs[2].pie(values, labels=labels, autopct='%.f%%', startangle=90)
plt.tight_layout()
plt.show()
