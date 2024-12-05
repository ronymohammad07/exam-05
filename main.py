from add_contant import add_contant
from save_data import load_books
main_list = load_books()

while True:
    print('Welcome To Contant Book Managmeent System')
    print('0. Exit')
    print('1. Add Name')
    
    
    add_ = input('Choise Any Number:')
    
    if add_ == '0':
        print('Thanks! Come Back agine')
        break
        
    elif add_ == '1':
        add_contant(main_list)
        # print('add successfully')
        
    else:
        print('invilid Choise')