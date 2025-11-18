import numpy as np
import matplotlib.pyplot as plt


# Функция трапециевидной принадлежности с учетом бесконечных границ
def trapezoid(x, a, b, c, d):
    y = np.zeros_like(x)
    for i, xi in enumerate(x):
        if xi <= b and a == -np.inf:  # левое "бесконечное" плечо
            y[i] = 1
        elif xi >= c and d == np.inf:  # правое "бесконечное" плечо
            y[i] = 1
        elif a < xi <= b:
            y[i] = (xi - a) / (b - a + 1e-9)
        elif b < xi <= c:
            y[i] = 1
        elif c < xi <= d:
            y[i] = (d - xi) / (d - c + 1e-9)
        else:
            y[i] = 0
    return y


# Диапазон температуры (в градусах Цельсия)
x = np.linspace(-10, 45, 600)

# Параметры трапеций (a, b, c, d)
sets = {
    "Холодно": (-np.inf, -5, 5, 10),
    "Прохладно": (5, 10, 15, 20),
    "Комфортно": (15, 20, 25, 30),
    "Жарко": (25, 30, 35, np.inf),
}

# Построение графиков
plt.figure(figsize=(10, 6))
for name, (a, b, c, d) in sets.items():
    y = trapezoid(x, a, b, c, d)
    plt.plot(x, y, label=name, linewidth=2)

# Настройки графика
plt.title(
    "Функции принадлежности для лингвистической переменной 'Комфортность температуры'"
)
plt.xlabel("Температура, °C")
plt.ylabel("Степень принадлежности μ(x)")
plt.legend()
plt.grid(True)
plt.show()
