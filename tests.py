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

class SoloTest(unittest.TestCase):
    
    def testTrue(self):
        self.assertTrue(devuelveTrue(), "Tiene que fallar")

    def testSuma(self):
        self.assertEqual(sumaPositivos("cadena",3),-1, "Suma correcta")
        self.assertEqual(12,sumaPositivos(4,8), "Suma correcta")

if __name__ == '__main__':
    unittest.main()
