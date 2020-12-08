#Author: Niyibaruta Diane
import unittest
from contact import Contact


class Test_contact(unittest.TestCase):
    def test_name(self):
        c = Contact('Diane', '0789321453', '20st')
        self.assertEqual(c.name, 'Diane')

    def test_phone(self):
        c = Contact('Diane', '0789321453', '20st')
        self.assertEqual(c.number, '0789321453')

    def test_addr(self):
        c = Contact('Diane', '0789321453', '20st')
        self.assertEqual(c.address, '20st')

    def test_wrname(self):
        c = Contact('Diane', '0789321453', '20st')
        self.assertNotEqual(c.name, 'Alice')

    def test_wrphone(self):
        c = Contact('Diane', '0789321453', '20st')
        self.assertNotEqual(c.number, '079993233')


if __name__ == '__main__':
    unittest.main()
