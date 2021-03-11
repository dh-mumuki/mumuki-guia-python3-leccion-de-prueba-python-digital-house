class Test(unittest.TestCase):

  def test_si_invocamos_nuevo_anio_se_debe_incrementar_en_uno_anio_actual(self):
    global anio_actual
    anio_actual = 2020
    nuevo_anio()
    self.assertEqual(anio_actual, 2021)
    
  def test_si_invocamos_nuevo_anio_tres_veces_se_debe_incrementar_en_tres_anio_actual(self):
    global anio_actual
    anio_actual = 2020
    nuevo_anio()
    nuevo_anio()
    nuevo_anio()
    self.assertEqual(anio_actual, 2023)