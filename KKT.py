import numpy as np
import scipy as sc
import sympy as sp
import matplotlib.pyplot as plt

# Representacion de la funcion
a = 3
fun = lambda x: (x[0]-a)**2 + (x[1]-2)**2
res = 100                        
_X = np.linspace(0, 7, res)
_Y = np.linspace(0, 7, res)
_Z = np.zeros((res, res))

for ix, x in enumerate(_X):
    for iy, y in enumerate(_Y):
        _Z[iy, ix] = fun([x, y])

fig = plt.figure()
plt.contour(_X, _Y, _Z, 100)
plt.colorbar()
#plt.show()

# Representacion de las restricciones
r1 = lambda x: x[0]**2 + x[1]**2 - 5
_X = np.linspace(0, 7, res)
_Y = np.linspace(0, 7, res)
_Z = np.zeros((res, res))
for ix, x in enumerate(_X):
    for iy, y in enumerate(_Y):
        _Z[iy, ix] = r1([x, y])
plt.contour(_X, _Y, _Z, 0, colors=['#c74040'])

r2 = lambda x: 2*x[0] + x[1] - 6
_X = np.linspace(0, 7, res)
_Y = np.linspace(0, 7, res)
_Z = np.zeros((res, res))
for ix, x in enumerate(_X):
    for iy, y in enumerate(_Y):
        _Z[iy, ix] = r2([x, y])
plt.contour(_X, _Y, _Z, 0, colors=['#3dd426'])

r3 = lambda x: x[0] + 2*x[1] - 4
_X = np.linspace(0, 7, res)
_Y = np.linspace(0, 7, res)
_Z = np.zeros((res, res))
for ix, x in enumerate(_X):
    for iy, y in enumerate(_Y):
        _Z[iy, ix] = r3([x, y])
plt.contour(_X, _Y, _Z, 0, colors=['#3dd426'])

r4 = lambda x: x[0]
_X = np.linspace(-0.5, 7, res)
_Y = np.linspace(-0.5, 7, res)
_Z = np.zeros((res, res))
for ix, x in enumerate(_X):
    for iy, y in enumerate(_Y):
        _Z[iy, ix] = r4([x, y])
plt.contour(_X, _Y, _Z, 0, colors=['#2686d4'])

r5 = lambda x: x[1]
_X = np.linspace(-0.5, 7, res)
_Y = np.linspace(-0.5, 7, res)
_Z = np.zeros((res, res))
for ix, x in enumerate(_X):
    for iy, y in enumerate(_Y):
        _Z[iy, ix] = r5([x, y])
plt.contour(_X, _Y, _Z, 0, colors=['#2686d4'])
#plt.show()

# Calculo de las combinaciones de restricciones
x, y, m = sp.symbols('x y m')
fun = lambda x, y: (x-a)**2 + (y-2)**2

f = (x-a)**2 + (y-2)**2 + m * (x**2 + y**2 - 5)
df1 = sp.diff(f, m)
df2 = sp.diff(f, x)
df3 = sp.diff(f, y)
sols = sp.solve((df1, df2, df3), (x, y, m), dict = True)
v1 = fun(sols[0][x], sols[0][y])
v2 = fun(sols[1][x], sols[1][y])
mv = min(v1, v2)
s2 = mv
print('El valor minimo de la funcion en los puntos obtenidos en la segunda combinacion es: '+ str(mv))
if mv == v1:
    plt.plot(sols[0][x], sols[0][y], "o", c="black")
else:
    plt.plot(sols[1][x], sols[1][y], "o", c="black")

f = (x-a)**2 + (y-2)**2 + m * (x + 2*y -4)
df1 = sp.diff(f, m)
df2 = sp.diff(f, x)
df3 = sp.diff(f, y)
sols = sp.solve((df1, df2, df3), (x, y, m))
s3 = fun(sols[x], sols[y])
print('El valor de la funcion en el punto obtenido en la tercera combinacion es: '+ str(fun(sols[x], sols[y])))
plt.plot(sols[x], sols[y], "o", c="black")

