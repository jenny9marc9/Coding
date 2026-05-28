import numpy as np
import matplotlib.pyplot as plt 

c=3
eps=1e-6
kmax=1000
A=np.array([c,1])
x=np.array([1,c])
tabx=[x]
g=A*x
n=np.linalg.norm(g)
tabn=[n]
n0=n
k=0
while (k<kmax) and (n>=eps*n0):
    d= -g
    alpha=-g.dot(d)/d.dot(A*d)
    x=x+alpha*d
    g=A*x
    n=np.linalg.norm(g)
    k=k+1
    tabx.append(x)
    tabn.append(n)
print(k)


tabx0=[vector[0] for vector in tabx]
tabx1=[vector[1] for vector in tabx]
def draw_vector_field(F, xmin, xmax, ymin, ymax, N=20):
    X = np.linspace(xmin, xmax, N)  # coordonnes X et Y
    Y = np.linspace(ymin, ymax, N)  # des points de la grille
    U, V = F(*np.meshgrid(X, Y))  # vector field
    M = np.hypot(U, V)  # Normes des (U[i],V[i])
    M[M == 0] = 1  # évite la division par 0
    U /= M  # Normalisations de U
    V /= M  # ...  et de V
    return plt.quiver(X, Y, U, V, angles='xy')

def level_lines(f, xmin, xmax, ymin, ymax, levels, N=500):
    x = np.linspace(xmin, xmax, N)
    y = np.linspace(ymin, ymax, N)
    z = f(*np.meshgrid(x, y))
    level_l = plt.contour(x, y, z, levels=levels)
    #plt.clabel(level_l, levels, fmt='%.1f') 
    

g = lambda x, y: .5*(x**2 + 8*y**2)
G = lambda x, y: np.array([x, 8*y])
h = lambda x, y: .5*(c*x**2+y**2)
H = lambda x, y: np.array([c*x,y])
%matplotlib inline
plt.figure(figsize=(12,6))
#level_lines(g, -8, 8, -3, 3, np.linspace(0, 28, 8))
#draw_vector_field(G,  -8, 8, -3, 3, 18)
level_lines(h, -8, 8, -3, 3, np.linspace(0,28,8))
draw_vector_field(H, -8, 8, -3, 3)
plt.plot(tabx0,tabx1)
plt.axis('equal')
plt.show()

c=1
iterations=[]
while (c<=32):
    eps=1e-6
    kmax=1000
    A=np.array([c,1])
    x=np.array([1,c])
    g=A*x
    n=np.linalg.norm(g)
    n0=n
    k=0
    while (k<kmax) and (n>=eps*n0):
        d= -g
        alpha=-g.dot(d)/d.dot(A*d)
        x=x+alpha*d
        g=A*x
        n=np.linalg.norm(g)
        k=k+1
    c=c+1
    iterations.append(k)
print(iterations)
plt.plot(iterations)

#armajo
eps=1e-3
x=np.array([1,0.5])
g=np.array([np.sinh(x[0])+2*np.sin(x[0]+x[1])*np.cos(x[0]+x[1]),
            2*np.sin(x[0]+x[1])*np.cos(x[0]+x[1])])
n0=np.linalg.norm(g)
n=n0
j=0
jmax=1000
k=0
kmax=1000
t0=1
tabx=[x]
tabn=[n]
while (j<jmax) and (n>=eps*n0):
    d=-g
    b=3/4
    c=.5
    t=t0
    while (np.cosh(x[0]+t*d[0])+np.sin(x[0]+t*d[0]+x[1]+t*d[1])**2>=
           np.cosh(x[0])+np.sin(x[0]+x[1])**2-t*c*np.linalg.norm(d)**2) and (k<kmax):
        t=t*b
        k=k+1
    x=x+t*d
    g=g=np.array([np.sinh(x[0])+2*np.sin(x[0]+x[1])*np.cos(x[0]+x[1]),
            2*np.sin(x[0]+x[1])*np.cos(x[0]+x[1])])
    n=np.linalg.norm(g)
    tabx.append(x)
    tabn.append(n)
    j=j+1
    t0=2*t
print(j,x)
tabx0=[vector[0] for vector in tabx]
tabx1=[vector[1] for vector in tabx]
plt.plot(tabx0,tabx1)

eps=1e-3
x=np.array([1,.5,1])
g=np.array([np.sinh(x[0])+2*np.sin(x[0]+x[1])*np.cos(x[0]+x[1]),
            2*np.sin(x[0]+x[1])*np.cos(x[0]+x[1])+2*(x[1]-x[2]),-2*(x[1]-x[2])])
n0=np.linalg.norm(g)
n=n0
j=0
jmax=1000
t0=1
tabx=[x]
tabn=[n]
while (j<jmax) and (n>=eps*n0):
    d=-g
    b=3/4
    c=.5
    t=t0
    while (np.cosh(x[0]+t*d[0])+np.sin(x[0]+t*d[0]+x[1]+t*d[1])**2+(x[1]+t*d[1]-x[2]-t*d[2])**2>=
           np.cosh(x[0])+np.sin(x[0]+x[1])**2+(x[1]-x[2])**2-c*t*np.linalg.norm(d)**2) and (j<jmax):
        t=t*b
    x=x+t*d
    g=g=np.array([np.sinh(x[0])+2*np.sin(x[0]+x[1])*np.cos(x[0]+x[1]),
            2*np.sin(x[0]+x[1])*np.cos(x[0]+x[1])+2*(x[1]-x[2]),-2*(x[1]-x[2])])
    n=np.linalg.norm(g)
    tabx.append(x)
    tabn.append(n)
    j=j+1
    t0=t*2
print(j,x)
print(tabx)
from mpl_toolkits.mplot3d import Axes3D
tabx0=[vector[0] for vector in tabx]
tabx1=[vector[1] for vector in tabx]
tabx2=[vector[2] for vector in tabx]
ax = Axes3D(plt.figure()) 
ax.set(xlabel=r'$x$', ylabel=r'$y$', zlabel=r'$z$')
ax.plot(tabx0, tabx1, tabx2,'.') 
plt.show()
