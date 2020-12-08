#Author: Niyibaruta Diane
import unittest
from school import School


class Test_School(unittest.TestCase):
    def test_name(self):
        c = School('Diane', '0789321453', '20st', 'ALU')
        self.assertEqual(c.name, 'Diane')

    def test_phone(self):
        c = School('Diane', '0789321453', '20st', 'ALU')
        self.assertEqual(c.number, '0789321453')

    def test_addr(self):
        c = School('Diane', '0789321453', '20st', 'ALU')
        self.assertEqual(c.address, '20st')

    def test_wrname(self):
        c = School('Diane', '0789321453', '20st', 'ALU')
        self.assertNotEqual(c.name, 'Alice')

    def test_sch(self):
        c = School('Diane', '0789321453', '20st', 'ALU')
        self.assertEqual(c.school, 'ALU')


if __name__ == '__main__':
    unittest.main()
