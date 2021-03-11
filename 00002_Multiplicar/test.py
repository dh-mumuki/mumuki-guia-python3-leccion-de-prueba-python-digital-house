class Test(unittest.TestCase):

  def test_multiplicar_4_por_5_devuelve_20(self):
    self.assertEqual(multiplicar(4, 5), 20, f"multiplicar(4,5) debería devolver 20, pero devolvió {multiplicar(4, 5)}")
    
  def test_multiplicar_4_por_menos_5_devuelve_menos_20(self):
    self.assertEqual(multiplicar(4, -5), -20, f"multiplicar(4, -5) debería devolver -20, pero devolvió {multiplicar(4, -5)}")