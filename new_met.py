import numpy as np
import scipy as sc
import sympy as sp
import matplotlib.pyplot as plt

# Numero de iteraciones
i = 10

# Calculo de las derivadas parciales primeras y segundas
x, y = sp.symbols('x y')
f = 100*(y - x**2)**2 + (1 - x)**2
df1 = sp.diff(f, x)
df2 = sp.diff(f, y)
df11 = sp.diff(f, x, x)
df22 = sp.diff(f, y, y)
df12 = sp.diff(f, x, y)
df21 = sp.diff(f, y, x)
g1 = sp.lambdify([x, y], df1)
g2 = sp.lambdify([x, y], df2)
g11 = sp.lambdify([x, y], df11)
g22 = sp.lambdify([x, y], df22)
g12 = sp.lambdify([x, y], df12)
g21 = sp.lambdify([x, y], df21)

# Representacion de la funcion
fun = lambda x: 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2
res = 100                        
_X = np.linspace(-1, 2, res)
_Y = np.linspace(-1, 2, res)
_Z = np.zeros((res, res))

for ix, x in enumerate(_X):
    for iy, y in enumerate(_Y):
        _Z[iy, ix] = fun([x, y])

fig = plt.figure()
plt.contour(_X, _Y, _Z, 100)
plt.colorbar()
plt.plot(1, 1, "o", c="red")
#plt.show()

# Generacion del punto inicial
#x = np.random.rand(2) * 3 - 1
x = [0, 1]
plt.plot(x[0], x[1], "o", c="orange")
#plt.show()

# Metodo de Newton
lr = 0.001
for i in range(i):
    _x = np.copy(x)
    h = np.array([[g11(_x[0], _x[1]), g12(_x[0], _x[1])],[g21(_x[0], _x[1]), g22(_x[0], _x[1])]])
    ih = np.linalg.inv(h)
    x[0] = x[0] - lr * (g1(_x[0], _x[1])*ih[0,0] + g1(_x[0], _x[1])*ih[0,1])
    x[1] = x[1] - lr * (g2(_x[0], _x[1])*ih[1,0] + g2(_x[0], _x[1])*ih[1,1])
    plt.plot(x[0], x[1], "o", c="yellow")

plt.show()