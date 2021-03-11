class Test(unittest.TestCase):

  def test_nuevo_anio(self):
    global anio_actual
    anio_actual = 2020
    nuevo_anio()
    self.assertEqual(anio_actual, 2021)
    
  def test_nuevo_anio_2(self):
    global anio_actual
    anio_actual = 2020
    nuevo_anio()
    nuevo_anio()
    nuevo_anio()
    self.assertEqual(anio_actual, 2023)