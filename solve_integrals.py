import numpy as np

def integrate(f, a, b, n):
    """Approximate the definite integral using a left Riemann sum.

    Args:
        f: Function to integrate.
        a: Lower limit of integration.
        b: Upper limit of integration.
        n: Number of rectangles.

    Returns:
        Approximate area under the curve.
    """
    dx = (b-a) / n # Width of each rectangle
    total_area = 0


    # Add the area of each rectangle to the total
    for i in range(n):
        x = a + i * dx # Left endpoint of the current interval
        rectangle_area = f(x) * dx
        total_area += rectangle_area

    return total_area

def double_integrate(f, nx, ny, x_min, x_max, y_min, y_max):
    """Approximate the volume under a surface using rectangular prisms.

    Args:
        f: Function of two variables, f(x, y).
        nx: Number of subdivisions along the x-axis.
        ny: Number of subdivisions along the y-axis.
        x_min, x_max: Integration limits along the x-axis.
        y_min, y_max: Integration limits along the y-axis.

    Returns:
        Approximate volume under the surface.
    """
    dx = (x_max - x_min) / nx # Width of each prism along x
    dy = (y_max - y_min) / ny # Width of each prism along y
    total_volume = 0

    # Approximate the volume by summing the individual prism volumes
    for i in range(nx):
        x = x_min + i * dx

        for j in range(ny):
            y = y_min + j * dy
            z = f(x, y) # Height of the prism at the lower-left corner
            prism_volume = z * dx * dy
            total_volume += prism_volume

    return total_volume

