#Author: Niyibaruta Diane
from contact import Contact


class Work(Contact):
    def __init__(self, name, number, address, company, position):
        super().__init__(name, number, address)
        self.company = company
        self.position = position
