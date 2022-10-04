from input_name import input_fname
from input_surname import input_lname

def enter_contact_information():   
    first = input_fname()
    last = input_lname()
    phone = input('Enter Phone number ')
    email = input('Enter E-mail ')    
    contact = ("[" + first + " " + last + ", " + phone + ", " + email +  "]\n")
    file_name = "phonebook.txt"
    file1 = open(file_name, "a")
    file1.write(contact)
    print( "This contact\n " + contact + "has been added successfully!")




