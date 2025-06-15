books = [

    {
        "title": "Seto Dharti",
        "author": "Amar Neupane",
        "year": 2012,
        "available": "yes"
    },
    {
        "title": "Shirishko Phool",
        "author": "Parijat",
        "year": 1965,
        "available": "yes"
    }
]

def View_All_Books():
    counter=1
    print("\n" + "*"*40)
    print("Here Is The List Of All Books")
    print("*"*40)
    
    for i in books:
        print(f"{counter}) Title: {i['title']} {(' ') *20} Author: {i['author']} {(' ') *10}Year: {i['year']}  {(' ') *5} Available: {i['available']}")
        counter+=1
    print("*"*40 + "\n")

def View_Available_Books():
    counter = 0
    print("\n" + "*"*40)
    print("Here Is The List Of Available Books")
    print("*"*40)
    
    for i in books:
        if i["available"].lower() == "yes":
            counter += 1
            print(f"{counter}) Title: {i['title']} {' ' * 20} Author: {i['author']} {' ' * 10} Year: {i['year']} {' ' * 5} Available: {i['available']}")
    
    if counter == 0:
        print("Sorry, no books are currently available.")
    print("*"*40 + "\n")
    return counter

def Add_Book():
    print("\n" + "*"*40)
    book_name= input("Enter The Name of The Book: ")
    book_author_name= input("Enter The Name of The Author of Book: ")
    released_year = int(input("Published Date of Book: "))
    is_available= "yes"
    if book_name and book_author_name and released_year:
        decision = input("Are You Sure Want To Add This Book?(y/n) : ").lower()
        if decision== "y":
            books.append(
                {"title" :book_name,
                "author": book_author_name, 
                "year": released_year,
                "available": is_available
                }
            )
            print("Book Added Successfully!!")
        else:
            print("Invalid Choice, try Again!!")
    print("*"*40 + "\n")

def SearcH_Book():
    print("\n" + "*"*40)
    book_found= False
    search_keyword= input("Enter Keyword To Search: ").lower()
    for j in books:
        if search_keyword in j["title"].lower() or search_keyword in j["author"].lower():
            print("We Found Following From Your Search: ")
            print(f"Title: {j['title']}, Author: {j['author']}, Year: {j['year']}, Available: {j['available']}")
            book_found= True

    if book_found==False:    
        print(f"Sorry The Book Like This Is Not Available")
    print("*"*40 + "\n")

def Borrow_Book():
    print("\n" + "*"*40)
    available_count = View_Available_Books()
    if available_count == 0:
        print("Currently, nothing is available to borrow.")
        print("*"*40 + "\n")
        return
    
    book_choice = int(input(f"Which Book You Wanna Borrow (1-{available_count}): "))

    if 1 <= book_choice <= available_count:
        count = 0
        for book in books:
            if book["available"].lower() == "yes":
                count += 1
                if count == book_choice:
                    book["available"] = "no"  # Mark as borrowed
                    print(f"You have borrowed '{book['title']}' successfully!")
                    break
    else:
        print("Invalid choice, please try again.")
    print("*"*40 + "\n")

def View_Borrowed_Books():
    counter = 0
    print("\n" + "*"*40)
    print("Here Is The List Of Borrowed Books")
    print("*"*40)
    
    for book in books:
        if book["available"].lower() == "no":
            counter += 1
            print(f"{counter}) Title: {book['title']} {' ' * 20} Author: {book['author']} {' ' * 10} Year: {book['year']} {' ' * 5} Available: {book['available']}")
    
    if counter == 0:
        print("No books are currently borrowed.")
    print("*"*40 + "\n")
    return counter

def Return_Book():
    print("\n" + "*"*40)
    borrowed_count = View_Borrowed_Books()
    if borrowed_count == 0:
        print("No books to return right now.")
        print("*"*40 + "\n")
        return
    
    book_choice = int(input(f"Which Book You Wanna Return (1-{borrowed_count}): "))
    
    if 1 <= book_choice <= borrowed_count:
        count = 0
        for book in books:
            if book["available"].lower() == "no":
                count += 1
                if count == book_choice:
                    book["available"] = "yes"  
                    print(f"You have returned '{book['title']}' successfully!")
                    break
    else:
        print("Invalid choice, please try again.")
    print("*"*40 + "\n")

def User_Actions():
    print("\n" + "*"*40)
    print("Choose an action:")
    print("1) View All Books")
    print("2) View All Available Books")
    print("3) View Your Book Borrowing List")
    print("4) Add Book")
    print("5) Search Book")
    print("6) Borrow Book")
    print("7) Return Book")
    print("0) Exit")
    print("*"*40)

while True:
    User_Actions()
    user = int(input("Action You Want To perform: "))
    
    match user:
        case 0:
            print("Bye!!")
            break
        case 1:
            View_All_Books()
        case 2:
            View_Available_Books()
        case 3:
            View_Borrowed_Books()
        case 4:
            Add_Book()
        case 5:
            SearcH_Book()
        case 6:
            Borrow_Book()
        case 7:
            Return_Book()
        case _:
            print("Invalid choice, please select a valid action.")
