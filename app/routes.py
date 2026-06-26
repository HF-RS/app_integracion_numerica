from flask import render_template, request, jsonify
from app import app
from app.calculadora.parser import crear_funcion_matematica
from app.metodos.trapecio import trapecio_simple, trapecio_compuesto
from app.metodos.simpson_13 import simpson_13_simple, simpson_13_compuesto
from app.metodos.simpson_38 import simpson_38_simple, simpson_38_compuesto

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    error = None
    funcion_original = ""
    limite_a = ""
    limite_b = ""
    subintervalos_n = 2  
    metodo_seleccionado = "trapecio_simple"

    if request.method == 'POST':
        try:
            funcion_original = request.form.get('funcion', '')
            limite_a_raw = request.form.get('limite_a', '')
            limite_b_raw = request.form.get('limite_b', '')
            metodo_seleccionado = request.form.get('metodo', 'trapecio_simple')
            
            n_raw = request.form.get('subintervalos_n')
            subintervalos_n = int(n_raw) if n_raw else 1

            try:
                limite_a = crear_funcion_matematica(limite_a_raw)(0)
            except Exception:
                raise ValueError(f"El límite inferior '{limite_a_raw}' no es una expresión válida.")

            try:
                limite_b = crear_funcion_matematica(limite_b_raw)(0)
            except Exception:
                raise ValueError(f"El límite superior '{limite_b_raw}' no es una expresión válida.")

            f = crear_funcion_matematica(funcion_original)

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
            # Errores de lógica del método
            error = str(ve)
        except ZeroDivisionError:
            # División entre cero
            error = "Error matemático: Estás intentando realizar una división entre cero."
        except ValueError:
            # Errores de conversión numérica
            error = "Error: Asegúrate de ingresar números o constantes válidas (ej: pi, e)."
        except Exception as e:
            # Captura de errores específicos de math
            if "math domain error" in str(e).lower():
                error = "Error de dominio matemático: Estás intentando calcular una raíz o logaritmo de un número negativo."
            else:
                error = f"Ocurrió un error inesperado: {str(e)}"

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