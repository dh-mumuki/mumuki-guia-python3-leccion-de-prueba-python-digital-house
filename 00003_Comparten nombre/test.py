class Test(unittest.TestCase):

  def test_ivan_y_marcos_no_comparten_nombre(self):
    self.assertFalse(comparten_nombre("Ivan", "Marcos"))

  def test_agustin_y_agustina_no_comparten_nombre(self):
    self.assertFalse(comparten_nombre("Agustin", "Agustina"))

  def test_mayra_y_mayra_comparten_nombre(self):
    self.assertTrue(comparten_nombre("Mayra", "Mayra"))