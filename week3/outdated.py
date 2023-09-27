months = [
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

            if day > 31: 
                    raise Exception()
            	
            print(f"{year}-{month:02}-{day:02}")
        except:
            try:
                month, day, year = user_date.split(" ")
                day = int(day[:-1]) 

                if day > 31: 
                    raise Exception()

                year = int(year)
                month = int(months.index(month)) + 1
                print(f"{year}-{month:02}-{day:02}") 
            except:
                pass
            else:
                break
        else: 
            break

main()