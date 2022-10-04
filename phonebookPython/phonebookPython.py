import get_contact as contact
import search_contact as search
import enter_contact as enter
import console_cleaning as cleaningC
import delete_contact as deleteC

def menu():
    print("\n   ******** Phone Book Menu ********\n"+
          "------------------------------------------\n"+
          "Enter 1,2,3 or 4:\n"+
          "Enter 1 To Display Your Contacts Records\n"+
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To search your contacts\n"+
          "Enter 4 Console cleaning!\n"+
          "Enter 5 Delete contact!\n"+
          "Enter 6 To Quit\n**********************")
    choice = input("Enter your choice: ")
    if choice == "1":
        if len(contact.file_contents) == 0:
            print("Phone Book is empty")
        else:
            print (contact.file_contents)
        contact.file_contents.close
        ent = input("Press Enter to continue ...")
        menu()
    elif choice == "2":
        enter.enter_contact_information()
        ent = input("Press Enter to continue ...")
        menu()
    elif choice == "3":
        search.search_contact_record()
        ent = input("Press Enter to continue ...")
        menu()
    elif choice == "4":
        cleaningC.clearC()
        menu()
    elif choice == "5":
        deleteC.deleteContact()
        ent = input("Press Enter to continue ...")
        menu()
    elif choice == "6":
        print("\nGoodbye, come again :D")
    else:
        print("Wrong choice, Please Enter [1 to 6]\n")
        ent = input("Press Enter to continue ...")
        menu()
menu()