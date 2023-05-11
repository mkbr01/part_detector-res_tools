import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Loads in data
dat = np.loadtxt('...')
x1 = dat[:, 0]
y1 = dat[:, 1]
z1 = dat[:, 2]
v1 = dat[:, 3]
KE1 = dat[:, 4]

dat2 = np.loadtxt('...')'
y2 = dat2[:, 1]
z2 = dat2[:, 2]
v2 = dat2[:, 3]
KE2 = dat2[:, 4]

dat3 = np.loadtxt('...')
x3 = dat3[:, 0]
y3 = dat3[:, 1]
z3 = dat3[:, 2]
v3 = dat3[:, 3]
KE3 = dat3[:, 4]

# Surface plot of energies/intensities
fig = plt.figure(1)
ti = np.arange(-4, 4.25, 0.25)
XI, YI = np.meshgrid(ti, ti)
ZI = griddata(z1, y1, KE1, XI, YI)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(XI, YI, ZI, cmap='viridis')
ax.scatter(z1, y1, KE1, c='k', marker='.')
ax.set_xlabel('z (mm)')
ax.set_ylabel('y (mm)')
ax.set_zlabel('KE (eV)')
plt.colorbar(ax.get_children()[0], ax=ax, location='right')

# Scatter plot
fig, ax = plt.subplots()
ax.scatter(z1, y1, color='b', marker='.')
ax.scatter(z2, y2, color='r', marker='.')
ax.set_xlabel('z (mm)')
ax.set_ylabel('y (mm)')

# Histogram
fig, ax = plt.subplots()
ax.hist(KE1, bins=6, density=True)
kde = gaussian_kde(KE1)
x = np.linspace(min(KE1), max(KE1), 100)
ax.plot(x, kde(x))
ax.set_xlabel('Detected KE (eV)')
ax.set_ylabel('N. of particles')

# 3D Scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, y1, z1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
