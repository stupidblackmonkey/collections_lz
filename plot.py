import matplotlib.pyplot as plt
import numpy as np
import random

kolichestvo_tochek = random.randint(20, 100) # Случайное количество точек от 20 до 100

x = np.linspace(1, kolichestvo_tochek)  # кол-во иксов случайное от 20 до 100
y = x**3 - 3*x**2 - x + 3  # формула функции

plt.plot(x, y)  # делает график
plt.show()  # выводит график
