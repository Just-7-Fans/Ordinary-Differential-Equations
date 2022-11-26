# Numpy + Scipy + Matplotlib ~ Matlab
# https://www.runoob.com/matplotlib/matplotlib-tutorial.html
import matplotlib.pyplot as plt
#from matplotlib import rc
import numpy
from scipy.integrate import solve_ivp

#rc('text', usetex = True)
font0 = {'family': 'Times New Roman', 'size': 12}

# numpy.array -> NdArray
xpoints = numpy.array([0, 6])  # [0,6]
ypoints = numpy.array([6, 2, 13, 10])

# 2D Plot
'''
plt.plot(ypoints, 'o:r')  # red (circle connected with dashed line)
plt.xlabel("x - Label")
plt.ylabel("y - Label")
plt.show()
'''

# Bar
'''
x = numpy.array(["Bar1", "Bar2", "Bar3"])
y = numpy.array([19, 3, 11])
plt.bar(x, y, width = 0.5)  # barh -> horizontal bar
plt.show()
'''

# Ordinary Differential Equations
# y' = y * (y - 1) ^ 2 * (y - 3)
def odefun(t, y): # t First for solve_ivp
    return y * (y - 1) ** 2 * (y - 3)

y0 = [-1, 0.5, 2, 3]
t_span = (0, 2)
t = numpy.linspace(0, 2, 1000)

for i in range(4):
    sol = solve_ivp(odefun, t_span, [y0[i]], method = 'RK45', t_eval = t)
    plt.plot(sol.t, sol.y[0], label = 'y(0) = ' + str(y0[i])) 
plt.title(r"$y'=y(y-1)^2(y-3)$") # r guides LaTeX
plt.xlabel('Time t', loc = 'right')
plt.ylabel('Solution y', loc = 'top')
plt.legend()
plt.show()

# Verhulst Model / Logistic Model
a, M = 1, 10
def logistic(t, y):
    return a * (1 - y / M) * y

y0 = numpy.arange(2, 20, 2)
y0 = numpy.concatenate(([0.2, 0.5, 1], y0))
t_span = (0, 10)
t = numpy.linspace(0, 10, 1000)

for i in range(len(y0)):
    sol = solve_ivp(logistic, t_span, [y0[i]], method = 'RK45', t_eval = t)
    plt.plot(sol.t, sol.y[0], label = 'p(0) = ' + str(y0[i]))
plt.title(r"${p' = \alpha p(1-\frac{p}{M}) p}$" + '\n' + r"${\alpha = 1, M = 10}$")
plt.xlabel('Time t', loc = 'right')
plt.ylabel('Solution p', loc = 'top')
plt.legend()
plt.show()

# Lotka - Volterra Model
# x' = ax - bxy     y' = -cy + dxy
a, b, c, d = 2/3, 0.3, 1, 0.2
def predator(t, z):
    x, y = z # x = z[0], y = z[1]
    return [a * x - b * x * y, -c * y + d * x * y]

t_span = (0, 50)
t = numpy.linspace(0, 50, 1000)

sol = solve_ivp(predator, t_span, [10, 5], method = 'RK45', t_eval = t)
plt.plot(sol.t, sol.y[0], label = 'x(t)')
plt.plot(sol.t, sol.y[1], 'r--', label = 'y(t)')
plt.title('x\' = ax - bxy\ny\'= -cy + dxy')
plt.legend()
plt.show()