import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-15, 15) #кол-во иксов = 30
y = x**3 - 3*x**2 - x + 3 #формула функции

plt.plot(x, y) #делает график

plt.show() #выводит график
