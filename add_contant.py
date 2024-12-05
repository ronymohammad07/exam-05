from save_data import save_data
def add_contant(main_list):
    phone_number = int(input('Enter Your Phone_number: '))
    name = input("Enter Your Name: ")
    email = input('Enter Your Email: ')
    address = input('Enter Your Present Address: ')
    
    
    main_data = {
        'phone_number': phone_number,
        'name': name,
        'email': email,
        'address': address
    }
    
    main_list.append(main_data)
    
    save_data(main_data)
    
    print(f'Contact Add {phone_number}Success')
    return