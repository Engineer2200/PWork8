import json

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

def writing(phone_book):
    with open('new_file.json', 'w', encoding='utf-8') as fp:
       fp.write(json.dumps(phone_book, ensure_ascii=False))

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)
    elif action == '2':
        start()
    elif action == '3':
        writing(phone_book)

