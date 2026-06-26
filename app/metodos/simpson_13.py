def simpson_13_simple(f, a, b):
    """
    Calcula la integral de f desde a hasta b usando la regla de Simpson 1/3 simple.
    El valor 'n' no se pasa como parámetro porque este método evalúa toda el área en un solo tramo.
    """
    x_m = (a + b) / 2
    
    return (b - a) * ((f(a) + 4 * f(x_m) + f(b)) / 6)

def simpson_13_compuesto(f, a, b, n):
    """
    Calcula la integral de f desde a hasta b usando la regla de Simpson 1/3 compuesta.
    """
    if n <= 0 or n % 2 != 0:
        raise ValueError("El número de subintervalos (n) debe ser un entero positivo y par para Simpson 1/3.")
    
    h = (b - a) / n
    
    suma_impares = 0
    suma_pares = 0
    
    for i in range(1, n, 2):
        x_i = a + i * h
        suma_impares += f(x_i)

    for j in range(2, n, 2):
        x_j = a + j * h
        suma_pares += f(x_j)
        
    integral = (b - a) * (f(a) + 4 * suma_impares + 2 * suma_pares + f(b)) / (3 * n)
    
    return integral