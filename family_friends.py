#Author: Niyibaruta Diane

from contact import Contact


class Family_Friends(Contact):
    def __init__(self, name, number, address, sector):
        super().__init__(name, number, address)
        self.sector = sector
