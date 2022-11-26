import numpy
import matplotlib.pyplot as plt

# Runge-Kutta
# y[n + 1] = y[n] + h(k[1] + 2k[2] + 2k[3] + k[4])/6
# k[1] = f(t[n], y[n])      k[2] = f(t[n] + h/2, y[n] + hk[1]/2)
# k[3] = f(t[n] + h/2, y[n] + hk[2]/2)      k[4] = f(t[n] + h, y[n] + hk[3])
n, h = 50, 0.01
a, b, c = 10, 8/3, 28
def f(x, y, z):
    return [a * (y - x), -x * z + c * x - y, x * y - b * z]

N = int(n / h)
X = numpy.zeros([N, 1])
Y = numpy.zeros([N, 1])
Z = numpy.zeros([N, 1])
X[0], Y[0], Z[0] = 2, 2, 10

for i in range(0, N - 1):
    x, y, z = X[i], Y[i], Z[i]
    X1, Y1, Z1 = f(x, y, z)
    x, y, z = X[i] + X1 * h / 2, Y[i] + Y1 * h / 2, Z[i] + Z1 * h / 2
    X2, Y2, Z2 = f(x, y, z)
    x, y, z = X[i] + X2 * h / 2, Y[i] + Y2 * h / 2, Z[i] + Z2 * h / 2
    X3, Y3, Z3 = f(x, y, z)
    x, y, z = X[i] + X3 * h, Y[i] + Y3 * h, Z[i] + Z3 * h
    X4, Y4, Z4 = f(x, y, z)

    X[i + 1], Y[i + 1], Z[i + 1] = X[i] + h * (X1 + 2 * X2 + 2 * X3 + X4) / 6, \
        Y[i] + h * (Y1 + 2 * Y2 + 2 * Y3 + Y4) / 6, Z[i] + h * (Z1 + 2 * Z2 + 2 * Z3 + Z4) / 6

plt.plot(X)
plt.show()


