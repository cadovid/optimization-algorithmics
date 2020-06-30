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
plt.plot(a, 2, "o", c="red")
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

# Generacion del punto inicial
x = [1, 1]
plt.plot(x[0], x[1], "o", c="orange")
#plt.show()
       
# Metodo de penalizacion interior por barrera logaritmica
c = 1
beta = 10
iters = 0
max_iter = 10
threshold = 1e-6
r = np.array([x[0]**2+x[1]**2-5, 2*x[0]+x[1]-6, x[0]+2*x[1]-4, -x[0], -x[1]]) # Restricciones
B = lambda x : -np.sum([np.log(-_) for _ in r])
chck = lambda x : (1./c)*B(x)

while chck(x) < threshold and iters < max_iter:
            # Calculo de las derivadas parciales primeras
            u, v = sp.symbols('u v')
            f = (u-a)**2 + (v-2)**2 + (1./c)*-np.sum([u**2+v**2-5, 2*u+v-6, u+2*v-4, -u, -v])
            df1 = sp.diff(f, u)
            df2 = sp.diff(f, v)
            g1 = sp.lambdify([u, v], df1)
            g2 = sp.lambdify([u, v], df2)
    
            # Metodo de descenso del gradiente
            lr = 0.01
            _x = np.copy(x)
            x[0] = x[0] - lr * g1(_x[0], _x[1])
            x[1] = x[1] - lr * g2(_x[0], _x[1])
            plt.plot(x[0], x[1], "o", c="yellow")
            c *= beta
            iters += 1
            r = np.array([x[0]**2+x[1]**2-5, 2*x[0]+x[1]-6, x[0]+2*x[1]-4, -x[0], -x[1]])    

sol = fun(x)
print('El valor minimo de la funcion encontrado es: ' + str(sol) + ' en el punto: ' + str(x) + ' obtenido con ' + str(iters-1) + ' iteraciones')
plt.show()

