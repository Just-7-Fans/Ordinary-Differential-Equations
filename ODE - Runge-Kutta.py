import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Runge-Kutta
# y[n + 1] = y[n] + h(k[1] + 2k[2] + 2k[3] + k[4])/6
# k[1] = f(t[n], y[n])      k[2] = f(t[n] + h/2, y[n] + hk[1]/2)
# k[3] = f(t[n] + h/2, y[n] + hk[2]/2)      k[4] = f(t[n] + h, y[n] + hk[3])
n, h = 50, 0.01
a, b, c = 10, 8/3, 28
def f(x, y, z):
    return [a * (y - x), -x * z + c * x - y, x * y - b * z]

def Runge_Kutta(_x, _y, _z):
    x, y, z = _x, _y, _z
    X1, Y1, Z1 = f(x, y, z)
    x, y, z = _x + X1 * h / 2, _y + Y1 * h / 2, _z + Z1 * h / 2
    X2, Y2, Z2 = f(x, y, z)
    x, y, z = _x + X2 * h / 2, _y + Y2 * h / 2, _z + Z2 * h / 2
    X3, Y3, Z3 = f(x, y, z)
    x, y, z = _x + X3 * h, _y + Y3 * h, _z + Z3 * h
    X4, Y4, Z4 = f(x, y, z)

    return [_x + h * (X1 + 2 * X2 + 2 * X3 + X4) / 6, \
        _y + h * (Y1 + 2 * Y2 + 2 * Y3 + Y4) / 6, _z + h * (Z1 + 2 * Z2 + 2 * Z3 + Z4) / 6]
    
N = int(n / h)
X, Y, Z = numpy.zeros([N, 1]), numpy.zeros([N, 1]), numpy.zeros([N, 1])
# X_, Y_, Z_ = numpy.zeros([N, 1]), numpy.zeros([N, 1]), numpy.zeros([N, 1])
X[0], Y[0], Z[0] = 2, 2, 10
# X_[0], Y_[0], Z_[0] = 2, 2, 10.01

for i in range(0, N - 1):
    X[i + 1], Y[i + 1], Z[i + 1] = Runge_Kutta(X[i], Y[i], Z[i])
    # X_[i + 1], Y_[i + 1], Z_[i + 1] = Runge_Kutta(X_[i], Y_[i], Z_[i])

plt.plot(X)
#plt.plot(X, label = r'$x_1(t)$')
#plt.plot(X_, label = r'$x_2(t)$')
#plt.plot(Y, label = 'y(t)', color = '#2ca02c')
#plt.plot(Z, label = 'z(t)', color = '#ff7f0e')
#plt.legend()
plt.show()

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(X, Y, Z)
plt.show()