f = (x-a)**2 + (y-2)**2 + m * x
df1 = sp.diff(f, m)
df2 = sp.diff(f, x)
df3 = sp.diff(f, y)
sols = sp.solve((df1, df2, df3), (x, y, m))
s4 = fun(sols[x], sols[y])
print('El valor de la funcion en el punto obtenido en la cuarta combinacion es: '+ str(fun(sols[x], sols[y])))
plt.plot(sols[x], sols[y], "o", c="black")

f = (x-a)**2 + (y-2)**2 + m * y
df1 = sp.diff(f, m)
df2 = sp.diff(f, x)
df3 = sp.diff(f, y)
sols = sp.solve((df1, df2, df3), (x, y, m))
s5 = fun(sols[x], sols[y])
print('El valor de la funcion en el punto obtenido en la quinta combinacion es: '+ str(fun(sols[x], sols[y])))
plt.plot(sols[x], sols[y], "o", c="black")

f1 = x + 2*y - 4
f2 = x**2 + y**2 - 5
sols = sp.solve((f1, f2), (x, y), dict = True)
v1 = fun(sols[0][x], sols[0][y])
v2 = fun(sols[1][x], sols[1][y])
mv = min(v1, v2)
s6 = mv
print('El valor minimo de la funcion en los puntos obtenidos en la sexta combinacion es: '+ str(mv))
if mv == v1:
    plt.plot(sols[0][x], sols[0][y], "o", c="blue")
else:
    plt.plot(sols[1][x], sols[1][y], "o", c="blue")

f1 = x
f2 = x**2 + y**2 - 5
sols = sp.solve((f1, f2), (x, y), dict = True)
v1 = fun(sols[0][x], sols[0][y])
v2 = fun(sols[1][x], sols[1][y])
mv = min(v1, v2)
s7 = mv
print('El valor minimo de la funcion en los puntos obtenidos en la septima combinacion es: '+ str(mv))
if mv == v1:
    plt.plot(sols[0][x], sols[0][y], "o", c="black")
else:
    plt.plot(sols[1][x], sols[1][y], "o", c="black")

f1 = y
f2 = x**2 + y**2 - 5
sols = sp.solve((f1, f2), (x, y), dict = True)
v1 = fun(sols[0][x], sols[0][y])
v2 = fun(sols[1][x], sols[1][y])
mv = min(v1, v2)
s8 = mv
print('El valor minimo de la funcion en los puntos obtenidos en la octava combinacion es: '+ str(mv))
if mv == v1:
    plt.plot(sols[0][x], sols[0][y], "o", c="red")
else:
    plt.plot(sols[1][x], sols[1][y], "o", c="red")

f1 = x + 2*y - 4
f2 = x
sols = sp.solve((f1, f2), (x, y))
s9 = fun(sols[x], sols[y])
print('El valor de la funcion en el punto obtenido en la novena combinacion es: '+ str(fun(sols[x], sols[y])))
plt.plot(sols[x], sols[y], "o", c="red")

f1 = x + 2*y - 4
f2 = y
sols = sp.solve((f1, f2), (x, y))
s10 = fun(sols[x], sols[y])
print('El valor de la funcion en el punto obtenido en la decima combinacion es: '+ str(fun(sols[x], sols[y])))
plt.plot(sols[x], sols[y], "o", c="black")

f1 = x
f2 = y
sols = sp.solve((f1, f2), (x, y))
s11 = fun(sols[x], sols[y])
print('El valor de la funcion en el punto obtenido en la undecima combinacion es: '+ str(fun(sols[x], sols[y])))
plt.plot(sols[x], sols[y], "o", c="red")

mg = min(s4, s6, s8, s9, s11)
print('El minimo global de la funcion es: ' + str(mg))