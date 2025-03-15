# test_algoritmos.py
import unittest
from algoritmo_bmh import search_bmh
from gerar_texto import generate_text

class TestBMH(unittest.TestCase):
    def test_casos_basicos(self):
        self.assertEqual(search_bmh("abracadabra", "abra"), [0, 7])
        self.assertEqual(search_bmh("abcdeabcde", "abc"), [0, 5])
        self.assertEqual(search_bmh("aaaaa", "aa"), [0, 1, 2, 3])
        self.assertEqual(search_bmh("teste", "xyz"), [])
    
    def test_texto_vazio(self):
        self.assertEqual(search_bmh("", "abc"), [])
        self.assertEqual(search_bmh("abc", ""), [])

class TestGeracaoTexto(unittest.TestCase):
    def test_tamanhos(self):
        for size in [500, 1000, 1500, 2000, 3000]:
            text = generate_text(size)
            self.assertEqual(len(text), size)

if __name__ == "__main__":
    unittest.main()