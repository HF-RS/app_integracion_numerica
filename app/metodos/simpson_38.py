def simpson_38_simple(f, a, b):
    """
    Calcula la integral de f desde a hasta b usando la regla de Simpson 3/8 simple.
    """
    h = (b - a) / 3
    x1 = a + h
    x2 = a + 2 * h
    return (3 * h / 8) * (f(a) + 3 * f(x1) + 3 * f(x2) + f(b))

def simpson_38_compuesto(f, a, b, n):
    """
    Calcula la integral de f desde a hasta b usando la regla de Simpson 3/8 compuesta.
    """
    if n <= 0 or n % 3 != 0:
        raise ValueError("El número de subintervalos (n) debe ser un entero positivo y múltiplo de 3 para Simpson 3/8.")
    
    h = (b - a) / n
    
    suma = f(a) + f(b)
    
    # En Simpson 3/8, los coeficientes son 3, 3, 2, 3, 3, 2...
    # Los múltiplos de 3 se multiplican por 2, el resto por 3.
    for i in range(1, n):
        if i % 3 == 0:
            suma += 2 * f(a + i * h)
        else:
            suma += 3 * f(a + i * h)
            
    integral = (3 * h / 8) * suma
    return integral
