import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-15, 15)
y = x**3 - 3*x**2 - x + 3

plt.plot(x, y)
plt.show()