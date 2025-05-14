import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters
s = 1.0  # size of the square
v1 = 0.3  # speed of bug 1
v2 = 0.4  # speed of bug 2
v3 = 0.5  # speed of bug 3

# Bug 4 position
x0 = 0.8  
y0 = 0.2  

# Define the time interval for the animation
frames = 600
t_max = 30     
t = np.linspace(0, t_max, frames)

# Calculate constants used in equations
A3 = s - x0
B3 = s - y0
D0 = np.sqrt(A3**2 + B3**2)
K3 = v3 / D0
K2 = v2 / s
k1 = v1 / s

Cx2 = -x0 - (K2 * A3) / (K2 - K3)
Ux2 = (K2 * A3) / (K2 - K3)
Cy2 = -y0 + s - (K2 * B3) / (K2 - K3)
Uy2 = (K2 * B3) / (K2 - K3)

# Define the equations for each bug based on the images
def bug1_x(t):
    term1 = x0 + (k1 * Cx2 / (k1 - K2)) * np.exp(-K2 * t)
    term2 = (k1 * Ux2 / (k1 - K3)) * np.exp(-K3 * t) 
    term3 = -(x0 + (k1 * Cx2 / (k1 - K2)) + (k1 * Ux2 / (k1 - K3))) * np.exp(-k1 * t)
    return term1 + term2 + term3

def bug1_y(t):
    term1 = y0 + (k1 * Cy2 / (k1 - K2)) * np.exp(-K2 * t)
    term2 = (k1 * Uy2 / (k1 - K3)) * np.exp(-K3 * t)
    term3 = -(y0 + (k1 * Cy2 / (k1 - K2)) + (k1 * Uy2 / (k1 - K3))) * np.exp(-k1 * t)
    return term1 + term2 + term3

def bug2_x(t):
    term1 = x0 + (-x0 - (K2 * A3 / (K2 - K3))) * np.exp(-K2 * t)
    term2 = (K2 * A3 / (K2 - K3)) * np.exp(-K3 * t)
    return term1 + term2

def bug2_y(t):
    term1 = y0 + (-y0 + s - (K2 * B3 / (K2 - K3))) * np.exp(-K2 * t)
    term2 = (K2 * B3 / (K2 - K3)) * np.exp(-K3 * t)
    return term1 + term2

def bug3_x(t):
    return x0 + (s - x0) * np.exp(-v3 * t / np.sqrt((s - x0)**2 + (s - y0)**2))

def bug3_y(t):
    return y0 + (s - y0) * np.exp(-v3 * t / np.sqrt((s - x0)**2 + (s - y0)**2))

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0, max(s, max(x0, y0)))
ax.set_ylim(0, max(s, max(x0, y0)))
ax.grid(True)
ax.set_xlabel('x(t)')
ax.set_ylabel('y(t)')
ax.set_title('Trajectories of Three Bugs Approaching Stationary Bug 4')

# Initialize empty plot elements for each bug
line1, = ax.plot([], [], 'r-')
line2, = ax.plot([], [], 'g-')
line3, = ax.plot([], [], 'b-')

point1, = ax.plot([], [], 'ro', markersize=8, label='Bug 1')
point2, = ax.plot([], [], 'go', markersize=8, label='Bug 2')
point3, = ax.plot([], [], 'bo', markersize=8, label='Bug 3')
point4, = ax.plot(x0, y0, 'ko', markersize=8, label='Bug 4')
plt.plot(x0, y0)
ax.legend()

# Function to update the animation frame
def animate(i):
    x1_data = bug1_x(t[:i+1])
    y1_data = bug1_y(t[:i+1])
    line1.set_data(x1_data, y1_data)
    point1.set_data(x1_data[-1:], y1_data[-1:])

    x2_data = bug2_x(t[:i+1])
    y2_data = bug2_y(t[:i+1])
    line2.set_data(x2_data, y2_data)
    point2.set_data(x2_data[-1:], y2_data[-1:])

    x3_data = bug3_x(t[:i+1])
    y3_data = bug3_y(t[:i+1])
    line3.set_data(x3_data, y3_data)
    point3.set_data(x3_data[-1:], y3_data[-1:])

    return line1, line2, line3, point1, point2, point3, point4

# Create the animation
ani = FuncAnimation(fig, animate, frames=frames, interval=50, blit=True, repeat=True)

# Show the animation
plt.show()