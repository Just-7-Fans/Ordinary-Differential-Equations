import numpy
import matplotlib.pyplot as plt

# k[1] = g(y[n])
# k[2] = g(y[n] + 2hk[1] / 3)
# y[n + 1] = y[n] + h(k[1] + 3k[2]) / 4

# van der Pol: y" - (1 - y^2)y' + y = 0
# y' = z    z' = (1 - y^2)z - y

def f(y, z):
    return [z, (1 - y ** 2) * z - y]

n, h = 50, 0.01
N = int(n / h)
Y = numpy.zeros([N, 1])
Z = numpy.zeros([N, 1])
Y[0], Z[0] = 0, 2

for i in range(0, N - 1):
    y, z = Y[i], Z[i]
    Y1, Z1 = f(y, z)
    y, z = Y[i] + 2 * Y1 * h / 3, Z[i] + 2 * Z1 * h / 3
    Y2, Z2 = f(y, z)

    Y[i + 1], Z[i + 1] = Y[i] + h * (Y1 + 3 * Y2) / 4, Z[i] + h * (Z1 + 3 * Z2) / 4

plt.plot(Y, label = 'y(x)')
plt.plot(Z, label = 'y\'(x)')
plt.legend()
plt.show()

plt.plot(Y, Z)
plt.show()