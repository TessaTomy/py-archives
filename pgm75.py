import numpy as np
import matplotlib.pyplot as plt

# Generate samples
samples = np.random.normal(loc=10, scale=3, size=1000)

# Plot histogram
plt.hist(samples, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of 1000 Samples from N(10, 3²)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
