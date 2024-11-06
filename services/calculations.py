import numpy as np


# Функція для обчислення параметрів лінійної регресії
def linear_regression(x, y):
    # Кількість точок
    n = len(x)
    
    # Обчислюємо параметри лінії регресії
    m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2)
    b = (np.sum(y) - m * np.sum(x)) / n
    
    return m, b