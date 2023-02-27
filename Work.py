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
    

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)
    elif action == '2':
        start()
    elif action == '3':
        writing(phone_book)
    elif action == '4':
        conclusion(phone_book)
        print(phone_book)
    elif action == '5':
        action1 = None
        while action1 != 'w':
            action1 = input(f'{change}').lower()
            if action1 == '1':


