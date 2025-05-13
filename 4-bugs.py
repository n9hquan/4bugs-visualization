import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters v and s
v = 1.0
s = 1.0

# Define the time interval for one loop of the animation
frames = 200
t_max = 10     
t = np.linspace(0, t_max, frames)

# Define the equations for each bug
def bug1_x(t, v, s):
    return (s / 2) * (1 - np.exp(-(v/s) * t) * (np.cos((v/s) * t) + np.sin((v/s) * t)))

def bug1_y(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.sin((v/s) * t) - np.cos((v/s) * t)))

def bug2_x(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.sin((v/s) * t) - np.cos((v/s) * t)))

def bug2_y(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.cos((v/s) * t) + np.sin((v/s) * t)))

def bug3_x(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.cos((v/s) * t) + np.sin((v/s) * t)))

def bug3_y(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.cos((v/s) * t) - np.sin((v/s) * t)))

def bug4_x(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.cos((v/s) * t) - np.sin((v/s) * t)))

def bug4_y(t, v, s):
    return (s / 2) * (1 - np.exp(-(v/s) * t) * (np.cos((v/s) * t) + np.sin((v/s) * t)))

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-s, s)
ax.set_ylim(-s, s)
ax.grid(True)
ax.set_xlabel('x(t)')
ax.set_ylabel('y(t)')
ax.set_title('Looping Trajectories of the Four Bugs')


# Initialize empty plot elements for each bug
line1, = ax.plot([], [], color='red')
line2, = ax.plot([], [], color='green')
line3, = ax.plot([], [], color='blue')
line4, = ax.plot([], [], color='purple')
point1, = ax.plot([], [], 'o', markersize=8, label='Bug 1', color='red')
point2, = ax.plot([], [], 'o', markersize=8, label='Bug 2', color='green')
point3, = ax.plot([], [], 'o', markersize=8, label='Bug 3', color='blue')
point4, = ax.plot([], [], 'o', markersize=8, label='Bug 4', color='purple')
ax.legend()

# Function to update the animation frame
def animate(i):

    x1_data = bug1_x(t[:i+1], v, s)
    y1_data = bug1_y(t[:i+1], v, s)
    line1.set_data(x1_data, y1_data)
    point1.set_data(x1_data[-1:], y1_data[-1:])

    x2_data = bug2_x(t[:i+1], v, s)
    y2_data = bug2_y(t[:i+1], v, s)
    line2.set_data(x2_data, y2_data)
    point2.set_data(x2_data[-1:], y2_data[-1:])

    x3_data = bug3_x(t[:i+1], v, s)
    y3_data = bug3_y(t[:i+1], v, s)
    line3.set_data(x3_data, y3_data)
    point3.set_data(x3_data[-1:], y3_data[-1:])

    x4_data = bug4_x(t[:i+1], v, s)
    y4_data = bug4_y(t[:i+1], v, s)
    line4.set_data(x4_data, y4_data)
    point4.set_data(x4_data[-1:], y4_data[-1:])

    return line1, line2, line3, line4, point1, point2, point3, point4

# Create the animation
ani = FuncAnimation(fig, animate, frames=frames, interval=50, blit=True, repeat=True)
plt.xlim(0, s)
plt.ylim(0, s)

# Show the animation
plt.show()
