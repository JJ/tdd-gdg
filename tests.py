import unittest

def devuelveTrue():
    return True

def sumaPositivos( a, b):
    if ( not (type(a) is int) ):
        return -1
    if ( not (type(b) is int) ):
        return -1
    if ( a >= 0 and b >= 0):
        return a + b

def multiplo3o5o15( numero ):
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

    return a/b

def palindromo(cadena):
    if type(cadena) is int or type(cadena) is float:
        return False

    return cadena == cadena[::-1]

def resta(a,b):
    if (not (type(a) is int)):
        return -1
    if (not (type(b) is int)):
        return -1
    return a-b

def multiplicacion(a,b):
    if (not (type(a) is int)):
        return -1
    if (not (type(b) is int)):
        return -1
    return a*b

class SoloTest(unittest.TestCase):

    def testTrue(self):
        self.assertTrue(devuelveTrue(), "Tiene que fallar")

    def testSuma(self):
        self.assertEqual(sumaPositivos("cadena",3),-1, "Suma correcta")
        self.assertEqual(12,sumaPositivos(4,8), "Suma correcta")

    def testMultiplos(self):
        self.assertEqual(multiplo3o5o15(3),1,"Multiplo de 3")
        self.assertEqual(multiplo3o5o15(5),2,"Multiplo de 5")
        self.assertEqual(multiplo3o5o15(15),3,"Multiplo de 15")
        self.assertEqual(multiplo3o5o15(7),0,"No es multiplo")

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

if __name__ == '__main__':
    unittest.main()
