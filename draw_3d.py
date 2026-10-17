import numpy as np

#Draw prism
def draw_prism(ax, f, x, y, dx, dy, color="teal"):
    """Draw a rectangular prism representing a small volume under a surface.

    Args:
        ax: Matplotlib 3D axes on which to draw the prism.
        f: Function of two variables, f(x, y).
        x, y: Coordinates of the prism's lower-left corner.
        dx, dy: Dimensions of the prism along the x- and y-axes.
        color: Color of the prism.
    """
    # Use the function value at the lower-left corner to approximate the height
    height = f(x, y)

    ax.bar3d(
        x, y, 0,        # Base position
        dx, dy, height,  # Width, depth, and height
        color=color,
        alpha=0.85,
        edgecolor="black",
        linewidth=0.5,
        shade=True
    )

#Draw 3d surfaces
def draw_3d_surface(ax, f, x_min, x_max, y_min, y_max, points = None, markers=True):
    """Plot a 3D surface and optionally mark selected points and their heights.

    Args:
        ax: Matplotlib 3D axes on which to draw the surface.
        f: Function of two variables, f(x, y).
        x_min, x_max: Lower and upper limits along the x-axis.
        y_min, y_max: Lower an                         upper limits along the y-axis.
        points: Optional list of (x, y) coordinates to mark.
        markers: Whether to display height markers for the selected points.
    """

    # Generate coordinate values for the surface
    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)

    # Create a 2D coordinate grid from the 1D arrays
    X, Y = np.meshgrid(x, y)

    # Calculate the height of the surface at each grid point
    Z = f(X, Y) 

    # Plot the surface
    ax.plot_surface(
        X, Y, Z,
        cmap='viridis',
        alpha=0.4,
        edgecolor='none'
    )

    # Add height markers only when enabled and points are provided
    if markers and points: 
        for px, py in points:
            pz = f(px, py)  

            # Draw a vertical dotted line from the base plane to the surface
            ax.plot3D([px, px], [py, py], [0, pz], color='black', linestyle=':', linewidth=2)

             # Mark the selected point on the surface
            ax.scatter3D(px, py, pz, color='red', s=50) 

