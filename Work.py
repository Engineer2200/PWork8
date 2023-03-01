import json

change = 'Enter command: 1 - read & show | w - Quit\n'
welcome = 'Enter command: 1 - read & show | q - Quit\n'
phone_book = {'Миша гараж':{'phone': ['722333335','72627397543'] , 'birthday': '11-02-2010', 'email':"mail@mail.ru"},
'Sasha':{'phone': ['78436840045','77554802591']}}
def print_book(book):
    for k,v in book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
            print (i, j, end = " | ")
        print()


def start():
    with open('new_file.json', 'w') as f:
        print("The json file is created")

def writing(i):
    with open('new_file.json', 'w', encoding='utf-8') as fp:
       fp.write(json.dumps(i, ensure_ascii=False))

def conclusion(ttt):
    with open('new_file.json', 'r', encoding='utf-8') as fp:
        ttt = json.load(fp)
        return(ttt)

def search(phone_book):
    found = False
    search_name = input('Введите имя контакта:')
    full_search = search_name.capitalize()
    for k in phone_book:
        if full_search == k:
            found = True
            print(k)
    if found == True:
        print((k) and (phone_book[full_search]))
    else:
        print('Нет контакта')
    
def new_record(book):
    k=input("Put new name : ")
    a={}
    a['phone']=list(input('Put phone : ').split())
    a['birthday']=input('Put birthday : ')
    a['email']=input('Put email : ')
    book[k]=a
    writing(phone_book)
    conclusion(phone_book)

def red(x):
    found = False
    search_name = input('Введите имя контакта:')
    full_search = search_name.capitalize()
    for k in phone_book:
        if full_search == k:
            found = True
        if found == True:
                ti = input('введите верное имя:')
                k = ti
        else:
            print('Нет контакта')
    writing(phone_book)
    conclusion(phone_book)    

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book) 
    elif action == '2':
        start() # создание пустого фала, либо его обнуление 
    elif action == '3':
        writing(phone_book) # запись в файл нашего словаря 
    elif action == '4':
        conclusion(phone_book)
        print(phone_book) # файл = списку
    elif action == '5':
        search(phone_book) # поиск контакта
    elif action == '6':
        new_record(phone_book) # добавление нового контакта 
    elif action == '7':
        red(phone_book) #


                