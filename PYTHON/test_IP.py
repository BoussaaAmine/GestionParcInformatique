import unittest
from Parc import Parc
class TestIP(unittest.TestCase):
    p=Parc()
    
    #Test de Vérifiaction de la méthode checkip a automatisé
    def test_IPV4(self):
        self.assertTrue(self.p.checkip("127.0.0.1"))
    def test_IP_Char(self):
        self.assertFalse(self.p.checkip("127.0.a.1"))
    def test_IP_UP255(self):
        self.assertFalse(self.p.checkip("127.0.300.1"))
    def test_IP_Empty(self):
        self.assertFalse(self.p.checkip("127.1.1"))
    def test_IP_0000(self):
        self.assertFalse(self.p.checkip("0.0.0.0"))

if __name__ == '__main__':
    unittest.main()