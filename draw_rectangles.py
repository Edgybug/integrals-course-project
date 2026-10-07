import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

def draw_rect(ax, color, start_x, start_y, width, height):
   
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

    # Curve points
    x = np.linspace(a, b, 1000)
    y = f(x)

    # Rectangle values
    dx = (b-a) / n # width of every rect
    x_bars = np.linspace(a, b - dx, n) 
    y_bars = f(x_bars)

    plt.figure(figsize=(8, 5))

    # Draw the curve
    plt.plot(x, y, 'r', linewidth=2, label='$f(x) = x^2$')

    # Draw the rectangles
    plt.bar(x_bars, y_bars, width=dx, align='edge', 
            alpha=0.3, edgecolor='blue', color='skyblue', label='Left Riemann Sum')

    # Making the graphic look better
    plt.title(f"Left Riemann sum for {n} rectangles")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(a - 0.5, b + 0.5)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.show()