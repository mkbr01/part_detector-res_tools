import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Loads in data
dat = np.loadtxt(...)
T1 = dat[:, 0]  # T1 - KE1: new FL 0.4
x1 = dat[:, 1]

T2 = dat[:, 6]  # T2 - KE2: new FL 0.55
x2 = dat[:, 7]
y2 = dat[:, 8]
z2 = dat[:, 9]
v2 = dat[:, 10]
KE2 = dat[:, 11]

T3 = dat[:, 12]  # T3 - KE3: new FL 0.7
x3 = dat[:, 13]
y3 = dat[:, 14]
z3 = dat[:, 15]
v3 = dat[:, 16]
KE3 = dat[:, 17]

T4 = dat[:, 18]  # T4 - KE4: old FL 0.4
x4 = dat[:, 19]
y4 = dat[:, 20]
z4 = dat[:, 21]
v4 = dat[:, 22]
KE4 = dat[:, 23]

T5 = dat[:, 24]  # T5 - KE5: old FL 0.55
x5 = dat[:, 25]
y5 = dat[:, 26]
z5 = dat[:, 27]
v5 = dat[:, 28]
KE5 = dat[:, 29]

T6 = dat[:, 30]  # T6 - KE5: old FL 0.7
x6 = dat[:, 31]
y6 = dat[:, 32]
z6 = dat[:, 33]
v6 = dat[:, 34]
KE6 = dat[:, 35]

T7 = dat[:, 36]  # T7 - KE7: old FL 0.8
x7 = dat[:, 37]
y7 = dat[:, 38]
z7 = dat[:, 39]
v7 = dat[:, 40]
KE7 = dat[:, 41]

plt.figure(1)
plt.scatter(v4, KE4, marker='x')
plt.xlabel('Vt (mm/?s)')
plt.ylabel('KE (eV)')
plt.show()

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(z4, y4, '.', label='0.4 O')
ax.scatter(z5, y5, '.', label='0.55 O')
ax.scatter(z6, y6, '.', label='0.7 O')
ax.scatter(z7, y7, '.', label='0.8 O')
ax.set_xlabel('z (mm)')
ax.set_ylabel('y (mm)')
ax.legend()
plt.show()

fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')
XI, YI = np.meshgrid(np.arange(-4, 4.25, 0.25), np.arange(-4, 4.25, 0.25))
Z4 = np.griddata((z4, y4), KE4, (XI, YI), method='linear')
ax.plot_surface(XI, YI, Z4, cmap='viridis')
ax.set_xlabel('z (mm)')
ax.set_ylabel('y (mm)')
ax.set_zlabel('KE (eV)')
plt.colorbar(orientation='horizontal')
