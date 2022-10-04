import re

def deleteContact():
    with open('phonebook.txt') as phonebook:
        lines = phonebook.readlines()
        print("Attention! If you enter numbers, you may delete other contacts!")
        str = input("enter first and last name to delete contact: ")
        pattern = re.compile(re.escape(str))
        with open('phonebook.txt', 'w') as phonebook: 
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    phonebook.write(line)



