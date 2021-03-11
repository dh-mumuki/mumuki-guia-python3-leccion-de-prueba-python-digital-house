class Test(unittest.TestCase):

  def test_suma_de_1_y_2_es_3(self):
    self.assertEqual(sumar(1, 2), 3, "sumar(1, 2) debería devolver 3 pero devolvió " + str(sumar(1, 2)))