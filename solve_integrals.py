
def integrate(f, a, b, n):

    total_area = 0
    rect_area = 0
    dx = (b-a) / n

    for i in range(n):
        x = a + i * dx

        rect_area = f(x) * dx

        total_area += rect_area

    return total_area

def my_function(x):
    return 3 * x**2

result = integrate(my_function, 0, 2, 10)
result1 = integrate(my_function, 0, 2, 100)
result2 = integrate(my_function, 0, 2, 1000)
result3 = integrate(my_function, 0, 2, 10000)


print(f"Calculated area with n 10: {result}")
print(f"Calculated area with n 100: {result1}")
print(f"Calculated area with n 1000: {result2}")
print(f"Calculated area with n 10000: {result3}")
