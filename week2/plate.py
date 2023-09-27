def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plate_length = len(s)
    print(plate_length)
    
    if plate_length < 2 or plate_length > 6:
        return False
    
    start_valid_number = False
    
    for index in range(plate_length):
        character = s[index]
        
        if index < 2 and (not character.isalpha()):
            return False
        elif character.isspace(): 
            return False
        
        if character.isdigit():
            if not start_valid_number and character != "0":
                start_valid_number = True
            else:
                return False
        
        if start_valid_number and character.isalpha():
            return False
    
    return True
    



main()