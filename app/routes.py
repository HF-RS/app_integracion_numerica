from flask import render_template, request, jsonify
from app import app
from app.calculadora.parser import crear_funcion_matematica
from app.metodos.trapecio import trapecio_simple, trapecio_compuesto
from app.metodos.simpson_13 import simpson_13_simple, simpson_13_compuesto
from app.metodos.simpson_38 import simpson_38_simple, simpson_38_compuesto

@app.route('/', methods=['GET', 'POST'])
def index():
    # Variables iniciales por defecto para el formulario
    resultado = None
    error = None
    funcion_original = ""
    limite_a = ""
    limite_b = ""
    subintervalos_n = 2  # Valor inicial recomendado
    metodo_seleccionado = "trapecio_simple"

    if request.method == 'POST':
        try:
            # 1. Recuperar los datos del formulario web
            funcion_original = request.form.get('funcion', '')
            limite_a = float(request.form.get('limite_a'))
            limite_b = float(request.form.get('limite_b'))
            metodo_seleccionado = request.form.get('metodo', 'trapecio_simple')
            
            # Obtener subintervalos solo si el método es compuesto
            n_raw = request.form.get('subintervalos_n')
            subintervalos_n = int(n_raw) if n_raw else 1

            # 2. Convertir el texto de la calculadora a una función matemática de Python
            f = crear_funcion_matematica(funcion_original)

            # 3. Evaluar la integral según el método seleccionado por el usuario
            if metodo_seleccionado == 'trapecio_simple':
                resultado = trapecio_simple(f, limite_a, limite_b)
                
            elif metodo_seleccionado == 'trapecio_compuesto':
                resultado = trapecio_compuesto(f, limite_a, limite_b, subintervalos_n)
                
            elif metodo_seleccionado == 'simpson_13_simple':
                resultado = simpson_13_simple(f, limite_a, limite_b)
                
            elif metodo_seleccionado == 'simpson_13_compuesto':
                resultado = simpson_13_compuesto(f, limite_a, limite_b, subintervalos_n)
                
            elif metodo_seleccionado == 'simpson_38_simple':
                resultado = simpson_38_simple(f, limite_a, limite_b)
                
            elif metodo_seleccionado == 'simpson_38_compuesto':
                resultado = simpson_38_compuesto(f, limite_a, limite_b, subintervalos_n)
                
            else:
                error = "El método seleccionado no es válido."

        except ValueError as ve:
            # Captura errores de validación matemática (como 'n' impar en Simpson 1/3)
            error = str(ve)
        except Exception as e:
            # Captura cualquier otro error inesperado (ej: división por cero al evaluar)
            error = f"Ocurrió un error inesperado al calcular: {str(e)}"

    # Retorna la página HTML inyectándole las respuestas del backend
    return render_template(
        'index.html',
        resultado=resultado,
        error=error,
        funcion=funcion_original,
        a=limite_a,
        b=limite_b,
        n=subintervalos_n,
        metodo_act=metodo_seleccionado
    )