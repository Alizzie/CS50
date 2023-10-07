from tabulate import tabulate
import sys

def main():
    filename = get_filename(sys.argv)
    file_content = []

    try:
        with open(filename) as file:
            for line in file:
                row = line.rstrip().split(",")
                file_content.append(row)
    except FileNotFoundError:
        sys.exit("File Not found")
    
    table = tabulate(file_content, headers="firstrow", tablefmt="grid")
    print(table)

            

def get_filename(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")
    
    filename = sys.argv[1]

    if filename[-4:] != ".csv":
        sys.exit("Not a Python file")

    return filename

if __name__ == "__main__":
    main()