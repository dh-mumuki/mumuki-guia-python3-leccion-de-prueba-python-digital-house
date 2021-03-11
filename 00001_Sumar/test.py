class Test(unittest.TestCase):

  def test_suma_de_1_y_2_es_3(self):
    self.assertEqual(sumar(1, 2), 3, "sumar(1, 2) debería devolver 3 pero devolvió " + str(sumar(1, 2)))
    
  def test_suma_de_10_y_20_es_30(self):
    self.assertEqual(sumar(10, 20), 30, "sumar(10, 20) debería devolver 30 pero devolvió " + str(sumar(10, 20)))