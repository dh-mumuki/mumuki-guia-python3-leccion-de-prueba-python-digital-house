class Test(unittest.TestCase):

  def test_nuevo_anio(self):
    global anio_actual
    anio_actual = 2020
    nuevo_anio()
    self.assertEqual(anio_actual, 2021)