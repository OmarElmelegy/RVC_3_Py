import numpy as np
import matplotlib.pyplot as plt
from spatialmath.base import trot2, transl2, trplot2 # type: ignore
from matplotlib.patches import Patch  # For custom legend

# Define the origin transformation (Identity)
O = trot2(0)  # Equivalent to no rotation

# Define a translation and rotation transformation
# Translation by (1, 2) and rotation by 30 degrees
T = transl2(1, 2) @ trot2(30, 'deg') 

# Optional: Define a third transformation for demonstration
T2 = transl2(-1, -1) @ trot2(45, 'deg')

# Create a matplotlib figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')  # Ensures that the x and y axes have the same scale
ax.grid(True)          # Adds a grid to the plot for better reference

# Plot the origin transformation
trplot2(O, frame='O', ax=ax, linewidth=2, color='blue')

# Plot the second transformation
trplot2(T, frame='T', ax=ax, linewidth=2, color='red')

# Optional: Plot the third transformation
trplot2(T2, frame='T2', ax=ax, linewidth=2, color='green')

# Optionally, set plot limits for better visibility
ax.set_xlim(-2, 4)
ax.set_ylim(-2, 4)

# Add a legend to distinguish the frames
legend_elements = [
    Patch(facecolor='blue', edgecolor='blue', label='Origin (O)'),
    Patch(facecolor='red', edgecolor='red', label='Transformation (T)'),
    Patch(facecolor='green', edgecolor='green', label='Transformation (T2)')
]
ax.legend(handles=legend_elements, loc='upper left')

# Print the transformation matrix
print("Transformation Matrix T:")
print(T)

# Add a title to the plot
plt.title("2D Transformation Frames")

# Display the plot
plt.show()