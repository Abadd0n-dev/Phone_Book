def input_lname():
    lname = input("Enter Last name ")
    try:      
        rem_lname = lname[1:]
        first_char = lname[0]
    except :
        print("Error !!! Invalid data entry !!!")
    return first_char.upper() + rem_lname
    




