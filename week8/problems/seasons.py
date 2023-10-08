from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    user_input = input("Date of Birth: ")
    birthdate = get_user_birthdate(user_input)
    difference = calculate_difference(birthdate)
    print(sing_difference(difference))


def calculate_difference(birthday):
    today = date.today()
    diff_in_days = (today - birthday).days
    diff_in_min = diff_in_days * 24 * 60
    return diff_in_min

def get_user_birthdate(user_input):
    try:
        year, month, day = map(int, user_input.split("-"))
        return date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

def sing_difference(diff):
    words = p.number_to_words(diff)
    return words


if __name__ == "__main__":
    main()