import get_contact as contact

def search_contact_record():
    search_name = input("Enter First name for Searching contact record: ")
    rem_name = search_name[1:]
    first_char = search_name[0]
    search_name = first_char.upper() + rem_name
    contact.file_contents   
    found = False   
    for line in contact.file_contents:
        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            print (line)
            found=True
            break
    if  found == False:
        print("There's no contact Record in Phone Book with name = " + search_name )
