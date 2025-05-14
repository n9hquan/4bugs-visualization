import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# Define the parameters v and s
v = 1.0
s = 1.0

# Define the time interval for one loop of the animation
frames = 200
t_max = 10     
t = np.linspace(0, t_max, frames)

# Define the equations for each bull
def bull1_x(t, v, s):
    return (s / 2) * (1 - np.exp(-(v/s) * t) * (np.cos((v/s) * t) + np.sin((v/s) * t)))

def bull1_y(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.sin((v/s) * t) - np.cos((v/s) * t)))

def bull2_x(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.sin((v/s) * t) - np.cos((v/s) * t)))

def bull2_y(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.cos((v/s) * t) + np.sin((v/s) * t)))

def bull3_x(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.cos((v/s) * t) + np.sin((v/s) * t)))

def bull3_y(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.cos((v/s) * t) - np.sin((v/s) * t)))

def bull4_x(t, v, s):
    return (s / 2) * (1 + np.exp(-(v/s) * t) * (np.cos((v/s) * t) - np.sin((v/s) * t)))

def bull4_y(t, v, s):
    return (s / 2) * (1 - np.exp(-(v/s) * t) * (np.cos((v/s) * t) + np.sin((v/s) * t)))

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-s, s)
ax.set_ylim(-s, s)
ax.grid(True)
ax.set_xlabel('x(t)')
ax.set_ylabel('y(t)')
ax.set_title('Trajectories of the Four bulls')

bull_image = mpimg.imread('red-bull.png')  # Make sure this image exists in the same directory or provide full path
bull1_icon = OffsetImage(bull_image, zoom=0.05)  # Adjust zoom to size the image
bull1_abox = AnnotationBbox(bull1_icon, (0, 0), frameon=False)
ax.add_artist(bull1_abox)

bull2_icon = OffsetImage(bull_image, zoom=0.05)  # Adjust zoom to size the image
bull2_abox = AnnotationBbox(bull2_icon, (0, 0), frameon=False)
ax.add_artist(bull2_abox)

bull3_icon = OffsetImage(bull_image, zoom=0.05)  # Adjust zoom to size the image
bull3_abox = AnnotationBbox(bull3_icon, (0, 0), frameon=False)
ax.add_artist(bull3_abox)

bull4_icon = OffsetImage(bull_image, zoom=0.05)  # Adjust zoom to size the image
bull4_abox = AnnotationBbox(bull4_icon, (0, 0), frameon=False)
ax.add_artist(bull4_abox)

# Initialize empty plot elements for each bull
line1, = ax.plot([], [], color='red')
line2, = ax.plot([], [], color='green')
line3, = ax.plot([], [], color='blue')
line4, = ax.plot([], [], color='purple')
# point1, = ax.plot([], [], 'o', markersize=8, label='bull 1', color='red')
# point2, = ax.plot([], [], 'o', markersize=8, label='bull 2', color='green')
# point3, = ax.plot([], [], 'o', markersize=8, label='bull 3', color='blue')
# point4, = ax.plot([], [], 'o', markersize=8, label='bull 4', color='purple')
ax.legend()

# Function to update the animation frame
def animate(i):

    x1_data = bull1_x(t[:i+1], v, s)
    y1_data = bull1_y(t[:i+1], v, s)
    line1.set_data(x1_data, y1_data)
    bull1_abox.xybox = (x1_data[-1], y1_data[-1])

    x2_data = bull2_x(t[:i+1], v, s)
    y2_data = bull2_y(t[:i+1], v, s)
    line2.set_data(x2_data, y2_data)
    bull2_abox.xybox = (x2_data[-1], y2_data[-1])

    x3_data = bull3_x(t[:i+1], v, s)
    y3_data = bull3_y(t[:i+1], v, s)
    line3.set_data(x3_data, y3_data)
    bull3_abox.xybox = (x3_data[-1], y3_data[-1])

    x4_data = bull4_x(t[:i+1], v, s)
    y4_data = bull4_y(t[:i+1], v, s)
    line4.set_data(x4_data, y4_data)
    bull4_abox.xybox = (x4_data[-1], y4_data[-1])

    return line1, line2, line3, line4, bull1_abox, bull2_abox, bull3_abox, bull4_abox

# Create the animation
ani = FuncAnimation(fig, animate, frames=frames, interval=50, blit=True, repeat=True)
plt.xlim(0, s)
plt.ylim(0, s)

# Show the animation
plt.show()
