list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            user_date = input("Date: ")
            month, day, year = map(int, user_date.split('/'))
            print(f"{day}")
        except:
            pass

main()