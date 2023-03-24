class LMS:
    """This class is used to keep records of book in Library"""

    def __init__(self, listOfBooks, libraryName):
        self.listOfBooks = listOfBooks
        self.libraryName = libraryName
        self.bookDict = {}
        id = 101

        with open(self.listOfBooks) as file:
            content = file.readlines() 
        
        for line in content:
            self.bookDict.update({str(id) : {'book_title':line.replace("\n", ""),
                                              "status":"Available",
                                              "Name":""}})
            id += 1

    def displayBooks(self):
       print("---------------List Of Books -----------------------")
       print("Book ID \t\t   Title \t\t Status")
       print("_____________________________________________________")
       for key, value in self.bookDict.items():
            print(key, "\t\t", value.get("book_title"), "\t\t",value.get('status'))
    

    # Adding a book to a Library
    def addBook(self):
        newBook = input("Enter Book Titile : ")

        with open(self.listOfBooks, mode='a') as file_update:
            file_update.writelines(f"{newBook}\n")
            id = str(int(max(self.bookDict)) + 1)
        self.bookDict.update({id: {'book_title':newBook, "status": "Available",
                                   "Name":""}})
        print("Successfully added a Book")
        
    def issueBook(self):
        bookId = input("Enter a Book Id : ")
        if bookId in self.bookDict.keys():
            if self.bookDict[bookId]['status'] == "Available":
                name = input("Enter your name: ")
                self.bookDict[bookId]['Name'] = name
                self.bookDict[bookId]['status'] = "Not Available"
                print("Book Issued Successfully...")
            elif self.bookDict[bookId]['status'] == "Not Available":
                print(f"This book is already Issued , Please try other book")
        else:
            print("Book Id is not present")


    def returnBook(self):
        bookId = input("Enter Book ID : ")
        if bookId in self.bookDict.keys():
            if self.bookDict[bookId]['status']== "Available":
                print("This book is already available, Please check the Book Id")
            else:
                 self.bookDict[bookId]['Name'] =""
                 self.bookDict[bookId]['status'] = "Available"
                 print(" Successfully Updated ")
        else:
            print("Book ID not found")
                    

