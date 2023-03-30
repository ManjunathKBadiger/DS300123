import json, csv

def login(username, password):
    with open('admin.json') as fr:
        data = json.load(fr)
        if data['username'] == username and data['password']==password:
            return True
        else:
            return False


def viewAll():
    with open('sample.csv' ) as fr:
        r_obj = csv.reader(fr)
        for items in r_obj:
            print(items)
       

def insert_items():
    with open('sample.csv') as fr:
        r = csv.reader(fr)
        id = 0
        for i in r:
            if len(i) > 0:
                id = i[0] # 107

    with open('sample.csv', 'a') as fw:
        w = csv.writer(fw)
        name = input('Enter a item name : ')
        price = input('Enter a item Price : ')
        w.writerow([str(int(id)+1), name, price])


def remove_item(id):
    with open('sample.csv') as fr:
        r = csv.reader(fr)
        lines = []
        for items in r:
            if id not in items:
                lines.append(items)

        with open('sample.csv', 'w', newline='') as fw:
           w =  csv.writer(fw)
           w.writerows(lines)

def edit_items(id):
    with open('sample.csv') as fr:
        r = csv.reader(fr)
        lines = []
        for items in r:
            if id in items:
                price = input('Enter a Price ') 
                items[2] = price
            lines.append(items)

        with open('sample.csv', 'w', newline='') as fw:
           w =  csv.writer(fw)
           w.writerows(lines)

def signUp():
    name = input("Enter a name : ")
    mobile = input("Enter a mobile# : ")
    email = input("Enter email : ")
    pwd = input("Creat a Password : ")

    with open('User_RegData.csv') as fr:
        data = fr.read()
        fileHasData = False
        if len(data) > 0:
            fileHasData = True
    with open('User_RegData.csv', 'a', newline='') as fw:
        w = csv.writer(fw)
        if not fileHasData:
            columns = ['UserID', 'Name', 'Mobile_Number', 'Email', 'Password']
            w.writerow(columns)
        w.writerow(['101', name, mobile, email, pwd])

signUp()