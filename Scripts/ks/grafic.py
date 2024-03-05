from statistics import mean
import matplotlib.pyplot as plt




n = [255, 127, 64, 32, 5, 0, 256]
delta_t = [3.279, 1.63, 0.82, 0.41, 0.064, 0, 3.3]


def least_squares(xdata, ydata):
    a = (sum([x * y for x, y in zip(xdata, ydata)]) - mean(ydata) * sum(xdata)) / (
                sum([x ** 2 for x in xdata]) - mean(xdata) * sum(xdata))
    b = mean(ydata) - a * mean(xdata)
# b = mean(ydata) - a * mean(xdata
    return a, b


print(least_squares(n, delta_t))

a, b = least_squares(n, delta_t)

fig, ax = plt.subplots()
ax.plot(n, delta_t, 'o', label="Экспериментальные данные")

xdata = [x for x in range(0, 260, 1)]
ax.plot(xdata, [a * x + b for x in xdata], label="Аппроксимация")
ax.legend()
ax.grid(True)
#plt.savefig("fig1.png")
plt.show()