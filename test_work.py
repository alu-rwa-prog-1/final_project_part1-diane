#Author: Niyibaruta Diane
import unittest
from work import Work


class Test_Work(unittest.TestCase):
    def test_name(self):
        c = Work('Diane', '0789321453', '20st', 'KFC', 'Manager')
        self.assertEqual(c.name, 'Diane')

    def test_phone(self):
        c = Work('Diane', '0789321453', '20st', 'KFC', 'Manager')
        self.assertEqual(c.number, '0789321453')

    def test_addr(self):
        c = Work('Diane', '0789321453', '20st', 'KFC', 'Manager')
        self.assertEqual(c.address, '20st')

    def test_wrname(self):
        c = Work('Diane', '0789321453', '20st', 'KFC', 'Manager')
        self.assertNotEqual(c.name, 'Alice')

    def test_pos(self):
        c = Work('Diane', '0789321453', '20st', 'KFC', 'Manager')
        self.assertEqual(c.position, 'Manager')


if __name__ == '__main__':
    unittest.main()
