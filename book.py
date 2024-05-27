

books = []
def add_book() :
    book = {}
    global books
    book["title"] = input("Enter title of the book : ")
    book["author"] = input("Enter author of the book :")
    book["pages"] = int(input("Enter number of pages :"))
    book["price"] = float(input("Enter price of the book : "))
    book["isbn"] = input("Enter ISBN of the book : ")
    books.append(book)
    input("\nThe book successfully added to database . Press enter to continue ...")


def list_books() :
    for book in books :
        print("Title :",book["title"])
        print("Author :",book["author"])
        print("Pages :",book["pages"])
        print("Price :",book["price"])
        print("ISBN :",book["isbn"])
        print("-----------------------------------------------")
    input("\nPress Enter to return to menu ... ")    






def find_book() :
    isbn = input ("Enter ISBN to find your book : ")
    for book in books :
        if book["isbn"] == isbn :
           print("Title :",book["title"])
           print("Author :",book["author"])
           print("Pages :",book["pages"])
           print("Price :",book["price"])
           print("ISBN :",book["isbn"])
           print("-----------------------------------------------")
           break
    else:
        print("\n\nThis book does not exist in books database ! press enter to continue ...")


            


def delete_book() : 
    isbn = input("Enter ISBN to delete your book : ")
    for book in books : 
        if book["isbn"] == isbn :
            books.remove(book)
            input("\n\nThe book has been deleted . ") 
            break
    else:
        input("\n\nThis book does not exist in books database ! press enter to continue ...")          




while True :
    print(40*"=")
    print("Press A to add a book ")
    print("Press L to list all books ")
    print("Press F to find a book ")
    print("Press D to delete a book ")
    print(40*"=")
    choice = input("Enter your choice : ").upper()

    if  choice =='A' :
        add_book()
    elif choice == 'L' :
        list_books()
    elif choice == 'F' :
        find_book()
    elif choice == 'D' :
        delete_book()            
    else :
        print("Wrong choice !")
