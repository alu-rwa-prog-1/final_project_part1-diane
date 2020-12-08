#Author: Niyibaruta Diane
from contact import Contact


class School(Contact):
    def __init__(self, name, number, address, school):
        super().__init__(name, number, address)
        self.school = school
