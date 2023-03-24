import LMS as l

obj = l.LMS("OOPS_Project/library.txt", "PWCLibrary")

while True:
    print("A: Add a Book")
    print("D: Display Book")
    print("I: Issue a Book ")
    print("R: Return a Book ")
    print("E: Exit the Application")
    key = input("Enter a Key : ")
    if key == "A":
        obj.addBook()
    elif key == "D":
        obj.displayBooks()
    elif key == "I":
        obj.issueBook()
    elif key == "R":
        obj.returnBook()
    elif key == "E":
        break



