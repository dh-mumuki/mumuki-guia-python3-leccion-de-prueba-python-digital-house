class Test(unittest.TestCase):

  def test_una_persona_con_15_anios_no_es_mayor_de_edad(self):
    self.assertFalse(es_mayor(15))

  def test_una_persona_con_17_anios_no_es_mayor_de_edad(self):
    self.assertFalse(es_mayor(17))

  def test_una_persona_con_18_anios_es_mayor_de_edad(self):
    self.assertTrue(es_mayor(18))

  def test_una_persona_con_19_anios_es_mayor_de_edad(self):
    self.assertTrue(es_mayor(19))

  def test_una_persona_con_30_anios_es_mayor_de_edad(self):
    self.assertTrue(es_mayor(30))