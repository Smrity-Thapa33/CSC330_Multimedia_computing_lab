import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-200, 200) # X-axis range
ax.set_ylim(-50, 50) # Y-axis range

# Create a red circle with radius 10 at the origin
circle = plt.Circle((0, 0), radius=10, color='r')
ax.add_patch(circle) # Add circle to the plot

# Animation function - called once for each frame
def animate(i):

    # Compute new coordinates using sine and cosine
    x = 100 * np.sin(i * 0.1) 
    y = 20 * np.cos(i * 0.1) 
    circle.center = (x, y) # Update circle position
    return circle, 

# Create the animation using FuncAnimation
ani = animation.FuncAnimation(
    fig, animate, frames=200, interval=50, blit=True
)
plt.title("Circular Motion using Sine and Cosine")
plt.show() # Display the animation