def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plate_length = len(s)
    
    if not has_valid_length(s) or not starts_with_two_letters(s):
        return False
    
    if not contains_no_punctuation(s):
        return False
    
    
    if not contains_no_digits(s):
        firstDigit = find_first_number(s)
        if s[firstDigit] == "0":
            return False

    return True

def has_valid_length(s):
    return 2 <= len(s) <= 6

def starts_with_two_letters(s):
    return s[:2].isalpha()

def contains_no_punctuation(s):
    return all((c.isalnum()) for c in s)

def find_first_number(s):
    for character in s:
        if character.isdigit():
            return s.index(character)

def contains_no_digits(s):
    return all(c.isalpha() for c in s)

if __name__ == "__main__":
    main()