#Author: Niyibaruta Diane


class Contact():
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

    def edit(self):
        while True:
            try:
                field = int(input("""What would you like to edit: 
                1. Name
                2. Number
                3. Address
                Type: """))
                print()
                break
            except ValueError:
                print('Please enter integers only!')
                print()
                continue
        
        if field == 1:
            self.name = input('Enter new name: ')
            print()
        elif field == 2:
            self.number = input('Enter new phone number: ')
            print()
        elif field == 3:
            self.address = input('Enter new address: ')
            print()
        else:
            print('Sorry. Enter either 1, 2 or 3.')
            print()
    
