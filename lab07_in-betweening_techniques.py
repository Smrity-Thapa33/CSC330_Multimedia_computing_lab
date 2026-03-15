import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 

# Create a figure and axis to draw on
fig, ax = plt.subplots()

# Set the limits of the x and y axes (drawing area)
ax.set_xlim(0, 10) 
ax.set_ylim(0, 10) 

circle = plt.Circle((1, 5), 0.5, color='blue')
ax.add_patch(circle)

# Define the animation function that updates the circle's position
def animate(i):
    target_x = 8 # The x-coordinate where the circle should end up
    start_x = 1 # The x-coordinate where the circle starts

    # Calculate the new x position using linear interpolation
    x = start_x + (target_x - start_x) * i / 100

    # Update the circle's center position (y stays constant at 5)
    circle.center = (x, 5)

    # Return the modified circle object as a tuple (for blitting)
    return circle,

# Create the animation
# - animate: the function to call for each frame
# - frames=101: total number of frames (from 0 to 100)
# - interval=20: time between frames in milliseconds (20ms = 50 FPS)
# - blit=True: only re-draw the parts that changed (performance boost)
ani = animation.FuncAnimation(fig, animate, frames=101, interval=20, blit=True)
plt.title("Tweening (In-betweening)") 
plt.show()