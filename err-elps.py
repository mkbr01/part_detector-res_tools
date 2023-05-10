import numpy as np
import matplotlib.pyplot as plt

s = [2, 2]
x = np.random.randn(334, 1)
dat1 = np.loadtxt(..)
y1 = dat1[:, 2]
y2 = dat1[:, 1]
data = np.column_stack((y1, y2))

# Calculate the eigenvectors and eigenvalues
covariance = np.cov(data, rowvar=False)
eigenval, eigenvec = np.linalg.eig(covariance)

# Get the index of the largest eigenvector
largest_eigenvec_ind_c = np.unravel_index(np.argmax(eigenval), eigenval.shape)[1]
largest_eigenvec = eigenvec[:, largest_eigenvec_ind_c]

# Get the largest eigenvalue
largest_eigenval = np.max(eigenval)

# Get the smallest eigenvector and eigenvalue
if largest_eigenvec_ind_c == 0:
    smallest_eigenval = np.max(eigenval[:, 1])
    smallest_eigenvec = eigenvec[:, 1]
else:
    smallest_eigenval = np.max(eigenval[:, 0])
    smallest_eigenvec = eigenvec[:, 0]

# Calculate the angle between the x-axis and the largest eigenvector
angle = np.arctan2(largest_eigenvec[1], largest_eigenvec[0])

# Shift the angle between 0 and 2pi
if angle < 0:
    angle += 2 * np.pi

# Get the coordinates of the data mean
avg = np.mean(data, axis=0)

# Get the 95% confidence interval error ellipse
chisquare_val = 2.4477
theta_grid = np.linspace(0, 2 * np.pi)
phi = angle
X0 = avg[0]
Y0 = avg[1]
a = chisquare_val * np.sqrt(largest_eigenval)
b = chisquare_val * np.sqrt(smallest_eigenval)

# The ellipse in x and y coordinates
ellipse_x_r = a * np.cos(theta_grid)
ellipse_y_r = b * np.sin(theta_grid)

# Define a rotation matrix
R = np.array([[np.cos(phi), np.sin(phi)], [-np.sin(phi), np.cos(phi)]])

# Rotate the ellipse to the angle phi
r_ellipse = np.dot(np.column_stack((ellipse_x_r, ellipse_y_r)), R)

# Plotting
plt.figure(2)
plt.subplot(2, 2, 3)
# Draw the error ellipse
plt.plot(r_ellipse[:, 0] + X0, r_ellipse[:, 1] + Y0, '-')
plt.hold(True)

# Plot the original data
plt.plot(data[:, 0], data[:, 1], '.')
plt.hold(True)

# Plot the eigenvectors
plt.quiver(X0, Y0, largest_eigenvec[0] * np.sqrt(largest_eigenval),
           largest_eigenvec[1] * np.sqrt(largest_eigenval), color='m', linewidth=2)
plt.quiver(X0, Y0, smallest_eigenvec[0] * np.sqrt(smallest_eigenval),
           smallest_eigenvec[1] * np.sqrt(smallest_eigenval), color='g', linewidth=2)
plt.hold(True)

# Set the axis labels
plt.xlabel('z (mm)')
plt.ylabel('y (mm)')
plt.title('0
