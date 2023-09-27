user_input = input('Extension: ')
user_input = user_input.split('.')
extension = user_input[-1]

match(extension):
    case 'jpeg' | 'gif' | 'jpg' | 'png': 
        print(f'image/{extension}')
    case 'pdf' | 'zip': 
        print(f'application/{extension}')
    case 'txt':
        print(f'text/{extension}')
    case _:
        print('application/octet-stream')
