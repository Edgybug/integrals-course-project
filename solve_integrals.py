
def integrate(f, a, b, n):

    total_area = 0
    rect_area = 0
    dx = (b-a) / n

    for i in range(n):
        x = a + i * dx

        rect_area = f(x) * dx

        total_area += rect_area

    return total_area

def function_to_integrate(x):
    return x**2


