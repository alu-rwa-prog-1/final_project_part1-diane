#Author: Niyibaruta Diane
import unittest
from family_friends import Family_Friends


class Test_Family_Friends(unittest.TestCase):
    def test_name(self):
        c = Family_Friends('Diane', '0789321453', '20st', 'Remera')
        self.assertEqual(c.name, 'Diane')

    def test_phone(self):
        c = Family_Friends('Diane', '0789321453', '20st', 'Remera')
        self.assertEqual(c.number, '0789321453')

    def test_addr(self):
        c = Family_Friends('Diane', '0789321453', '20st', 'Remera')
        self.assertEqual(c.address, '20st')

    def test_wrname(self):
        c = Family_Friends('Diane', '0789321453', '20st', 'Remera')
        self.assertNotEqual(c.name, 'Alice')

    def test_sec(self):
        c = Family_Friends('Diane', '0789321453', '20st', 'Remera')
        self.assertEqual(c.sector, 'Remera')


if __name__ == '__main__':
    unittest.main()
