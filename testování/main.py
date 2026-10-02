import unittest

def obsahuje_jen_pismena(text):
    return text.isalpha()

class TestobsahujeJenPismena(unittest.TestCase):
    def test_jen_pismena(self):
            self.assertTrue(obsahuje_jen_pismena("Ahoj"))

    






















#Vytvořte funkci `obsahuje_jen_pismena(text)`, která přijme textový řetězec a vrátí `True`, pokud řetězec obsahuje **pouze písmena** (bez mezer, číslic, speciálních znaků), jinak vrátí `False`.

#Napište k ní **alespoň 3 testy** ověřující různé vstupy.

#<details>
#<summary>🔎 Očekávaný výstup (klikni pro zobrazení)</summary>

#```
#test_jen_pismena (__main__.TestObsahujeJenPismena) ... ok
#test_prazdny_retezec (__main__.TestObsahujeJenPismena) ... ok
#test_s_cislicemi (__main__.TestObsahujeJenPismena) ... ok
#test_s_mezerami (__main__.TestObsahujeJenPismena) ... ok
