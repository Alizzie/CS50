import sys
import csv

def main():
    before_file, after_file = get_filename(sys.argv)

    try:
        before_filecontent = []
        with open(before_file) as file:
            for line in file:
                row = line.rstrip().split(",")
                if len(row) != 3:
                    continue
                write_row(after_file, row)          
    
    except FileNotFoundError:
        sys.exit("File not found")


def write_row(filename, row):
    with open(filename, "a") as file:
        writer = csv.DictWriter(file, fieldnames=["last name", "first name", "house"])
        writer.writerow({"last name": row[0][1:], "first name": row[1][1:-1], "house": row[2]})

def get_filename(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")

    for filename in sys.argv[1:]:
        if filename[-4:] != ".csv":
            sys.exit("Not a CSV file")

    return sys.argv[1:]

if __name__ == "__main__":
    main()