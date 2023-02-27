import json

db_path = 'phone_book.json'
welcome = 'Enter command: 1 - read & show | 2 - add record | 3 - search | 4 - init DB | q - Quit\n'
phone_book = {
    'Миша гараж':{'phone': ['72443351195','72627397543'] , 'birthday': '11-02-2010', 'email':"mail@mail.ru"},
    'Sasha':{'phone': ['78436840045','77554802591']}}

def print_book(book):
    for k,v in book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
            print (i, j, end = " | ")
        print()


def init_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh: # открываем файл на запись
        fh.write(json.dumps(db, ensure_ascii=False)) # преобразовываем словарь data в unicode-строку и записываем в файл
        print('БД успещно сохранена')

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)
    elif action == '2':
        print(action, ' -> ', db_path)
    elif action == '3':
        print(action, ' -> ', db_path)
    elif action == '4':
        init_db(db_path,phone_book)