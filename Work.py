
welcome = 'Enter command: 1 - read & show | q - Quit\n'
phone_book = {
'Миша гараж':{'phone': ['722333335','72627397543'] , 'birthday': '11-02-2010', 'email':"mail@mail.ru"},
'Sasha':{'phone': ['78436840045','77554802591']}}
def print_book(book):
    for k,v in book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
            print (i, j, end = " | ")
        print()

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)


