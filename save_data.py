# save_book_all_data
import csv

def save_data (main_list):
    with open ('save_book_all_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['name', 'phone_number', 'email Address', 'Present Address'])
        # (f'{Titel:<30} {Author:<30} {ISBN:<15} {Year:<10} {Price:<10} {Quantity:<15}')
        for book in main_list:
            writer.writerow(book['phone_number'],[book['name'],  book['email'], book['address']])

def load_books():
    main_list = []
    
    try:
        with open('save_book_all_data.csv', 'r', newline='') as read_book:
            reader = csv.reader(read_book)
            next(reader)
            for book in reader:
                
                main_list.append({
                    'name': book[0],
                    'phone_number': book[1],
                    'email': book[2],
                    'address': book[3],
                })
    except FileNotFoundError:
        pass

    return main_list



