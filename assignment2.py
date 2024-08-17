
import json

def handle_file(x='a'):
    try:
        with open('file1.json', 'r') as c:
            data = json.load(c)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
        print('File not found, initializing new data.')
    
    if x == 'a':
        username = input('Enter username: ')
        password = input('Enter password: ')

        if username in data:
            print("Username already exists.")
        else:
            data[username] = password
            with open('file1.json', 'w') as c:
                json.dump(data, c)
            print("Signup successful.")
    elif x == 'r':
        username = input('Enter username: ')
        password = input('Enter password: ')

        if username in data and data[username] == password:
            print('Login successful.')
        else:
            print('Login failed.')

def login():
    while True:
        print('1. Signup')
        print('2. Login')
        print('3. Exit')
        a = int(input('Enter your choice: '))
        
        if a == 1:
            handle_file()
        elif a == 2:
            handle_file(x='r')
        elif a == 3:
            break
        else:
            print('Invalid choice.')

login()
