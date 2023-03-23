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
            self.bookDict.update({str(id) : {'book_title':line.replace("\n", ""), "status":"Available"}})
            id += 1

    def displayBooks(self):
       for i in self.bookDict.items():
            print(i)


l_obj = LMS("OOPS_Project/library.txt", "PWCLibrary")

l_obj.displayBooks()

# l_obj.displayBooks()
