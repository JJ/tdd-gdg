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
    
class SoloTest(unittest.TestCase):
    
    def testTrue(self):
        self.assertTrue(devuelveTrue(), "Tiene que fallar")

    def testSuma(self):
        self.assertEqual(sumaPositivos("cadena",3),-1, "Suma correcta")
        self.assertEqual(12,sumaPositivos(4,8), "Suma correcta")

    def testMultiplos(self):
        self.assertEqual(multiplo3o5o15(3),1,"Multiplo de 3")
        self.assertEqual(multiplo3o5o15(5),2,u"Multiplo de 5")
        self.assertEqual(multiplo3o5o15(15),3,u"Multiplo de 15")
        self.assertEqual(multiplo3o5o15(7),0,u"No es multiplo")
        

if __name__ == '__main__':
    unittest.main()
