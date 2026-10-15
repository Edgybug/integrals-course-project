import numpy as np

def integrate(f, a, b, n):

    total_area = 0
    rectangle_area = 0
    dx = (b-a) / n

    for i in range(n):
        x = a + i * dx

        rectangle_area = f(x) * dx

        total_area += rectangle_area

    return total_area

def double_integrate(f, nx, ny, x_min, x_max, y_min, y_max):

    dx = (x_max - x_min) / nx #width of prisms at x
    dy = (y_max - y_min) / ny #width of prisms at y

    total_volume = 0
    for x in np.arange(x_min, x_max, dx): # evenly spaced values for x based on dx
        for y in np.arange(y_min,  y_max, dy): # evenly spaced values for y based on dy
            z = f(x, y)
            prism_volume = z * dx * dy
            total_volume += prism_volume

    return total_volume

