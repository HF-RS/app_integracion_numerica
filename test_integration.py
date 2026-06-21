import unittest
import math
from app.metodos.trapecio import trapecio_simple, trapecio_compuesto
from app.metodos.simpson_13 import simpson_13_simple, simpson_13_compuesto
from app.metodos.simpson_38 import simpson_38_simple, simpson_38_compuesto

class TestIntegrationMethods(unittest.TestCase):

    def test_trapecio(self):
        # Función de prueba: f(x) = x^2
        # Integral de x^2 desde 0 hasta 1 es 1/3
        f = lambda x: x**2
        a, b = 0, 1
        # Aumentamos n para obtener la precisión requerida por el test
        n = 100 
        resultado_analitico = 1/3

        # Prueba de trapecio simple (es una aproximación burda)
        res_simple = trapecio_simple(f, a, b)
        self.assertAlmostEqual(res_simple, 0.5)

        # Prueba de trapecio compuesto
        res_compuesto = trapecio_compuesto(f, a, b, n)
        # Con n=100, la precisión debe ser suficiente para 3 decimales
        self.assertAlmostEqual(res_compuesto, resultado_analitico, places=3)

    def test_simpson_13(self):
        # La regla de Simpson 1/3 es exacta para polinomios de grado <= 3
        # Usamos f(x) = x^3. La integral de 0 a 1 es 1/4 = 0.25
        f = lambda x: x**3
        a, b = 0, 1
        n = 10 # n debe ser par
        resultado_analitico = 0.25

        # Prueba de Simpson 1/3 simple: debe ser exacto
        res_simple = simpson_13_simple(f, a, b)
        self.assertAlmostEqual(res_simple, resultado_analitico, places=7)

        # Prueba de Simpson 1/3 compuesto: debe ser exacto
        res_compuesto = simpson_13_compuesto(f, a, b, n)
        self.assertAlmostEqual(res_compuesto, resultado_analitico, places=7)

    def test_simpson_38(self):
        # Función de prueba: f(x) = e^x
        # Integral de e^x desde 0 hasta 1 es e - 1
        f = math.exp
        a, b = 0, 1
        n = 9 # n debe ser múltiplo de 3
        resultado_analitico = math.e - 1

        # Prueba de Simpson 3/8 simple
        res_simple = simpson_38_simple(f, a, b)
        self.assertAlmostEqual(res_simple, resultado_analitico, places=3)

        # Prueba de Simpson 3/8 compuesto
        res_compuesto = simpson_38_compuesto(f, a, b, n)
        self.assertAlmostEqual(res_compuesto, resultado_analitico, places=5)

    def test_validaciones_n(self):
        f = lambda x: x
        a, b = 0, 1
        
        # n debe ser par para Simpson 1/3 compuesto
        with self.assertRaises(ValueError):
            simpson_13_compuesto(f, a, b, n=3)
            
        # n debe ser múltiplo de 3 para Simpson 3/8 compuesto
        with self.assertRaises(ValueError):
            simpson_38_compuesto(f, a, b, n=4)
            
        # n debe ser positivo
        with self.assertRaises(ValueError):
            trapecio_compuesto(f, a, b, n=0)

if __name__ == '__main__':
    unittest.main()
