import math
import unittest


def isPrime(n):
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(2, n - 1, n) == 1


def devuelveTrue():
    return True


def sumaPositivos(a, b):
    if (not (type(a) is int)):
        return -1
    if (not (type(b) is int)):
        return -1
    if (a >= 0 and b >= 0):
        return a + b


def multiplo3o5o15(numero):
    if numero % 15 == 0:
        return 3
    if numero % 3 == 0:
        return 1
    if numero % 5 == 0:
        return 2
    return 0


def division(a, b):
    if b == 0:
        return -1

    return a / b


def palindromo(cadena):
    if type(cadena) is int or type(cadena) is float:
        return False

    return cadena == cadena[::-1]


def resta(a, b):
    if (not (type(a) is int)):
        return -1
    if (not (type(b) is int)):
        return -1
    return a - b


def multiplicacion(a, b):
    if (not (type(a) is int)):
        return -1
    if (not (type(b) is int)):
        return -1
    return a * b


def cuadrado(a):
    if(not(type(a)is int)):
        return -1
    else:
        return a**2


def squareRoot(a):
    if(not(type(a)is int)):
        return -1
    else:
        return math.sqrt(a)


def Bisiesto(numero):
    if (numero % 4 == 0 and numero % 100 != 0) or numero % 400 == 0:
        return True
    else:
        return False


def odd(number):
    if(number % 2 == 0):
        return True
    else:
        return False


def even(number):
    if(number % 2 != 0):
        return True
    else:
        return False

def Fibonacci(pos):
    if (not (type(pos) is int)):
        return -1
    if pos == 1 or pos == 0:
        return 1
    else:
        fib = 2
        fib_anterior = 1
        for i in range(2,pos):
            fib += fib_anterior
            fib_anterior = fib-fib_anterior
        return fib



def elevadoEnteros(base,exponente):
	if(not (type(base) is int)):
		return -1
	else:
		return math.pow(base, exponente)

class SoloTest(unittest.TestCase):

    def testTrue(self):
        self.assertTrue(devuelveTrue(), "Devuelve lo que tiene que devolver")

    def testSuma(self):
        self.assertEqual(sumaPositivos("cadena", 3), -1, "Suma correcta")
        self.assertEqual(sumaPositivos(4, 8), 12, "Suma correcta")

    def testMultiplos(self):
        self.assertEqual(multiplo3o5o15(3), 1, "Multiplo de 3")
        self.assertEqual(multiplo3o5o15(5), 2, "Multiplo de 5")
        self.assertEqual(multiplo3o5o15(15), 3, "Multiplo de 15")
        self.assertEqual(multiplo3o5o15(7), 0, "No es multiplo")

    def testDivision(self):
        self.assertEqual(division(1, 0), -1, "Division correcta")
        self.assertEqual(division(4, 2), 2, "Division correcta")

    def testPalindromo(self):
        self.assertEqual(palindromo("hola"), False)
        self.assertEqual(palindromo("aba"), True)
        self.assertEqual(palindromo(1), False)

    def testResta(self):
        self.assertEqual(resta(50, 20), 30, "Resta correcta")
        self.assertEqual(resta(50, 80), -30, "Resta correcta")
        self.assertEqual(resta("a", 10), -1, "Resta incorrecta")
        self.assertEqual(resta(10, "b"), -1, "Resta incorrecta")

    def testMultiplicacion(self):
        self.assertEqual(multiplicacion(5, 2), 10, "Resta correcta")
        self.assertEqual(multiplicacion(-5, 8), -40, "Resta correcta")
        self.assertEqual(multiplicacion("a", 10), -1, "Resta incorrecta")
        self.assertEqual(multiplicacion(10, "b"), -1, "Resta incorrecta")

    def testPrime(self):
        self.assertTrue(isPrime(11))
        self.assertTrue(not isPrime(10))

    def testCuadrado(self):
        self.assertEqual(cuadrado(2), 4, "El cuadrado de 2 es 4")
        self.assertEqual(cuadrado(3), 9, "El cuadrado de 3 es 9")

    def testRoot(self):
        self.assertEqual(squareRoot(4), 2, "La raiz cuadrada de 4 es 2")
        self.assertEqual(squareRoot(25), 5, "La raiz cuadrada de 25 es 5")
        self.assertEqual(squareRoot(7.9), -1,
                         "No ha introducido un numero entero")

    def testBisiesto(self):
        self.assertEqual(Bisiesto(2016), True)

    def test_odd(self):
        self.assertTrue(odd(2), "El numero 2 es par")
        self.assertTrue(not odd(3), "El numero 3 no es par")

    def test_even(self):
        self.assertTrue(even(3), "El numero 3 es impar")
        self.assertTrue(not even(2), "El numero 2 no es impar")

    def test_fibonacci(self):
        self.assertEqual(Fibonacci("hola"), -1, "Argumento incorrecto")
        self.assertEqual(Fibonacci(0), 1, "La sucesion de Fibonacci en la pos 0 es 1")
        self.assertEqual(Fibonacci(4), 5, "La sucesion de Fibonacci en la pos 4 es 5")

    def testElevadoEnteros(self):
	    self.assertEqual(elevadoEnteros(2,4), 16, "2 elevado 4 es 16")
	    self.assertEqual(elevadoEnteros(-1,3), -1, "No es un entero")

if __name__ == '__main__':
    unittest.main()
