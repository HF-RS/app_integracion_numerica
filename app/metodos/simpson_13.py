def simpson_13_simple(f, a, b):
    """
    Calcula la integral de f desde a hasta b usando la regla de Simpson 1/3 simple.
    """
    m = (a + b) / 2
    return (b - a) * (f(a) + 4 * f(m) + f(b)) / 6

def simpson_13_compuesto(f, a, b, n):
    """
    Calcula la integral de f desde a hasta b usando la regla de Simpson 1/3 compuesta.
    """
    if n <= 0 or n % 2 != 0:
        raise ValueError("El número de subintervalos (n) debe ser un entero positivo y par para Simpson 1/3.")
    
    h = (b - a) / n
    
    # Suma de los términos con coeficiente 4 (índices impares)
    suma_impares = sum(f(a + i * h) for i in range(1, n, 2))
    
    # Suma de los términos con coeficiente 2 (índices pares)
    suma_pares = sum(f(a + i * h) for i in range(2, n, 2))
    
    integral = (h / 3) * (f(a) + 4 * suma_impares + 2 * suma_pares + f(b))
    return integral
