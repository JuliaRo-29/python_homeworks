from math import ceil


def square(side):
    s = side**2
    return s


side = float(input("Длина стороны кавдрата:"))
result = square(side)
rounded_result = ceil(result)

print(f'площадь: {rounded_result}')
