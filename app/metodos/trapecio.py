def trapecio_simple(f, a, b):
    """
    Calcula la integral de f desde a hasta b usando la regla del trapecio simple.
    """
    return (b - a) * (f(a) + f(b)) / 2

def trapecio_compuesto(f, a, b, n):
    """
    Calcula la integral de f desde a hasta b usando la regla del trapecio compuesto.
    """
    if n <= 0:
        raise ValueError("El número de subintervalos (n) debe ser un entero positivo.")
    
    h = (b - a) / n
    # La fórmula es (h/2) * [f(a) + 2*sum(f(x_i)) + f(b)]
    suma_intermedios = sum(f(a + i * h) for i in range(1, n))
    
    integral = (h / 2) * (f(a) + 2 * suma_intermedios + f(b))
    return integral
