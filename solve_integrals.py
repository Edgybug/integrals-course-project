
def integrate(f, a, b, n):

    total_area = 0
    rectangle_area = 0
    dx = (b-a) / n

    for i in range(n):
        x = a + i * dx

        rectangle_area = f(x) * dx

        total_area += rectangle_area

    return total_area


