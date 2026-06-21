import math

def crear_funcion_matematica(expresion):
    """
    Crea una función de Python a partir de una expresión matemática en formato de cadena.
    """
    # Reemplazamos el símbolo '^' por '**' para que Python lo entienda como potencia
    expresion_segura = expresion.replace('^', '**')

    # Diccionario de funciones y constantes permitidas
    safe_dict = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan,
        'sqrt': math.sqrt,
        'exp': math.exp,
        'log': math.log,
        'log10': math.log10,
        'pi': math.pi,
        'e': math.e,
        'abs': abs
    }

    def f(x):
        try:
            # Añadimos 'x' al diccionario seguro para que esté disponible
            safe_dict['x'] = float(x)
            # Evaluamos la expresión
            return eval(expresion_segura, {"__builtins__": None}, safe_dict)
        except Exception as e:
            raise ValueError(f"Error al evaluar la función en x={x}: {str(e)}. Verifica la sintaxis.")

    return f
