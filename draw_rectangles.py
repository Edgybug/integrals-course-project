import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

def draw_rect(ax, color, start_x, start_y, width, height):
    """Draw a rectangle on the given axes.

    Args:
        ax: Matplotlib axes on which to draw the rectangle.
        color: Color of the rectangle's outline.
        start_x: X-coordinate of the rectangle's lower-left corner.
        start_y: Y-coordinate of the rectangle's lower-left corner.
        width: Width of the rectangle.
        height: Height of the rectangle.
    """
    rect = patches.Rectangle(
        (start_x, start_y), 
        width, 
        height, 
        linewidth=2, 
        edgecolor=color, 
        facecolor='none', 
        alpha=0.8)
    
    ax.add_patch(rect)

def draw_riemann_rectangles(a, b, n, f):
    """Plot a function and approximate its integral using left Riemann rectangles.

    Args:
        a: Lower limit of integration.
        b: Upper limit of integration.
        n: Number of rectangles.
        f: Function to plot and integrate approximately.
    """

    # Generate points for drawing a smooth function curve
    x = np.linspace(a, b, 1000)
    y = f(x)

    # Calculate the width and heights of the left-endpoint rectangles
    dx = (b-a) / n 
    x_bars = np.linspace(a, b - dx, n) 
    y_bars = f(x_bars)
                         
    plt.figure(figsize=(8, 5))

    # Plot the function curve
    plt.plot(x, y, 'r', linewidth=2, label='Function')

   # Draw the rectangles using the function value at each left endpoint
    plt.bar(x_bars, 
            y_bars, 
            width=dx, 
            align='edge', 
            alpha=0.3, 
            edgecolor='blue', 
            color='skyblue', 
            label='Left Riemann Sum')

    # Add chart labels and formatting
    plt.title(f"Left Riemann sum for {n} rectangles")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(a, b)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.show()