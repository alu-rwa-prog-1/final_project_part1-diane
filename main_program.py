#Author: Niyibaruta Diane
from typing import ValuesView
from work import Work
from school import School
from family_friends import Family_Friends

print()

contacts = {'work': {}, 'school': {}, 'family and friends': {}}

print('PhoneBook')

print()

while True:
    try:
        action = int(input("""Please choose an action below:
        1. Add Contacts
        2. Search Contact
        3. Edit Contacts
        4. Delete Contacts
        5. Exit Program
        type: """))
        print()

    except ValueError:
        print('Enter integers only!. Try Again')
        print()
        continue

    if action == 1:
        while True:
            while True:
                try:
                    con_type = int(input("""Please choose type of contact to add:
                    1. Work Contact
                    2. School Contact
                    3. Family and Friends
                    type: """))
                    print()
                    break
                except ValueError:
                    print('Enter integers only!. Try Again')
                    print()
                    continue
            
            if con_type == 1:
                nm = input('Enter the name: ').lower()
                num = input('Enter the phone number: ')
                addr = input('Enter the address: ')
                comp = input('Enter company name: ')
                pos = input('Enter the position: ')
                contacts['work'][nm] = Work(nm, num, addr, comp, pos)
                print()

            elif con_type == 2:
                nm = input('Enter the name: ').lower()
                num = input('Enter the phone number: ')
                addr = input('Enter the address: ')
                sch = input('Enter school name: ')
                contacts['school'][nm] = School(nm, num, addr, sch)
                print()

            elif con_type == 3:
                nm = input('Enter the name: ').lower()
                num = input('Enter the phone number: ')
                addr = input('Enter the address: ')
                sec = input('Please enter the sector: ')
                contacts['family and friends'][nm] = Family_Friends(nm, num, addr, sec)
                print()

            else:
                print('Sorry. Enter either 1, 2 or 3.')
                print()
                continue
            
            a = 0
            while True:
                try:
                    ad_con = int(input("""Would you like to add another contact? 
                    1. Yes
                    2. No
                    type: """))
                    print()
                    if ad_con == 1:
                        a = 0
                        break
                    elif ad_con == 2:
                        a = 1
                        break
                    else:
                        print('Sorry. Enter either 1 or 2.')
                        print()
                        continue
                except ValueError:
                    print('Enter integers only!. Try Again')
                    print()
                    continue
            
            if a == 1:
                a = 0
                break
            elif a == 0:
                continue
            
    elif action == 2:
        while True:
            try:
                nam = input('Enter name to search number: ').lower()
                for s, t in contacts.items():
                    for x, y in t.items():
                        if nam == x:
                            print('Phone Number: ' + y.number)
                            print()

            except KeyError:
                print('Sorry. That name does not exist in your contact list. Try again')
                print()
                continue
            
            while True:
                try:
                    o_nam = int(input("""Search another name?
                    1. Yes
                    2. Exit
                    type:  """))
                    print()
                    break
                except ValueError:
                    print('Enter integers only!. Try Again')
                    print()
                    continue
            if o_nam == 1:
                continue
            elif o_nam == 2:
                break
            else:
                pass

    elif action == 3:
        c = 0
        while True:
            edit_c = input('Enter the name of contact to edit: ').lower()
            for s, t in contacts.items():
                for x, y in t.items():
                    if x == edit_c:
                        y.edit()
                        print('Edited!')
                        c += 1
            
            if c == 0:
                print('Sorry. That name does not exist in your contact list. Try again')
                print()
                continue
            elif c == 1:
                c = 0
                break
    elif action == 4:

        u = 0
        while True:
            del_c = input('Enter the name of contact to delete: ').lower()
            for s, t in contacts.items():
                if u == 1:
                    break
                for x, y in t.items():
                    if x == del_c:
                        del x
                        print('Deleted!')
                        print()
                        u += 1
            
            if u == 0:
                print('Sorry. That name does not exist in your contact list. Try again')
                print()
                continue
            elif u == 1:
                u = 0
                break
                
    elif action == 5:
        break
    else:
        print('Sorry. Enter either 1, 2, 3, 4 or 5.')
        print()
        continue
    
    while True:
        try:
            rep = int(input("""Would you like to perform another action?
            1. Yes
            2. Exit
            type:  """))
            print()
            break
        except ValueError:
            print('Please enter integers only. Try again')
            print()
            print()
            continue
    
    if rep  == 1:
        continue
    elif rep == 2:
        break

print('End of Program')